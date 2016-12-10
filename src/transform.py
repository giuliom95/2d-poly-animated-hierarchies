import numpy as np

class Transform(object):
    """
    Defines and contains a transformation matrix.
    """
    
    def __init__(self, parent, translation_func, rotation_func, scale_func):
        """
        Args:
        parent -- The parent transform. If None, this transform 
        will be the world tranform.
        translation_func -- Translation function.
        rotation_func -- Rotation function.
        scale_func -- Scale function.
        """
        self.parent = parent
        
        self.translation_func = translation_func
        self.rotation_func = rotation_func
        self.scale_func = scale_func
        
        self.translation = None
        self.rotation = None
        self.scale = None
        self.mat = None
        self.update(0)
        
            
    def rebuild_mat(self):
        """
        Rebuilds the transformation matrix according to
        the current translation, rotation and scale.
        """ 
        sin = np.sin(self.rotation)
        cos = np.cos(self.rotation)
        tx, ty = self.translation
        sx, sy = self.scale
        
        self.mat = np.identity(3)
        self.mat[0][0] = sx * cos
        self.mat[0][1] = -1 * sin
        self.mat[1][0] = sin
        self.mat[1][1] = sy * cos
        self.mat[0][2] = tx
        self.mat[1][2] = ty
        
    def get_vertices(self, vertices):
        """
        Applies the transformation to a list of vertices
        
        Args:
        vertices -- A list of vertices given in homogeneous coordinates.
        """
        world_mat = self.calc_world_matrix()
        return np.array([
            np.dot(world_mat, vertex) 
            for vertex in vertices
        ])
    
    def calc_world_matrix(self):
        """
        Calculates recursively the world transform matrix.
        """
        if self.parent is None:
            return self.mat
        else:
            return np.dot(self.parent.calc_world_matrix(), self.mat)
            
    def update(self, x):
        """
        Updates translation, rotation and scale according to their
        associated functions evaluated with x as parameter.
        
        Args:
        x -- Parameter passed to the functions.
        """
        self.translation = self.translation_func(x)
        self.rotation = self.rotation_func(x)
        self.scale = self.scale_func(x)
        self.rebuild_mat()


