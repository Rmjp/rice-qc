import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('img1.jpg',-1)
gr = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
ret,bi = cv.threshold(gr, 145, 255, cv.THRESH_BINARY_INV)
blur = cv.GaussianBlur(bi,(3, 3),0)
cv.imshow("blur", blur)
cv.imshow("gr", gr)
cv.waitKey(0)
cv.destroyAllWindows()

