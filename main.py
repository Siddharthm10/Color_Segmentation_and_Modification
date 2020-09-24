def customize_function(event, x, y, flags, params):
    global xpos,ypos
    global b,g,r
    global label,l
    global refPt
    if event == cv2.EVENT_RBUTTONDOWN:
        #saving the x, y positions #######temp (to be kept if necessary)
        xpos = x
        ypos = y
        # b,g,r = img[y,x]
        #identifying the label on which the user clicks
        l=label[y,x]

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
        cv2.imshow("image", img)

        

def change_color( s_img, img, color_to_apply):



    #making mask from the provided label
    mask = cv2.inRange(label,2,2)

    #coloring roi with the color to be applied in the mask regions
    s_img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]][mask[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]>0] = color_to_apply

    # if there are two reference points, then crop the region of interest
    # from teh image and display it
    # if len(refPt) == 2:
        # s_img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]] = img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    # else:
        # s_img = img
    cv2.imshow("Result",s_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # return s_img



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
    
    return reduced, label


#######################################################################################################
if __name__ == "__main__":

    #importing important Libraries
    import cv2
    import numpy as np
    import argparse
    import imutils

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
    xpos=ypos=0
    r=g=b=0
    l=0
    refPt = []

    #other variables
    no_of_colors = 3
    color_to_apply = (0,0,0)

    #Pre-process image 
    _,label = image_preprocessing(img, no_of_colors) # Kmeans colored image


    #creating a named window for the image we want to show : demo
    cv2.namedWindow('demo')
    cv2.setMouseCallback('demo', customize_function)
    while(1):
        cv2.imshow('demo', img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            img = clone.copy()
            xpos=r=g=b=ypos=l=0
            refPt = []
        if key == ord('c'):
            change_color(s_img, img, color_to_apply)
        elif key == ord('q'):
            break
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#######################################################################################################
