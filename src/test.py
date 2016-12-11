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
    
    ticks = 0
    old_ticks = ticks
    old_time = pygame.time.get_ticks()
    
    world = World(
        lambda x: (0.5*np.sin(x*(np.pi/64)), 0),
        lambda x: 0,
        lambda x: (1, 1))
    
    t1 = Transform(
        world,
        lambda x: (0.6*np.cos(x*(np.pi/64)), 0.5*np.sin(x*(np.pi/64))),
        lambda x: x*(np.pi/32),
        lambda x: (1, 1))
    t2 = Transform(
        world,
        lambda x: (0.5*np.cos((x+32)*(np.pi/64)), 0.6*np.sin((x+32)*(np.pi/64))),
        lambda x: x*(np.pi/32),
        lambda x: (1, 1))
    t3 = Transform(
        world,
        lambda x: (0.6*np.cos((x+64)*(np.pi/64)), 0.5*np.sin((x+64)*(np.pi/64))),
        lambda x: x*(np.pi/32),
        lambda x: (1, 1))
    t4 = Transform(
        world,
        lambda x: (0.5*np.cos((x+96)*(np.pi/64)), 0.6*np.sin((x+96)*(np.pi/64))),
        lambda x: x*(np.pi/32),
        lambda x: (1, 1))
    
    
    vertices = np.array([
        [-.25, -.25, 1],
        [+.25, -.25, 1],
        [+.25, +.25, 1],
        [-.25, +.25, 1]])
    faces = [[0,1,2], [0,2,3]]
    colors = [[255,0,0]]*len(vertices)
    s1 = Shape(vertices, colors, faces, t1)
    s2 = Shape(vertices, colors, faces, t2)
    s3 = Shape(vertices, colors, faces, t3)
    s4 = Shape(vertices, colors, faces, t4)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                return
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        world.update_all(ticks)
        ticks += 1
        
        glBegin(GL_TRIANGLES)
        [
            [
                (glColor(color), glVertex(point)) 
                for (color, point) in face
            ] 
            for face in s1.get_faces()
        ]
        [
            [
                (glColor(color), glVertex(point)) 
                for (color, point) in face
            ] 
            for face in s2.get_faces()
        ]
        [
            [
                (glColor(color), glVertex(point)) 
                for (color, point) in face
            ] 
            for face in s3.get_faces()
        ]
        [
            [
                (glColor(color), glVertex(point)) 
                for (color, point) in face
            ] 
            for face in s4.get_faces()
        ]
        glEnd()
                
        pygame.display.flip()
        
        cur_time = pygame.time.get_ticks()
        if cur_time - old_time > 1000:
            print(ticks - old_ticks)
            old_time = cur_time
            old_ticks = ticks


if __name__ == '__main__':
    main()
   

