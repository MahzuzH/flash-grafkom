import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import math

verts = [
    # Objek Pertama
    # Bagian atas
    (6, 6, 1),  # 0
    (4, 1, 1),  # 1
    (7, 1, 1),  # 2
    (2, -6, 1),  # 3
    (4, -1, 1),  # 4
    (1, -1, 1),  # 5
    # Bagian Bawah
    (6, 6, -1),  # 6
    (4, 1, -1),  # 7
    (7, 1, -1),  # 8
    (2, -6, -1),  # 9
    (4, -1, -1),  # 10
    (1, -1, -1),  # 11

    # Objek Kedua
    (-6, 6, 1),  # 12
    (-4, 1, 1),  # 13
    (-7, 1, 1),  # 14
    (-2, -6, 1),  # 15
    (-4, -1, 1),  # 16
    (-1, -1, 1),  # 17
    # Bagian Bawah
    (-6, 6, -1),  # 18
    (-4, 1, -1),  # 19
    (-7, 1, -1),  # 20
    (-2, -6, -1),  # 21
    (-4, -1, -1),  # 22
    (-1, -1, -1),  # 23

    ]

edges = [
    # Bagian Satu
    (0, 1),
    (0, 6),
    (1, 2),
    (1, 7),
    (2, 8),
    (2, 3),
    (3, 9),
    (3, 4),
    (4, 10),
    (4, 5),
    (5, 11),
    (5, 0),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 10),
    (10, 11),
    (11, 6),

    # Bagian Dua
    (12, 13),
    (12, 18),
    (13, 14),
    (13, 19),
    (14, 20),
    (14, 15),
    (15, 21),
    (15, 16),
    (16, 22),
    (16, 17),
    (17, 23),
    (17, 12),
    (18, 19),
    (19, 20),
    (20, 21),
    (21, 22),
    (22, 23),
    (23, 18)

]

surfaces = {
    (5, 1, 4),
    (1, 4, 2),
    (4, 2, 3),
    (5, 1, 0),
    (11, 7, 10),
    (7, 10, 8),
    (10, 8, 9),
    (11, 7, 6),
    (0, 6, 1),
    (1, 7, 6),
    (1, 7, 2),
    (2, 8, 7),
    (2, 8, 3),
    (9, 3, 8),
    (3, 9, 4),
    (4, 10, 9),
    (4, 10, 5),
    (5, 11, 10),
    (0, 6, 5),
    (5, 11, 6),

    (17, 13, 16),
    (13, 16, 14),
    (16, 14, 15),
    (17, 13, 12),
    (23, 19, 22),
    (19, 22, 20),
    (22, 20, 21),
    (23, 19, 18),
    (12, 18, 13),
    (13, 19, 18),
    (13, 19, 14),
    (14, 20, 19),
    (14, 20, 15),
    (21, 15, 20),
    (15, 21, 16),
    (16, 22, 21),
    (13, 22, 17),
    (17, 23, 22),
    (12, 18, 17),
    (17, 23, 18)
}


def Flash():
    glBegin(GL_TRIANGLES)
    for surface in surfaces:
        glColor3fv((1,1,0))
        for vertex in surface:
            glVertex3fv(verts[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((0,0,0))
        for vertex in edge:
            glVertex3fv(verts[vertex])

    glEnd()


def main():
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.key.set_repeat(1, 10)
    glClearColor(0.6, 0.6, 0.6, 0)

    gluPerspective(70, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, -1, -4)
    glRotated(-90, 1, 0, 0)
    glRotated(90, 0, 0, 1)
    lastPosX = 0
    lastPosY = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    glTranslatef(-0.20, 0, 0.0)
                if event.key == pygame.K_d:
                    glTranslatef(0.20, 0, 0.0)
                if event.key == pygame.K_z:
                    glTranslatef(0.0, 0.20, 0.0)
                if event.key == pygame.K_c:
                    glTranslatef(0.0, -0.20, 0.0)
                if event.key == pygame.K_w:
                    glTranslatef(0.0, 0, 0.20)
                if event.key == pygame.K_s:
                    glTranslatef(0.0, 0, -0.220)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(1, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(1, 0, -1, 0)
                if event.key == pygame.K_UP:
                    glRotatef(1, -1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(1, 1, 0, 0)
                if event.key == pygame.K_RCTRL:
                    glRotatef(1, 0, 0, 1)
                if event.key == pygame.K_RALT:
                    glRotatef(1, 0, 0, -1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Mouse wheel ke atas
                    glScaled(1.05, 1.05, 1.05)
                if event.button == 5:  # Mouse wheel ke bawah
                    glScaled(0.95, 0.95, 0.95)

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                dx = x - lastPosX
                dy = y - lastPosY
                mouseState = pygame.mouse.get_pressed()
                if mouseState[0]:
                    modelView = (GLfloat * 16)()
                    mvm = glGetFloatv(GL_MODELVIEW_MATRIX, modelView)

                    temp = (GLfloat * 3)()
                    temp[0] = modelView[0] * dy + modelView[1] * dx
                    temp[1] = modelView[4] * dy + modelView[5] * dx
                    temp[2] = modelView[8] * dy + modelView[9] * dx
                    norm_xy = math.sqrt(temp[0] * temp[0] + temp[1]
                                        * temp[1] + temp[2] * temp[2])
                    glRotatef(math.sqrt(dx * dx + dy * dy),
                              temp[0] / norm_xy, temp[1] / norm_xy, temp[2] / norm_xy)

                lastPosX = x
                lastPosY = y

        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Flash()

        pygame.display.flip()
        pygame.time.wait(10)


main()