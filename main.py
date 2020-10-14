def customize_function(event, x, y, flags, params):
    global l,label
    global refPt
    global Updated
    
    if event == cv2.EVENT_RBUTTONDOWN:
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
        cv2.rectangle(s_img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow('demo', s_img)




def change_color(img, color_to_apply):

    #making mask from the provided label
    mask = cv2.inRange(label,l,l)
    #making a grayscale image to save the textures
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #saving the grayscale image with threshold, to lower the dark areas
    temp = np.multiply(grayscale_Threshold, cv2.split(gray_img))
    #saving the bgr with same values(values of the grayscale image)
    b,g,r = temp[0],temp[0],temp[0]
    #initiating the numpy arrays and multiplying with the rgb colors 
    #in order to apply a new color 1,0,0 represents normalized color red
    R = np.multiply(color_to_apply[0],r)
    G = np.multiply(color_to_apply[1],g)
    B = np.multiply(color_to_apply[2],b)
    #merging these color into a new image
    New_image = cv2.merge((B,G,R))
    #multi-functionality(1: apply color to complete image;
    #2: applying color to the ROI selected)
    if(len(refPt)<2):
        img[mask>0]= New_image[mask>0]
    else:
        img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]][mask[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]>0] = New_image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]][mask[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]>0]

    #Saving the modified image
    # cv2.imwrite("Result.jpg", img)
    return img


###############################################################################################
if __name__ == "__main__":

    #importing important Libraries
    import cv2
    import numpy as np
    import argparse
    import json
    import time
    from Utilities.Popup import input_color
    from Utilities.preprocessing import image_preprocessing

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
    Updated = True

    #other variables
    with open('cfg/config.txt','r') as file:
        data = json.load(file)
        no_of_colors = data['no_of_colors'][0]
        #RGB Normalized value
        # color_to_apply = data['color_to_apply'][0]
        #should be greater than 1 for image to be light otherwise for a darker variant it should be less than 1 $$
        grayscale_Threshold = data['Grayscale_threshold'][0] 
    #Pre-process image 
    label,center = image_preprocessing(img, no_of_colors) # Kmeans colored image
    
    #creating a named window for the image we want to show : demo
    cv2.namedWindow('demo')
    #callback on demo
    cv2.setMouseCallback('demo', customize_function)
    while(Updated):
        color_to_apply = input_color()
        while(1):
            #show image on which changes will be made
            cv2.imshow('demo', img)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('r'):
                #reset if r is pressed
                img = clone.copy()
                l=0
                refPt = []
            if key == ord('c'):
                #show output if c is pressed
                img = change_color(img, color_to_apply)
            if key == ord('m'):
                break;
            elif key == ord('q'):
                #quit if q is pressed
                Updated = False
                break

    cv2.destroyAllWindows()

#######################################################################################################
