from cv2 import cv2
import numpy as np
image1 = cv2.imread('input1.png')
image2 = cv2.imread('input2.png')
cv2.imshow("input1", image1)
cv2.waitKey(0)
cv2.imshow("input2", image2)
cv2.waitKey(0)
dest_and = cv2.bitwise_and(image1, image2)
cv2.imshow("Bitwise And",dest_and)
cv2.waitKey(0)
dest_or = cv2.bitwise_or(image1, image2)
cv2.imshow("Bitwise Or",dest_or)
cv2.waitKey(0)

cv2.destroyAllWindows()