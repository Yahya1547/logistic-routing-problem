from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from graf import *
from math import *
from mtsp import solve
import pygame
from pygame.locals import *

def scale() :
    # Melakukan scaling node pada peta agar sesuai perspektif
    maxX = -1 * float('inf')
    maxY = -1 * float('inf')
    minX = float('inf')
    minY = float('inf')
    # Mencari nilai minimum dan maximum dari sumbu X dan Y
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
    
    # Mengubah koordinat berdasarkan skala yang didapat
    num_scale = max(maxX - minX, maxY - minY)
    for node in dataNode :
        x = dataNode[node][0]
        y = dataNode[node][1]

        newX = x / num_scale
        newY = y / num_scale
        dataNode[node] = (newX, newY, 0)


def map(dest):
    
    radius = 0.001
    
    for node in dataNode :
        posx, posy = dataNode[node][0], dataNode[node][1]
        glBegin(GL_POLYGON)
        
        # Membedakan warna antara titik tujuan dan titik yang bukan tujuan salesman
        if node in dest :
            glColor3f(1, 1, 0)
        else :
            glColor3f(1,0,1)
        
        # Membentuk kotak yang menandakan suatu titik pada peta
        glVertex2f(posx+radius,posy+radius)
        glVertex2f(posx+radius,posy-radius)
        glVertex2f(posx-radius,posy-radius)
        glVertex2f(posx-radius,posy+radius)
        glEnd()
    
def route_line(solution_routes) :
    # Melakukan pencetakan rute dari jalan yang dilalui oleh tiap salesman
    color = [1,0,0]
    i = 0
    for routes in solution_routes :
        glBegin(GL_LINES)
        glColor3f(color[0], color[1], color[2])

        for route in routes :
            path = route[2]
            for pair in path :
                start, end = pair[0], pair[1]
                glVertex2f(dataNode[start][0], dataNode[start][1])
                glVertex2f(dataNode[end][0], dataNode[end][1])

        glEnd()
        # Melakukan pengubahan warna rute untuk tiap salesman yang berbeda
        i += 1
        color[i % 3] += 1
    

def mouseMove(event) :
    # Melakukan zoom in berdasarkan pergerakan mousewheel
    # Zoom dilakukan dengan memanfaatkan scaling pada sumbu x,y, dan z
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: # wheel rolled up
        glScaled(1.05, 1.05, 1.05)
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: # wheel rolled down
        glScaled(0.95, 0.95, 0.95)

def printSolutions(solutions) :
    # Mencetak total jarak pada solusi dari tiap salesman, dan mencetak total jarak yang dilalui seluruh salesman
    sum = 0
    for i in range(len(solutions)) :
        sum += solutions[i]
        print("Solution route for salesman " + str(i+1) + " : " + str(solutions[i]))
    
    print("Total solution : " + str(sum))

def main(dest, solution_routes):
    pygame.init()
 
    display = (w,h)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL, RESIZABLE)

    # Setting posisi dan perspektif dari objek yang di visualisasi
    gluPerspective(45, (1.0*display[0]/display[1]), 0.1, 50.0)
    glTranslatef(-0.5,-0.5, -1.5)
 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # Melakukan perpindahan menggunakan arrow up, down, left, right pada keyboard
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    glTranslatef(0.1,0,0)
                if event.key == pygame.K_RIGHT :
                    glTranslatef(-0.1,0,0)
                if event.key == pygame.K_UP :
                    glTranslatef(0,-0.1,0)
                if event.key == pygame.K_DOWN :
                    glTranslatef(0,+0.1,0)
            
            # melakukan zoom berdasarkan mousewheel event
            mouseMove(event)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        map(dest)
        route_line(solution_routes)

        pygame.display.flip()
        pygame.time.wait(30)


if __name__ == '__main__' : 
    dataNode = buildDataNode()
    solutions, solution_routes, dest = solve()
    scale()
    w,h= 1000,1000
    printSolutions(solutions)
    main(dest, solution_routes)
