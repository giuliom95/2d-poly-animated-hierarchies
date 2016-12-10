import numpy as np

class Transform(object):
    """
    Defines and contains a transformation matrix.
    """
    
    def __init__(self, parent):
        """
        Args:
        parent -- The parent transform. If None, this transform 
        will be the world tranform.
        """
        self.parent = parent
        self.translation = [0,0]
        self.rotation = 0
        self.scale = [1,1]
        self.mat = np.identity(3)
            
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
    
    def set_rotation(self, r):
        """
        Sets rotation.
        Updates the transf matrix.
        
        Args:
        r -- New rotation in degrees given as a float.
        """
        self.rotation = np.pi/180 * r
        self.rebuild_mat()
        
    def set_translation(self, t):
        """
        Sets translation.
        Updates the transf matrix.
        
        Args:
        t -- New translation given as a couple of floats.
        """
        self.translation = t[:2]
        self.rebuild_mat()
        
    def set_scale(self, s):
        """
        Sets scale.
        Updates the transf matrix.
        
        Args:
        s -- New scale given as a couple of floats.
        """
        self.scale = s[:2]
        self.rebuild_mat()
        
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
        Calculates the world transf matrix recursively.
        """
        if self.parent is None:
            return self.mat
        else:
            return np.dot(self.parent.calc_world_matrix(), self.mat)
    

