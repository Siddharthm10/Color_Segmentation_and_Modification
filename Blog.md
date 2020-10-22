
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
While scrolling through the Fashion section on a shopping website, have you ever thought - "I wish I could change this color, and then this dress would look amazing !!"   
I have felt the same :D.

Working in the Image Processing field gives you the power to make this possible. As we started working on it, we came across this concept of Color Segmentation. The idea was to customize/change the colors present in an image. As we began to research, we came across many amazing articles on color segmentation using Neural Networks & OpenCV (a python library written for the sole purpose of taking up Computer Vision challenges).

There were many cool projects like Invisibility Cloak (like the one from the Harry Potter), object detection, Virtual Pen(Used to draw over live webcam), and many others. Our goal was to do product customization where we can change any color present in a T-Shirt, Furniture, or any other product.

