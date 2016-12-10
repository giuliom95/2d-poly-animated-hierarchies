import pygame
from pygame.locals import *
from OpenGL.GL import *

from transform import *
from shape import *

import numpy as np

SCREEN_SIZE = (600,600)

def main():
    
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    time = 0
    
    world = Transform(
        None,
        lambda x: (0, 0),
        lambda x: 0,
        lambda x: (1, 1))
    
    t1 = Transform(
        world,
        lambda x: (0.5*np.sin(x*(np.pi/64)), 0.5*np.cos(x*(np.pi/64))),
        lambda x: x*(np.pi/64),
        lambda x: (1, 1))
    
    vertices = np.array([
        [-.25, -.25, 1],
        [+.25, -.25, 1],
        [+.25, +.25, 1],
        [-.25, +.25, 1]])
    faces = [[0,1,2], [0,2,3]]
    colors = [[255,0,0]]*len(vertices)
    s1 = Shape(vertices, colors, faces, t1)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                return
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        time += 1
        world.update(time)
        t1.update(time)
        
        glBegin(GL_TRIANGLES)
        [
            [
                (glColor(color), glVertex(point)) 
                for (color, point) in face
            ] 
            for face in s1.get_faces()
        ]
        glEnd()
                
        pygame.display.flip()
        
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
   

