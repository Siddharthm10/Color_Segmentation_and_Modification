def customize_function(event, x, y, flags, params):
    global l,label
    global refPt

    
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
        # cv2.rectangle(s_img, refPt[0], refPt[1], (0, 255, 0), 2)
        # cv2.imshow('demo', s_img)




def change_color(img, color_to_apply):

    #making mask from the provided label
    mask = cv2.inRange(label,l,l)

    #making a grayscale image to save the textures
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    #saving the grayscale image with threshold, to lower the dark areas
    # temp = np.multiply(grayscale_Threshold, cv2.split(gray_img))
    # # HERE WE WERE GETTING BLACK SPOTS ON INCREASING THE THRESHOLD
    gray_img[mask>0] += 90
    temp = np.array(cv2.split(gray_img),dtype=np.uint8)

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
    import json
    import time
    import gzip
    from Utilities.Popup import input_color
    # from Utilities.preprocessing import image_preprocessing

    folderpath = 'images/'
    filename = input("Enter the file you want to open: ")
    filepath = folderpath+filename
    label_file_dir = 'labels/'+filename.split('.')[0]+ '.npy.gz'

    #Reading the image and making a copy with OpenCV : s_img -> Showcased image
    img = cv2.imread(filepath)
    clone = img.copy() #clone for reseting
    # reduced = img.copy() #copy for reduced colors using kmeans

    #initializing Global variables
    l=0
    refPt = []


    #other variables
    with open('cfg/threshold.txt','r') as file:
        data = json.load(file)
        #should be greater than 1 for image to be light otherwise for a darker variant it should be less than 1 $$
        grayscale_Threshold = data['Grayscale_threshold'][0] 
    
    with open('labels/centers.json','r') as file:
        data = json.load(file)
        #Pre-process image 
        center = np.array(data[filename]) 
    
    f=gzip.open(label_file_dir, mode='rb')
    label = np.load(file=f)
    f.close()

    #creating a named window for the image we want to show : demo
    cv2.namedWindow('demo')
    #callback on demo
    cv2.setMouseCallback('demo', customize_function)
    
    while(1):
        #show image on which changes will be made
        cv2.imshow('demo', img)
        cv2.imshow('original', clone)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            #reset if r is pressed
            img = clone.copy()
            l=0
            refPt = []
        if key == ord('c'):
            #show output if c is pressed
            color_to_apply = input_color()
            color = np.zeros((100,100,3), np.uint8)
            color[:] = (color_to_apply[2]*255, color_to_apply[1]*255, color_to_apply[0]*255)
            cv2.imshow("color", color)
            img = change_color(img, color_to_apply)
        elif key == ord('q'):
            #quit if q is pressed
            break

    cv2.destroyAllWindows()

#######################################################################################################
