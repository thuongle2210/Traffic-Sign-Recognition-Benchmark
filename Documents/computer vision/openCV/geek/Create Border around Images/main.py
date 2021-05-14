from cv2 import cv2
image = cv2.imread("geek.png")
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_REFLECT)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()