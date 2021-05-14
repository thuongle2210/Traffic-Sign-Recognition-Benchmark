import cv2
import numpy as np

image1 = cv2.imread("input1.jpg")
image2 = cv2.imread("input2.jpg")
sum = cv2.add(image1, image2)
#cv2.imshow("sum Image", sum)
#cv2.waitKey(0)

weightedSum = cv2.addWeighted(image1, 1, image2, 1,0)
#cv2.imshow("input1", image1)
#cv2.imshow("input2", image2)

print(cv2.split(image1)[0])
print(cv2.split(image2)[0])
print(cv2.split(weightedSum)[0])


#cv2.imshow("Weighted Image", weightedSum)
#cv2.waitKey(0)