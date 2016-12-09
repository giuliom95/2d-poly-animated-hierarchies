# 2d-poly-hierarchies

A library to manage hierarchies of bi-dimensional polygons.  
It is written in Python and relies on the [NumPy][1] library.  
The test modules use [PyOpenGL][2] through the [PyGame][3] framework.  

[1]: http://www.numpy.org/
[2]: http://pyopengl.sourceforge.net/
[3]: http://www.pygame.org/

## Architecture

The main classes are *Transform* and *Shape*.  
The first one contains and manages a transformation matrix, while the other
defines a group of triangles by their vertices (they are expressed in 
homogeneous coordinates) and the color of these.  
Every *Shape* needs a *Transform*. The *Transform* objects are hierarchically
managed as trees: every *Transform* has a parent, except for the tree root.
This root will be the transformation matrix of the world.
