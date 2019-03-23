import numpy as np
import cv2

img = cv2.imread('cara1.png',0)
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert color image to grayscale
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite('clahe_2.png',cl1)
cv2.imwrite('clahe_1.png',img)
