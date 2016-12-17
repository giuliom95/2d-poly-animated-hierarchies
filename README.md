# 2d-poly-animated-hierarchies

A library to manage hierarchies of bi-dimensional polygons 
and basic animations of them.  
It is very slow. It is only a personal project to learn oop in Python.  
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
There is also the *DrawableShape* class: it extends the *Shape* class by
adding the **draw** method, that simply draws the shape through 
OpenGL functions.

## In dev/To do

Check the [Trello board coupled to this repo][4].

[4]: https://trello.com/b/i3FmiFIE/2d-poly-animated-hierarchies
