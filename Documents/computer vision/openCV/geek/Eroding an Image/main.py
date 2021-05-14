from cv2 import cv2
import numpy as np
from numpy.lib.type_check import imag
image = cv2.imread("se1.png")
cv2.imshow("Image before eroding", image)
cv2.waitKey(0)
kernel = np.ones((5, 5), np.int8)
image = cv2.erode(image, kernel,cv2.BORDER_REFLECT)
cv2.imshow("Image after eroding", image)
cv2.waitKey(0)
cv2.destroyAllWindows()