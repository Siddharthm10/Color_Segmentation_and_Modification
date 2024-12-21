import cv2
import numpy as np
import matplotlib.pyplot as plt

#BGR image
img_original = cv2.imread("images/image_01.jpg")
img_original = cv2.resize(img_original, (600,600))

# RGB image
img_rgb_0 = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

# HSV image 
img_hsv_0 = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)

# reshaping for Kmeans
x_hsv_0 = np.float32(img_hsv_0.reshape(-1,3))
print(x_hsv_0)

# Applying Kmeans
no_of_colors = 4
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
_,labels,centers = cv2.kmeans(x_hsv_0, no_of_colors, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
labels = labels.reshape((img_original.shape[:-1]))
centers = centers.astype(np.uint8)
print(labels)
print(centers)
plt.show((np.ones((100,100)))*cv2.cvtColor(centers[1], cv2.COLOR_HSV2RGB))
# selecting labels -> coloring those labels
# img_hsv_red_0 = img_hsv_0.copy()
# for l in range(len(np.unique(labels))):
#     mask = cv2.inrange(labels, l, l)
#     img_hsv_red_0[mask>0] = centers[l]
