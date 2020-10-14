import cv2
import numpy as np

image = cv2.imread('UsPolo.jpg')
imgHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


red_low = np.array([140,40,100])
red_upper = np.array([179,255,255])

mask = cv2.inRange(imgHsv, red_low, red_upper)


image[mask>0] = (0,0,0)
# cv2.GaussianBlur(image, (5,5), cv2.BORDER_DEFAULT)

cv2.imshow("Final", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# from PIL import Image 

# img = Image.open("UsPolo.jpg" )

# def color_image(image_to_transform, color, color_to_apply):
# 	#convert image to rgb
# 	output_image = image_to_transform.convert("RGB")
# 	for x in range(output_image.width):
# 		for y in range(output_image.height):
# 			if output_image.getpixel((x, y)) <= color:
# 				output_image.putpixel((x, y), color_to_apply)
# 	return output_image



# white = (100,100,100)
# green = (0,255,0)
# # print(bool(white<red))

# img_e = color_image(img, white, green)
# img_e.show()
# img.show()