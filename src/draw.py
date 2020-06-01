from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from graf import *
from math import *

dataNode = buildDataNode()

def scale() :
    for node in dataNode :
        x = dataNode[node][0]
        y = dataNode[node][1]

        newX = x/10
        newY = y/10
        dataNode[node] = (newX, newY)

scale()
w,h= 1000,1000
def map():
    glBegin(GL_POINTS)
    radius = 1.5
    for node in dataNode :
        posx, posy = dataNode[node][0], dataNode[node][1]

        for i in range(360) :
            cosine = radius * cos(i*pi/180) + posx
            sine = radius * sin(i*pi/180) + posy
            glVertex2f(cosine, sine)
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
    glColor3f(1.0, 0.0, 3.0)
    map()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()