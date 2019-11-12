from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

texture = GLuint

name = 'aplikasi rumah '
ypos = 0
zpos = 0
xpos = 0
a = -9
b = -5
c = -30


def keyboard(key, x, y):
    ch = key.decode("utf-8")
    global ypos,xpos, a, b, c
    # print(type(key), key, type(ch), ch)
    if ch == 'z':
        ypos = ypos + 5
        if ypos > 360:
            ypos = 0
        glutPostRedisplay()
    if ch == 'x':
        ypos = ypos - 5
        if ypos > 360:
            ypos = 0
        glutPostRedisplay()
    if ch == 'r':
        xpos = xpos + 5
        if xpos > 360:
            xpos = 0
        glutPostRedisplay()
    if ch == 'f':
        xpos = xpos - 5
        if xpos > 360:
            xpos = 0
        glutPostRedisplay()
    if ch == 's':
        b = b + 1
        glutPostRedisplay()
    if ch == 'w':
        b = b - 1
        glutPostRedisplay()
    if ch == 'd':
        a = a - 1
        glutPostRedisplay()
    if ch == 'a':
        a = a + 1
        glutPostRedisplay()
    if ch == 'q':
        c = c + 1
        glutPostRedisplay()
    if ch == 'e':
        c = c - 1
        glutPostRedisplay()
    log()


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


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glTranslatef(a, b, c)
    glRotatef(xpos, 1, 0, 0)
    glRotatef(ypos, 0, 1, 0)
    glRotatef(zpos, 0, 0, 1)
    # dinding+lantai
    dindinglantai()
    # lemari
    lemari()
    # meja
    meja()
    # saklar
    saklar()
    # AC
    ac()
    # kursi
    kursi()
    # laci
    laci()
    # tempat tidur
    tidur()
    # lampu meja
    lampumeja()
    # lemari bawah tv
    lemaribawahtv()
    # komputer
    komputer()
    # laptop
    laptop()
    # tv
    tv()
    # speaker
    speaker()
    # karpet
    karpet()
    #
    glFlush()
    glutSwapBuffers()
    return


def dindinglantai():
    # lantai bawah
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(30))
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)
    kotak(0, 0, 18 + 3, 25 + 7, 0.5, 0)
    glEnd()
    glPopMatrix()
    # dinding belakang
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    kotak(0, 0.5, 0.5, 25 + 7, 10, 0.0)
    glEnd()
    glPopMatrix()
    # dinding Kanan
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(0.5, 1.0, 0.5)
    kotak(25 + 7, 0.5, 18 + 3, 24.5 + 7, 10, 0)
    glEnd()
    glPopMatrix()
    # dinding kiri
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(0.5, 1.0, 0.5)
    kotak(0, 0.5, 18 + 3, 0.5, 10, 0)
    glEnd()
    glPopMatrix()


def meja():
    # meja atas
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.1, 0.1)
    kotak(21 + 7, 3.5, 17 - 7, 24.8 + 7, 3.8, 9.2 - 7)
    # kaki kanan belakang
    kotak(24.3 + 7, 0.5, 16.9 - 7, 24.6 + 7, 3.6, 16.6 - 7)
    # kaki kiri belakang
    kotak(24.3 + 7, 0.5, 9.9 - 7, 24.6 + 7, 3.6, 9.6 - 7)
    # kaki kiri depan
    kotak(21.1 + 7, 0.5, 9.9 - 7, 21.4 + 7, 3.6, 9.6 - 7)
    # kaki kanan depan
    kotak(21.1 + 7, 0.5, 16.9 - 7, 21.4 + 7, 3.6, 16.6 - 7)
    # belakang bawah
    kotak(24.4 + 7, 1, 16.6 - 7, 24.6 + 7, 1.6, 9.9 - 7)
    # kanan bawah
    kotak(21.4 + 7, 1, 16.9 - 7, 24.3 + 7, 1.6, 16.7 - 7)
    # kiri bawah
    kotak(21.4 + 7, 1, 9.8 - 7, 24.3 + 7, 1.6, 9.9 - 7)
    glEnd()
    glPopMatrix()


def kursi():
    # kursi
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(3))
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.1, 0.1)
    kotak(18 + 7, 2.2, 15.5 - 7, 20.8 + 7, 2.5, 12.8 - 7)
    # kiri depan
    kotak(20.5 + 7, 0.5, 15.5 - 7, 20.8 + 7, 2.5, 15.2 - 7)
    # kanan depan
    kotak(20.5 + 7, 0.5, 13.1 - 7, 20.8 + 7, 2.5, 12.8 - 7)
    # kanan belakang
    kotak(18 + 7, 0.5, 13.1 - 7, 18.3 + 7, 5.2, 12.8 - 7)
    # kiri belakang
    kotak(18 + 7, 0.5, 15.5 - 7, 18.3 + 7, 5.2, 15.2 - 7)
    # senderan
    kotak(18 + 7, 3.8, 15.5 - 7, 18.2 + 7, 4.9, 12.8 - 7)
    glEnd()
    glPopMatrix()


def lemari():
    # dudukan lemari
    glPushMatrix()
    glRotatef(90.0, 0, 1, 0)
    glTranslated(23.5 - 25.3, -3.0 + 3.5, 6.0 + 9)
    glScaled(2.0, 0.5, 9.5)
    glColor3d(0.92, 0.51, 0.23)
    glutSolidCube(1)
    glPopMatrix()
    # lemarinya
    glPushMatrix()
    glRotatef(90.0, 0, 1, 0)
    glTranslated(23.5 - 25.3, 2.0 + 3.5, 4.5 + 10)
    glScaled(2.6, 9.5, 7.5)
    glColor3d(1.0, 0.4, 0.0)
    glutSolidCube(1)
    glPopMatrix()
    # pintu lemari
    glPushMatrix()
    glRotatef(90.0, 0, 1, 0)
    glTranslated(22.15 - 25.3, 2.0 + 3.5, 3.3 + 10)
    glScaled(0.2, 8.5, 3.6)
    glColor3d(1.0, 0.6, 0.0)
    glutSolidCube(1)
    glPopMatrix()
    # Cermin Lemari
    glPushMatrix()
    glRotatef(90.0, 0, 1, 0)
    glTranslated(22.15 - 25.3, 2.0 + 3.5, 6.8 + 10)
    glScaled(0.2, 8.5, 2.0)
    glColor3d(1.0, 1.0, 1.0)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()  # Motif 1 dari bawah
    glRotatef(90.0, 0, 1, 0)
    glTranslated(22.0 - 25.3, -1.2 + 3.5, 3.3 + 10)
    glScaled(0.2, 1.0, 2.6)
    glColor3d(1.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()  # Motif 2 dari bawah
    glRotatef(90.0, 0, 1, 0)
    glTranslated(22.0 - 25.3, 0.8 + 3.5, 3.3 + 10)
    glScaled(0.2, 1.0, 2.6)
    glColor3d(1.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()  # Motif 3 dari bawah 
    glRotatef(90.0, 0, 1, 0)
    glTranslated(22.0 - 25.3, 2.8 + 3.5, 3.3 + 10)
    glScaled(0.2, 1.0, 2.6)
    glColor3d(1.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()  # Motif 1 dari bawah
    glRotatef(90.0, 0, 1, 0)
    glTranslated(22.0 - 25.3, 4.8 + 3.5, 3.3 + 10)
    glScaled(0.2, 1.0, 2.6)
    glColor3d(1.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()


def saklar():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(10))
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    kotak(6.5, 6.5, 0.6, 7.5, 7.5, 0.5)
    glColor3f(1.0, 1.0, 1.0)
    kotak(6.65, 6.7, 0.65, 6.92, 7.3, 0.6)
    kotak(7.08, 6.7, 0.65, 7.35, 7.3, 0.6)
    glEnd()
    glPopMatrix()


def ac():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(10))
    glBegin(GL_QUADS)
    glColor3f(1.1, 1.1, 1.1)
    kotak(0.55, 8.45, 10.2 + 5, 1.2, 9.7, 6.5 + 3)
    glColor3f(0.0, 0.0, 0.0)
    kotak(1.2, 8.5, 10.2 + 5, 1.25, 8.45, 6.5 + 3)
    kotak(1.2, 8.6, 10.1 + 5, 1.25, 8.62, 6.6 + 3)
    kotak(1.2, 9.58, 10.1 + 5, 1.25, 9.6, 7 + 3)
    kotak(1.2, 9.52, 10.2 + 5, 1.25, 9.54, 6.5 + 3)
    kotak(0.55, 8.39, 10.1 + 5, 1.15, 8.4, 6.6 + 3)
    glEnd()
    glPopMatrix()


def laci():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0.0)
    kotak(0.5, 0.8, 8.5, 4, 4.5, 4.7)
    # kaki kiri
    kotak(0.5, 0.5, 8.5, 4.3, 4.9, 8.3)
    # kaki kanan
    kotak(0.5, 0.5, 4.5, 4.3, 4.9, 4.7)
    # pegangan
    kotak(4.2, 2.1, 6.9, 4.3, 2.3, 6.2)
    kotak(4.2, 3.9, 6.9, 4.3, 4.1, 6.2)
    glEnd()
    glPopMatrix()
    # lacinya
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(3))
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.1, 0.1)
    kotak(4, 1, 8.2, 4.2, 2.5, 4.9)
    kotak(4, 2.7, 8.2, 4.2, 4.3, 4.9)
    glEnd()
    glPopMatrix()


def tidur():
    # Tempat Tidur
    # rangka 
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.2, 0.1)
    kotak(1.1, 1.4, 15.5, 13.4, 3, 8.7)
    # kaki 1
    kotak(0.5, 0.5, 15.6, 1.2, 5.3, 14.9)
    # kaki 2
    kotak(0.5, 0.5, 9.4, 1.1, 5.3, 8.7)
    # kaki 3
    kotak(12.9, 0.5, 9.4, 13.6, 4.5, 8.7)
    # kaki 4
    kotak(12.9, 0.5, 15.6, 13.6, 4.5, 14.9)
    # penyangga depan
    kotak(0.6, 3, 15.4, 1, 5.3, 8.9)
    # penyangga belakang
    kotak(12.9, 1.4, 15.4, 13.6, 4.5, 8.9)
    glEnd()
    glPopMatrix()
    # kasur
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(1))
    glBegin(GL_QUADS)
    glColor3f(1.1, 1.1, 1.1)
    kotak(1.1, 2.5, 15.4, 13.4, 3.5, 9)
    # bantal
    glColor3f(0.7, 0.7, 0.7)
    kotak(1.3, 3.5, 15.3, 3, 4, 12.8)
    kotak(1.3, 3.5, 12.2, 3, 4, 9.2)
    # selimut
    glColor3f(0.8, 0.1, 0.1)
    kotak(5, 3.5, 15.4, 13.4, 3.7, 14)
    glColor3f(0.5, 0.1, 0.1)
    kotak(5, 3.5, 14, 13.4, 3.7, 13)
    glColor3f(0.8, 0.1, 0.1)
    kotak(5, 3.5, 13, 13.4, 3.7, 12)
    glColor3f(0.5, 0.1, 0.1)
    kotak(5, 3.5, 12, 13.4, 3.7, 11)
    glColor3f(0.8, 0.1, 0.1)
    kotak(5, 3.5, 11, 13.4, 3.7, 10)
    glColor3f(0.5, 0.1, 0.1)
    kotak(5, 3.5, 10, 13.4, 3.7, 9)
    glColor3f(0.8, 0.1, 0.1)
    # sisi kanan
    kotak(5, 3, 9, 13.4, 3.6, 8.9)
    glColor3f(0.5, 0.1, 0.1)
    # sisi kiri
    kotak(5, 3, 15.5, 13.4, 3.6, 15.4)
    glEnd()
    glPopMatrix()


def lampumeja():
    # Lampu Meja syahril
    glPushMatrix()  # Cone Putih 
    glTranslated(1.7 + 0.3, 0.85 - 0.3 + 5.2, 23.5 - 17)
    glRotated(-90, 1, 0, 0)
    glScaled(1.5 - 0.32, 1.5 - 0.32, 1.5 - 0.32)
    glColor3d(1.0, 1.0, 1.0)
    glutSolidCone(1, 1, 35, 35)
    glPopMatrix()
    glPushMatrix()  # Bola Hitam Tengah 
    glTranslated(1.7 + 0.3, 0.0 + 5.2, 23.5 - 17)
    glScaled(0.9 - 0.32, 1.2 - 0.32, 0.9 - 0.32)
    glColor3d(0.0, 0.0, 0.0)
    glutSolidSphere(1, 35, 35)
    glPopMatrix()


def lemaribawahtv():
    glPushMatrix()
    glRotatef(180.0, 0, 1, 0)
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0.0)
    kotak(0.5 - 32, 0.8, 8.5 - 21, 4 - 33.7, 4.5 - 2, 4.7 - 23)
    # kaki kiri
    kotak(0.5 - 32, 0.5, 8.5 - 21, 4.3 - 33.7, 4.9 - 2, 8.3 - 21)
    # kaki kanan
    kotak(0.5 - 32, 0.5, 4.5 - 23, 4.3 - 33.7, 4.9 - 2, 4.7 - 23)
    # pegangan
    kotak(4.2 - 33.7, 2.1, 6.9 - 22, 4.3 - 33.7, 2.3, 6.2 - 22)
    glEnd()
    glPopMatrix()
    # lacinya
    glPushMatrix()
    glRotatef(180.0, 0, 1, 0)
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.1, 0.1)
    kotak(4 - 33.7, 1, 8.2 - 21, 4.2 - 33.7, 2.5, 4.9 - 23)
    glEnd()
    glPopMatrix()


def komputer():
    # Komputer
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    # cpu
    kotak(21.5 + 7, 3.8, 11.8 - 7, 23.5 + 7, 6, 10.8 - 7)
    # Monitor lcd
    kotak(23.3 + 7, 4.1, 15.5 + 1.3 - 7, 23.5 + 7, 6.4, 12.2 - 7)
    kotak(23.5 + 7, 4.3, 15.3 + 1.3 - 7, 23.6 + 7, 6.2, 12.4 - 7)
    kotak(23.6 + 7, 3.8, 14 + 1.3 - 7, 23.8 + 7, 6, 13.5 - 7)
    kotak(23.4 + 7, 3.8, 14.3 + 1.2 - 7, 23.9 + 7, 4, 13.2 - 7)
    # keyboard
    kotak(21.8 + 7, 3.8, 12.3 - 6.3, 23 + 7, 4, 15.2 - 6.3)
    glEnd()
    glPopMatrix()
    # layar lcd
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(8))
    glBegin(GL_QUADS)
    glColor3f(1.1, 1.0, 1.0)
    kotak(23.29 + 7, 4.3, 15.3 + 1.2 - 7, 23.29 + 7, 6.2, 12.4 - 7)
    glEnd()
    glPopMatrix()
    # cpu
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(4))
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)
    kotak(21.49 + 7, 3.8, 11.8 - 7, 21.5 + 7, 6, 10.8 - 7)
    glEnd()
    glPopMatrix()


def laptop():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    # Monitor lcd
    kotak(8.3, 3.8, 11.20, 10.4, 5.3, 11.30)
    # keyboard
    kotak(8.3, 3.8, 11.3, 10.35, 4, 12.3)
    glEnd()
    glPopMatrix()
    # layar lcd
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(8))
    glBegin(GL_QUADS)
    glColor3f(1.1, 1.0, 1.0)
    kotak(8.4, 4.0, 11.31, 10.3, 5.2, 11.32)
    glEnd()
    glPopMatrix()


def tv():
    # TV
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(2))
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    kotak(23.3 + 7.4, 4.1 - 0.5, 15.5 + 3.4, 23.5 + 7.4, 6.4 + 1, 12.2)
    kotak(23.5 + 7.4, 4.3 - 0.5, 15.3 + 3.4, 23.6 + 7.4, 6.2 + 1, 12.4)
    kotak(23.6 + 7.4, 3.8 - 0.5, 14 + 1 + 3.4, 23.8 + 7.4, 6 + 1, 13.5 - 1)
    glEnd()
    glPopMatrix()
    # layar
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(8))
    glBegin(GL_QUADS)
    glColor3f(1.1, 1.0, 1.0)
    kotak(23.29 + 7.4, 4.3 - 0.5, 15.3 + 3.4, 23.29 + 7.4, 6.2 + 1, 12.4)
    glEnd()
    glPopMatrix()


def speaker():
    # Speaker
    glPushMatrix()  # Box Speaker Hitam Kiri
    glTranslated(23.7 + 7, 0.4 + 2.9, 13.4 - 2.1)
    glScaled(2.0 - 0.7, 5.5, 2.0 - 0.9)
    glColor3d(0.1, 0.1, 0.1)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()  # Speaker Depan Kiri
    glTranslated(22.7 + 0.3 + 7, 0.7 + 2.9, 13.4 - 2.1)
    glScaled(0.3 - 0.1, 4.5, 1.5 - 0.7)
    glColor3d(0.2, 0.2, 0.2)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()  # Speaker Kiri Tombol 1
    glTranslated(22.7 + 0.4 + 7, -2.0 + 2.9, 23.1 - 12.1)
    glScaled(0.15, 0.15, 0.15)
    glColor3d(1.0, 1.0, 1.0)
    glutSolidSphere(1, 35, 35)
    glPopMatrix()
    glPushMatrix()  # Speaker Kiri Tombol 2
    glTranslated(22.7 + 0.4 + 7, -2.0 + 2.9, 23.6 - 12.1)
    glScaled(0.15, 0.15, 0.15)
    glColor3d(1.0, 1.0, 1.0)
    glutSolidSphere(1, 35, 35)
    glPopMatrix()
    glPushMatrix()  # Box Speaker Hitam Kanan
    glTranslated(23.7 + 7, 0.4 + 2.9, 23.6 - 3.8)
    glScaled(2.0 - 0.7, 5.5, 2.0 - 0.9)
    glColor3d(0.1, 0.1, 0.1)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()  # Speaker Depan Kanan
    glTranslated(22.7 + 0.3 + 7, 0.7 + 2.9, 23.6 - 3.8)
    glScaled(0.3 - 0.1, 4.5, 1.5 - 0.7)
    glColor3d(0.2, 0.2, 0.2)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()  # Speaker Kanan Tombol 1
    glTranslated(22.7 + 0.4 + 7, -2.0 + 2.9, 23.1 - 3.6)
    glScaled(0.15, 0.15, 0.15)
    glColor3d(1.0, 1.0, 1.0)
    glutSolidSphere(1, 35, 35)
    glPopMatrix()
    glPushMatrix()  # Speaker Kanan Tombol 2
    glTranslated(22.7 + 0.4 + 7, -2.0 + 2.9, 23.6 - 3.6)
    glScaled(0.15, 0.15, 0.15)
    glColor3d(1.0, 1.0, 1.0)
    glutSolidSphere(1, 35, 35)
    glPopMatrix()


def karpet():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture(1))
    glBegin(GL_QUADS)
    glColor3f(0.1, 0.3, 0.1)
    kotak(0, 0, 17, 20, 0.51, 5)
    glEnd()
    glPopMatrix()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0 * w / h, 1.0, 40.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, 0.0)
    gluLookAt(1.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def log():
    print("xpos = " + str(xpos) + " ypos = " + str(ypos) + " zpos = " + str(zpos))
    print("a = " + str(a) + " b = " + str(b) + " c = " + str(c))


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1024, 600)
    glutInitWindowPosition(20, 75)
    glutCreateWindow(name)
    glClearColor(0.5, 0.5, 0.5, 0.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)

    glutMainLoop()
    return


if __name__ == '__main__': main()
