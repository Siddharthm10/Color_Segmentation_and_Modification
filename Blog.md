
# Color_Segmentation_and_Modification:
 ##### The purpose behind the project is to select the colors from an image and modify them with a custom color(user's Choice) within the ROI selected. There can be many applications for this project like fashion customizability, Trying different paints and color combinations for house decor & furniture etc.

### Libraries Used:
- PIL
- OpenCV
- Numpy
- os

### Steps:
##### 1. First step was to detect the RGB colors assosciated with each position in the image.
 - It was easy as the images read by opencv contained numpy arrays (3-D) containing the RGB values.
 - We used a callback function which returned the x,y position of the click and then extracted the respective RGB values which we displayed using cv2.text. (You can find the code for this in Main.py)

##### 2. Second step was to select a ROI (Region Of Interest)
 - We used the mouse callback here as well to get the drag and dropped area by getting the x,y coordinates of both the end points
 - Then we trimmed the original image using the coordinates, worked with that image and placed it back on the original image.

##### 3. Selecting the portion with one color 
 - Initial idea was to get all the traverse through the entire image(PIL used) and setting some threshold for each RGB values and then changing the color.
  - Problems faced here were : Thresholds had to be set mannually for each product & for each color, Also there were some added complication with using OpenCV & PIL together.
 - Then we tried HSV color ranges to make masks for each color.
  - But again due to high variation this wasnt efficient unless provided with the mannual ranges.
 - Now we are trying deep learning networks for color segmentation.



PS : Things to be tried :- 
 - Fill method 
 - KNN New logic 







---
# Color Segmentation & Modification
>While scrolling through the Fashion section on a shopping website, have you ever thought - "I wish I could change this color, and then this dress would look amazing !!"   
>I have felt the same :D.

Working in the Image Processing field gives you the power to make this possible. As we started working on it, we came across this concept of Color Segmentation. The idea was to customize/change the colors present in an image. As we began to research, we came across many amazing articles on color segmentation using Neural Networks & OpenCV (a python library written for the sole purpose of taking up Computer Vision challenges).  

There were many cool projects like *Invisibility Cloak* (like the one from the Harry Potter), *object detection*, *Virtual Pen*(Used to draw over live webcam), and many others that used color detection/segmentation. Our goal was to do product customization where we can change any color present in a T-Shirt, Furniture, or any other product.

Using Neural Networks might have given us a better accuracy but there were other restraints like training/processing time, and lack of training data.
So, we chose to proceed with OpenCV as it's accuracy can be optimised and is faster as compared to the Neural Networks.  
Here I have explained a few approaches that we tried while working on this project.  

## Pick the portion containing a certain color.
Have you ever wondered, How does a computer see an image?
It processes the image as a combination of RGB(Red, Green, and Blue) values varying between 0 to 255. Here when all the three values are 0, we see Black color, and when all the three values are 255, we see white color.
While dealing with real-life pictures, we have to deal with shadows and color gradients, which cause varying RGB values.  
Our initial approach was to traverse through the image and set some thresholds to identify a different color.   
**Cons**: Thresholds had to be set manually for each color in each image. As we want the process to be as autonomous as possible, we rejected this idea.

### HSV Color picker: 
HSV(Hue, Saturation & Value) is a cylindrical color model that remaps the RGB primary colors into dimensions that are easier for humans to understand. With the help of this color space(*link to the article on color spaces*), we can identify and mask portions containing a color.  
**Pros**: Good accuracy, Speed.  
**Cons**: HSV values for masking required precision, which only comes with manual work. And hence, we dropped the idea.  

### KNN Algorithm:
KNN (K Nearest Neighbors), as the name suggests it traverses through all the RGB values and plots them on a coordinate plane. You can read more about KNN [here](https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/).  

**Pros**: 
- Categorizes colors efficiently.
- The only manual input is the number of clusters(or colors in our case).    
  
**Cons**: 
- The processing time for each image is high (about 4 seconds for a 1200x1200 image).

