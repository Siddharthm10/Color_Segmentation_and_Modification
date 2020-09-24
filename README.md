
# Color_Segmentation_and_Modification:
 ##### The purpose behind the project is to select the colors from an image and modify them with a custom color(user's Choice) within the ROI selected. There can be many applications for this project like fashion customizability, Trying different paints and color combinations for house decor & furniture etc.
 
### Libraries Used:
- PIL
- OpenCV
- Numpy
- os

### Steps:
##### 1. First step was to detect the RGB colors associated with each position in the image.
 - It was easy as the images read by opencv contained numpy arrays (3-D) containing the RGB values.
 - We used a callback function which returned the x,y position of the click and then extracted the respective RGB values which we displayed using cv2.text. (You can find the code for this in Main.py)
 
##### 2. Second step was to select a ROI (Region Of Interest)
 - We used the mouse callback here as well to get the drag and dropped area by getting the x,y coordinates of both the end points
 - Then we trimmed the original image using the coordinates, worked with that image and placed it back on the original image.
 
##### 3. Selecting the portion with one color 
 - Initial idea was to get all the traverse through the entire image(PIL used) and setting some threshold for each RGB values and then changing the color.
  - Problems faced here were : Thresholds had to be set manually for each product & for each color, Also there were some added complication with using OpenCV & PIL together.
 - Then we tried HSV color ranges to make masks for each color.
  - But again due to high variation this wasn't efficient unless provided with the manual ranges.
 - Now we are trying deep learning networks for color segmentation.
 
 
 
PS : Things to be tried :- 
 - Fill method 
 - KNN New logic 
