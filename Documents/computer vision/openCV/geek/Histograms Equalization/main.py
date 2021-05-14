from cv2 import cv2 
import numpy as np

image = cv2.imread("dog.png", 0)

equ = cv2.equalizeHist(image)
print(equ)
res = np.hstack((image, equ))
print(res)
cv2.imshow("image", res)
cv2.waitKey(0)