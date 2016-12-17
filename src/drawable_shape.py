from shape import Shape
from OpenGL.GL import *


class DrawableShape(Shape):
    """
    A drawable polygonal shape.
    """

    def __init__(self, vertices, colors, faces, transform, layer=0):
        """
        :param args: vertices, colors, faces, transform, layer
        """
        Shape.__init__(self, vertices, colors, faces, transform)
        transform.add_shape(self)
        self.layer = layer

    def draw(self):
        """
        Uses OpenGL to draw itself
        :return: None
        """
        glBegin(GL_TRIANGLES)
        [
            [
                (glColor(vcolor), glVertex(point))
                for (vcolor, point) in face]
            for face in self.get_faces()]
        glEnd()
