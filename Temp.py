import cv2
import numpy as np
import json
import time

img = cv2.imread('images/image_01.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imwrite('Grayscale_image.jpg', gray)
Z = img.reshape((-1,3))
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
# 10 - no of iterations, 1.0 - required accuracy
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 8, 1.0)
_,label,center = cv2.kmeans(Z, 5, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
label = label.reshape((img.shape[:-1]))
label = label.astype(np.uint8)
center = center.astype(np.uint8)
reduced = img[label][center]

cv2.imshow('Output', reduced)
cv2.waitKey(0)
cv2.destroyAllWindows()