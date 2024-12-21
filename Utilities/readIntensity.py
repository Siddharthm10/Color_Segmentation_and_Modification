import cv2
import numpy as np
import time
image = cv2.imread('UsPolo.jpg')
clone = image.copy()
beta = 3
lower = np.array([55,30,26])
upper = np.array([159,255,255])
imgHSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
mask = cv2.inRange(image,lower,upper)
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# gray_image = np.dstack((gray_image,gray_image,gray_image))
# clone[mask>0] = gray_image[mask>0]
# temp = np.array(np.multiply(2,cv2.split(gray_image)))
# np.array(np.where(temp[0]>255))[1][:] 
# print(np.array(np.where(temp[0]>255)).shape)
# time.sleep(20)

gray_image[mask>0] += 115
temp = np.array(cv2.split(gray_image))
temp[temp>255]=255

b,g,r = temp[0],temp[0],temp[0]
R = np.multiply(1,r)
G = np.multiply(0,g)
B = np.multiply(0,b)
New_image = cv2.merge((B,G,R))
# New_image = np.dstack((B,G,R))
image[mask>0] = New_image[mask>0]

# print((np.amin(temp[0][mask>0]),np.max(temp[0][mask>0])))
# time.sleep(20)

# #color showcasing
# color = np.zeros((300,300,3), np.uint8)
# color[:] = (0,0,255)
# print(np.amin(temp[0])
# # cv2.imshow("color_entered",color)
cv2.imshow("output", temp[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
# print((np.amin(gray_image)))
# print(np.array(np.where(gray_image<10)).shape)
# print(temp)