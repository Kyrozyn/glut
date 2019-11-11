from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'ball_glut'
ypos = 0
zpos = 0
xpos = 0
a = -9
b = -5
c = -30


def kotak(x1, y1, z1, x2, y2, z2):
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x1, y1, z1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x2, y1, z1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x2, y2, z1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x1, y2, z1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x1, y2, z1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x2, y2, z1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x2, y2, z2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x1, y2, z2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x1, y2, z2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x2, y2, z2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x2, y1, z2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x1, y1, z2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x1, y1, z2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x2, y1, z2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x2, y1, z1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x1, y1, z1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x1, y1, z1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x1, y2, z1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x1, y2, z2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x1, y1, z2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x2, y1, z1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x2, y2, z1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x2, y2, z2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x2, y1, z2)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1024, 600)
    glutInitWindowPosition(20, 75)
    glutCreateWindow("gelut")
    glClearColor(0.5, 0.5, 0.5, 0.0);
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glutDisplayFunc(display)
    glutMainLoop()
    return


def display():
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glTranslatef(a, b, c)
    glRotatef(xpos, 1, 0, 0)
    glRotatef(ypos, 0, 1, 0)
    glRotatef(zpos, 0, 0, 1)
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, 2)
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)
    kotak(0, 0.5, 18, 0.5, 10, 0)
    glEnd()
    glPopMatrix()
    glFlush()
    glutSwapBuffers()
    return


if __name__ == '__main__': main()
