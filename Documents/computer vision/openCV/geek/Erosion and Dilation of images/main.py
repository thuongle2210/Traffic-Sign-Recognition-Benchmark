from cv2 import cv2
import numpy as np
image = cv2.imread("se1.png")
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(image, kernel, iterations=1)
img_dilate = cv2.dilate(image, kernel, iterations=2)
cv2.imshow("Input", image)
cv2.imshow("Erosion", img_erosion)
cv2.imshow("Dilation", img_dilate)
cv2.waitKey(0)
