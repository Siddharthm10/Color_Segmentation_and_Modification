import cv2
import numpy as np
image = cv2.imread('UsPolo.jpg')
clone = image.copy()

lower = np.array([55,30,26])
upper = np.array([159,255,255])
imgHSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
mask = cv2.inRange(image,lower,upper)
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
temp = (np.multiply(2,cv2.split(gray_image)))

b,g,r = temp[0],temp[0],temp[0]
R = np.multiply(1,r)
G = np.multiply(0,g)
B = np.multiply(0,b)
New_image = cv2.merge((B,G,R))
image[mask>0] = New_image[mask>0]



cv2.imshow("output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

