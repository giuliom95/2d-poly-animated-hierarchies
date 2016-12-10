import pygame
from pygame.locals import *
from OpenGL.GL import *

from transform import *
from shape import *

SCREEN_SIZE = (600,600)

def main():
    
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    rot = 0
    world = Transform(None)
    
    t1 = Transform(world)
    t1.set_translation([0.3,0])
    
    vertices = np.array([[0,0,1],[.5,0,1],[0,.5,1],[.5,.5,1]])
    faces = [[0,1,2], [1,2,3]]
    colors = [[255,0,0]]*len(vertices)
    s1 = Shape(vertices, colors, faces, t1)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                return
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        rot += 2
        world.set_rotation(rot)
        t1.set_rotation(rot)
        
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
   

