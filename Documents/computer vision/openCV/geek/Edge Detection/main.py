from cv2 import cv2
import numpy as np
image = cv2.imread("dog.jpg")
image = cv2.resize(image,(300, 300))
edge_detection = cv2.Canny(image,120, 200)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imshow("Edge Detection",edge_detection)
cv2.waitKey(0)
cv2.destroyAllWindows()