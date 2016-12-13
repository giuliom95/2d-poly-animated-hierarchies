import numpy as np


class Transform(object):
    """
    Defines and contains a transformation matrix.
    """
    
    def __init__(self, parent, translation_func, rotation_func, scale_func):
        """
        Args:
        parent -- The parent transform. If None self is the world transform.
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
        self.mat = np.identity(3)
        self.update_mat(0)
        
        self.children = []
        self.update_parent_children()

        self.world_mat = self.calc_world_mat()
        
    def rebuild_mat(self):
        """
        Rebuilds the transformation matrix according to
        the current translation, rotation and scale.
        """ 
        sin = np.sin(self.rotation)
        cos = np.cos(self.rotation)
        tx, ty = self.translation
        sx, sy = self.scale
        
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
        return np.array([
            np.dot(self.world_mat, vertex) 
            for vertex in vertices
        ])
    
    def calc_world_mat(self):
        """
        Returns the world matrix of the parent.
        If self is the world then returns self.mat 
        """
        if self.parent:
            return np.dot(self.parent.world_mat, self.mat)
        else:
            return self.mat
            
    def update_mat(self, x):
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
           
    def update_all(self, x):
        """
        Updates translation, rotation and scale of self and every child
        according to their associated functions evaluated with x as parameter.
        
        Args:
        x -- Parameter passed to the functions.
        """
        self.update_mat(x)
        self.world_mat = self.calc_world_mat()
        
        [child.update_all(x) for child in self.children]

    def update_parent_children(self):
        """
        Adds transform to the children list of the parent
        """
        if self.parent:
            self.parent.children.append(self)
