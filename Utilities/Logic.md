## Logic for final coloring:
- Step 1: Get all the RGB values in the ROI.
- Step 2: Calculate the average of RGB values found.
- Step 3: Substract Each RGB value from the average.
- Step 4: Respectively for that position Apply same variations to the applied image color.


## Logic for predicting the amount of colors:
The problem that we have is getting the different colors classified so that if the user thinks of changing a certain color:
- Step 1: Set four thresholds for R,G,B,Combined(RGB) (If threshold is crossed a new class is defined of that color).
- Step 2: Traverse through the image with the thresholds.
- Step 3: if(d(r)>Rt && d(g)>Gt && d(b)>Bt & (d(r)+d(g)+d(b))>Ct): This position has a different color.(make a new class) {comparision btw consecutive pixels}
- Step 4: Also compare with the already defined color so that the same color doesnt get into a new class. {comparision btw current pixel and defined color classes}


## Another logic for predicting the colors: 
The reason why the hsv logic didnt work was because there were still too much of variation in the color of the images and thus it was hard even for HSV range to cover every other rgb values. I believe the new logic deals with the problems. Working on it:
- Step 1: Use KMeans for the entire image 
- Step 2: Run the entire image through the Kmeans and change the color to be predicted with the prediction.
- Step 3: Make mask using those cluster centers.