from PIL import Image
import numpy
from numpy import *
def imgtomatrix():
    global matrix_r,matrix_g,matrix_b
    matrix_r = numpy.asarray(r)
    matrix_g = numpy.asarray(g)
    matrix_b = numpy.asarray(b)

def matrixtoimg():
    global R,G,B
    R = Image.fromarray(matrix_R)
    G = Image.fromarray(matrix_G)
    B = Image.fromarray(matrix_B)

def RGB2fan():
    global matrix_R,matrix_G,matrix_B
    imgtomatrix()
    matrix_R = around((matrix_r * 0 + 255) - matrix_r)
    matrix_G = (matrix_g * 0 + 255) - matrix_g
    matrix_B = (matrix_b * 0 + 255) - matrix_b
    print(matrix_R)
    matrixtoimg()
    display()

def gray_pic():
    global matrix_RGB,matrix_R,matrix_G,matrix_B
    imgtomatrix()
    matrix_R = matrix_r * 0.3 + matrix_g * 0.59 + matrix_b * 0.11
    matrix_G = matrix_r * 0.3 + matrix_g * 0.59 + matrix_b * 0.11
    matrix_B = matrix_r * 0.3 + matrix_g * 0.59 + matrix_b * 0.11
    matrixtoimg()
    R.show()
    #display()
def two_value_pic():
    imgtomatrix()
    global matrix_R,R
    #cv2.threshold(im,150,255,THRESH_BINARY_INV)
    matrix_R = matrix_r * 0.3 + matrix_g * 0.59 + matrix_b * 0.11
    R = matrix_R - 180
    print(R)
def display():
    im = Image.merge("RGB", (R,G,B))
    im.show()
if __name__ == '__main__':
    im=Image.open('C:/1.png')
    r,g,b,a = im.split()
    #data = input('DATA:')
    data = 'two_value'
    if data == 'RGB':
       RGB2fan()
    elif data == 'gray':
       gray_pic()
    elif data == 'two_value':
       two_value_pic()
    #print(matrix_r)
    #im.save("save.png","PNG")
