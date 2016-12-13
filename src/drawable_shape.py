from shape import Shape
from OpenGL.GL import *


class DrawableShape(Shape):
    """
    A drawable polygonal shape.
    """

    def __init__(self, *args):
        """
        :param args: vertices, colors, faces, transform
        """
        Shape.__init__(self, *args)
        _, _, _, transform = args
        transform.add_shape(self)

    def draw(self):
        """
        Uses OpenGL to draw itself
        :return: None
        """
        [
            [
                (glColor(vcolor), glVertex(point))
                for (vcolor, point) in face]
            for face in self.get_faces()]
