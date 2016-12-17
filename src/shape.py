class Shape(object):
    """
    A polygonal shape made of triangles.
    """
    
    def __init__(self, vertices, colors, faces, transform):
        """
        Args:
        :param vertices: A list of vertices given in homogeneous coordinates.
        :param colors: A list that assigns a vertex to a color
        :param faces: A list of triangular faces given as triples of indexes.
        :param transform: The transform to apply to this shape
        """
        self.vertices = vertices
        self.colors = colors
        self.faces = faces
        self.transform = transform
        
    def get_faces(self):
        """
        Returns a list of triples of colored vertices transformed 
        according to self.transform and sorted per face.
        """
        transf_vs = self.transform.get_vertices(self.vertices)
        return [[(self.colors[v], transf_vs[v]) for v in f] for f in self.faces]
