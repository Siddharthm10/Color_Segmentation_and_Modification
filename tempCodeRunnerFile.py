
upper = np.array([159,255,255])
imgHSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
mask = cv2.inRange(image,lower,upper)
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
b,g,r = cv2.split(gray_image)*3
R = np.multiply(1,r)
G = np.multiply(0,g)
B = np.multiply(0,b)
New_image = cv2.merge((B,G,R))
image[mask>0] = New_image[mask>0]