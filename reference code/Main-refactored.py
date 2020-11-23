

#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):
    global clicked
    global refPt, cropping
    global r,g,b
    # print("inside draw_function\n")
    if event == cv2.EVENT_RBUTTONDOWN:
        # print("inside if EVENT_LBUTTONDBLCLK\n")
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        # time.sleep(5)

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    elif event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", img)


if __name__ == "__main__" :
	
	import cv2
	import numpy as np
	import pandas as pd
	import argparse
	import time


	#Creating argument parser to take image path from command line
	ap = argparse.ArgumentParser()
	ap.add_argument('-i', '--image', required=True, help="Image Path")
	args = vars(ap.parse_args())
	img_path = args['image']

	#Reading the image with opencv
	img = cv2.imread(img_path)
	clone = img.copy()
	result_img = img.copy()


	#declaring global variables (are used later on)
	clicked = False
	refPt = []
	cropping = False
	r = g = b = xpos = ypos = 0

	cv2.namedWindow('image')
	cv2.setMouseCallback('image',draw_function)

	#Setting the lower and Upper Bound
	red_low = np.array([140,40,100])
	red_upper = np.array([179,255,255])

	while(1):

	    cv2.imshow("image",img)
	    key = cv2.waitKey(1) & 0xFF

	    # print(clicked)
	    # time.sleep(5)
	    if (clicked):
	        # print("inside if clicked\n")

	        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
	        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
	        # time.sleep(1)
	        # print("after rectangle\n")

	        #Creating text string to display( Color name and RGB values )
	        text = ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
	        # print("after getColorName" + text)
	        # time.sleep(1)

	        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
	        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
	        # print("after putText\n")

	        #For very light colours we will display text in black colour
	        if(r+g+b>=600):
	            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

	        clicked=False
	    # if the 'r' key is pressed, reset the cropping region
	    if key == ord("r"):
	        img = clone.copy()
	    # if the 'c' key is pressed, break from the loop
	    elif key == ord("c"):
	        break


	# if there are two reference points, then crop the region of interest
	# from teh image and display it
	if len(refPt) == 2:
		#Trimming the image
	    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]

    #Converting image to hsv color
	imgHsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

	#Mask using upper and lower bound
	mask = cv2.inRange(imgHsv, red_low, red_upper)
	# mask_inv = cv2.bitwise_not(mask)

	#Changing the color to color we want to apply
	roi[mask>0] = (0,0,0)

	#applying changes to result_img (final output image)
	result_img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]] = roi

	#showing image
	cv2.imshow("Final", result_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
