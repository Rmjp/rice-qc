import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#input and binary
img = cv.imread('img1.jpg',-1)
gr = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
ret,bi = cv.threshold(gr, 150, 255, cv.THRESH_BINARY_INV)

#preprocessing(Gaussian, ero)
blur = cv.GaussianBlur(bi,(3, 3),0)

kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(blur, cv.MORPH_OPEN, kernel)

kernel = np.ones((3,3),np.uint8)
closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

ret,pre = cv.threshold(closing, 160, 255, cv.THRESH_BINARY)

#imshow
cv.imshow("clo", closing)
cv.imshow("ope", opening)
cv.imshow("bi", bi)
cv.waitKey(0)
cv.destroyAllWindows()

