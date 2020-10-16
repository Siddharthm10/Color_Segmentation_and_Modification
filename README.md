# Custom Color Product
### Aim:
- The aim of this project is to provide an easy interface to the user for customizability of the product.

### Execution Steps:
1. Execute the command line.
2. Enter the image name.
3. Right-Click on the color you want to change.
4. Press 'c' and choose the color to apply the changes.
5. Press 'r' to reset the image.
6. Press 'q' to quit the application.

### Pre-requisite libraries for code implementation
- Numpy
- OpenCV
- ArgParse
- Json


### Input image format:
The input image should be clicked or choosed accordingly for best results.
- The backgroung should not have any constituent colors of the product(so that the color recognition does its job with better accuracy).

### Specifications:
- Run Time: 0.2 seconds

### Command line:
```
    $python main.py

    #and then enter the filename.
```
### Config 
- Config file consists of :
  - Number of colors
  - Grayscale threshold(>1)
  - Color to apply
  
### File Paths:
- images: Example images.
- cfg: Customizable config variables.
- labels: Contains labels and centers related to the images.
- reference: Codes used for reference.
- source: Code.  
- Utilities: Codes that the main function is using.

### Code Flow:
#### Step 1) Classify the colors present in an image
- To classify the colors present we used K-Nearest Neighbours.
- In this the whole image is traversed and all the colors are seperated into different classes.
- The user has to provide with the no of different centers to classify.(Basically the no. of colors has to be given as an input by the user)
- It can be done via the cfg file.

#### Step 2) Get input via mouse clicks 
- Mouse Callback functions are used for this purpose in opencv.
- Read the label and centers created by knn.
- And the mask is made with the label on which the user clicks.

#### Step 3) Color the Specified portion
- This has to be done while keeping the textures of the image.
- Firstly the image is converted to grayscale and the textures are read.
- Then the color is applied to the masked portion.

### Features to be developed:
- UI for selecting the image to work on.
- Addition of new image to the database easier.
- Selective freedom for the user. {Some areas should not be available for customization}.(depends on the requirement of the company)
- Background and skin optimization.
- 