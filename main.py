def customize_function(event, x, y, flags, params):
    global xpos,ypos
    global b,g,r
    global label,l
    global refPt
    
    if event == cv2.EVENT_RBUTTONDOWN:
        # b,g,r = img[y,x]
        #identifying the label on which the user clicks
        l=int(label[y,x])

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    elif event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))

        # draw a rectangle around the region of interest
        cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow('demo', img)




def change_color(img, color_to_apply):

    #making mask from the provided label
    mask = cv2.inRange(label,l,l)
    #making a grayscale image to save the textures
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #saving the grayscale image with threshold, to lower the dark areas
    temp = np.multiply(grayscale_Threshold, cv2.split(gray_img))
    #saving the bgr with same values(values of the grayscale image)
    b,g,r = temp[0],temp[0],temp[0]
    #initiating the numpy arrays and multiplying with the rgb colors in order to apply a new color 1,0,0 represents normalized color red
    R = np.multiply(1,r)
    G = np.multiply(0,g)
    B = np.multiply(0,b)
    #merging these color into a new image
    New_image = cv2.merge((B,G,R))
    #multifunctionality(1: apply color to complete image ;  2: applying color to the ROI selected)
    if(len(refPt)<2):
        img[mask>0]= New_image[mask>0]
    else:
        img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]][mask[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]>0] = New_image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]][mask[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]>0]


    
    #Saving the modified image
    cv2.imwrite("Result.jpg", img)
    #Showing the modified image  
    # cv2.imshow('demo',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img



def image_preprocessing(img, no_of_colors):
    # img = cv2.resize(img, (600,400), interpolation = cv2.INTER_AREA)
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    # 10 - no of iterations, 1.0 - required accuracy
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    _,label,center = cv2.kmeans(Z, no_of_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    label = label.reshape((img.shape[:-1]))
    # Now convert back into uint8, and make original image
    reduced = np.uint8(center)[label]
    
    return reduced, label, center


#######################################################################################################
if __name__ == "__main__":

    #importing important Libraries
    import cv2
    import numpy as np
    import argparse
    # import imutils
    import time

    #creating argument parser to take image from command line
    ap = argparse.ArgumentParser()
    ap.add_argument("-i","--image",help = "Enter the Path to image")
    args = vars(ap.parse_args())
    img_path = args['image']

    #Reading the image and making a copy with OpenCV : s_img -> Showcased image
    img = cv2.imread(img_path)
    s_img = img.copy() #output image 
    clone = img.copy() #clone for reseting
    # reduced = img.copy() #copy for reduced colors using kmeans

    #initializing Global variables
    l=0
    refPt = []


    #other variables
    no_of_colors = 5
    color_to_apply = (0,0,255)
    grayscale_Threshold = 2 #should be greater than 1 for image to be light otherwise for a darker variant it should be less than 1 $$

    #Pre-process image 
    _,label,center = image_preprocessing(img, no_of_colors) # Kmeans colored image
    
    #creating a named window for the image we want to show : demo
    cv2.namedWindow('demo')
    #callback on demo
    cv2.setMouseCallback('demo', customize_function)
    while(1):
        #show image on which changes will be made
        cv2.imshow('demo', img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            #reset if r is pressed
            img = clone.copy()
            xpos=r=g=b=ypos=l=0
            refPt = []
        if key == ord('c'):
            #show output if c is pressed
            img = change_color(img, color_to_apply)
            
        elif key == ord('q'):
            #quit if q is pressed
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#######################################################################################################
