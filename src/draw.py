from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from graf import *
from math import *
from mtsp import solve
import pygame
from pygame.locals import *

lastPosX = 0
lastPosY = 0
zoomScale = 1.0
dataL = 0
xRot = 0
yRot = 0
zRot = 0
dataNode = buildDataNode()
# solutions, solution_routes, dest = solve()

verticies = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def scale() :
    maxX = -1 * float('inf')
    maxY = -1 * float('inf')
    minX = float('inf')
    minY = float('inf')
    for node in dataNode :
        x = dataNode[node][0]
        y = dataNode[node][1]
        if x > maxX :
            maxX = x
        if y > maxY :
            maxY = y
        if x < minX :
            minX = x
        if y < minY :
            minY = y
    
    num_scale = max(maxX - minX, maxY - minY)
    for node in dataNode :
        x = dataNode[node][0]
        y = dataNode[node][1]

        newX = x / num_scale
        newY = y / num_scale
        dataNode[node] = (newX, newY, 0)

    # for node in dataNode :
    #     x = dataNode[node][0]
    #     y = dataNode[node][1]

    #     newX = x/10
    #     newY = y/10
    #     dataNode[node] = (newX, newY, 0)

scale()
w,h= 1000,1000
def map():
    
    radius = 0.001
    
    for node in dataNode :
        posx, posy = dataNode[node][0], dataNode[node][1]
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 0)
        glVertex2f(posx+radius,posy+radius)
        glVertex2f(posx+radius,posy-radius)
        glVertex2f(posx-radius,posy-radius)
        glVertex2f(posx-radius,posy+radius)
        glEnd()
    
def route_line() :
    glBegin(GL_LINES)
    glColor3f(0, 1, 0)
    for pair in route :
        start, end = pair[0], pair[1]
        glVertex2f(dataNode[start][0], dataNode[start][1])
        glVertex2f(dataNode[end][0], dataNode[end][1])
    glEnd()

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    map()
    # route_line()
    # glutSwapBuffers()

def mouseMove(event) :
    global lastPosX, lastPosY, zoomScale, xRot, yRot, zRot
 
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: # wheel rolled up
        glScaled(1.05, 1.05, 1.05)
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: # wheel rolled down
        glScaled(0.95, 0.95, 0.95)

def moveLeft() :
    for node in dataNode :
        x = dataNode[node][0]
        y = dataNode[node][1]

        newX = x - 1
        dataNode[node] = (newX, y, 0)

def main():
    pygame.init()
 
    display = (w,h)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL, RESIZABLE)

    gluPerspective(45, (1.0*display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    glTranslatef(0.1,0,0)
                if event.key == pygame.K_RIGHT :
                    glTranslatef(-0.1,0,0)
                if event.key == pygame.K_UP :
                    glTranslatef(0,-0.1,0)
                if event.key == pygame.K_DOWN :
                    glTranslatef(0,+0.1,0)
            mouseMove(event)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # showScreen()
        # Cube()
        map()
        pygame.display.flip()
        pygame.time.wait(30)


main()
