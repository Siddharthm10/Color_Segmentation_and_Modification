import numpy as np
import cv2


def image_preprocessing(img, no_of_colors):
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    # 10 - no of iterations, 1.0 - required accuracy
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 8, 1.0)

    _,label,center = cv2.kmeans(Z, no_of_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    label = label.reshape((img.shape[:-1]))
    # Now convert back into uint8, and make original image
    # reduced = np.uint8(center)[label]
    
    return label, center

