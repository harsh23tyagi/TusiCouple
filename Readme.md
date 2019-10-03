~ Created by Harsh Tyagi

# Tusi Couple Implementation

### External resources used:

- MatPlotlib python library for generating aof graphs and figures

---

## CODE EXECUTION SUMMARY:

- The below executed code takes in the input of the center points of the outer circle and inner circle
- The code then finds the path of the rgb points as mentioned in the figure on the web portal
- Algo explained below in the algorithm section

---

## FUNCTIONS/METHODS USED:

- create_twocircles(): This method takes in the inputs such as the center of the outer circle, and the y-coordinate for the center of the inner circle
- take_ColorCoordinate(): This method takes in the y-coordinates of the RGB color points, assuming that they are on the diameter chord of the inner circle which is vertically aligned with the diameter of the outer circle
- dis_ColorFromInnerCenter(): This method finds the distance between a center point and the coordinate passed as parameter
- r2_calculation(): This method finds the x-axis length of the ellipse
- ellipseEquationX(): This method is used to find the x coordinates of the path of the ellipse
- ellipseEquationY(): This method is used to find the y coordinates of the path of the ellipse
- findEllipticalPoint2(): This method is used to create a list of the x-coordinates and y-coordinates of the ellipse
- showing_withalldiag(): This method is called by the findEllipticalPoint2() method to plot the circles and the ellipse path of the RGB points in their respective colors
- main(): the main method calling all the other methods and performs the binding and essential tasks for the code

---

Release Notes:

- Before I made this code, i needed to understand how a Tusi Couple was working.
- I deciphered the working by seeing the animated image on the web portal, which was also present on wikipedia page
- Then, i used common ellipse equation and inferential logic to create and plot the following code

ALGORITHM USED:

- The first assumption made in the following code is that, we have to pick a starting point:
  I picked up the starting point as vertically aligned diameter of both the circles over y-axis and the RGB points over it

- We also infer that the movement of the RGB points will create an ellipse, and thus we need to find the x-axis length of the ellipse and y-axis length of the ellipse

- My first method create_twocircles(), asks for the center point of the outer circle, both x and y coordinates. It asks for just the y-coordinate for the inner circle, since they are vertically aligned
- The algorithm, post taking in the center coordinates, takes in the RGB point of coordinates, since our starting instance is vertically aligned circles, again only y-coordinates are asked for the three points
- dis_ColorFromInnerCenter() is then used to calculate the distance of the RGB points from the center to the point, which can be positive(if towards the center of outer circle) or negative(away from the center of outer circle)
- This distance is used to calculate the x-axis length of the ellipse, which is symboled as r2, this method is called three times for the three point
- The algorithm also calculates the y-axis length of the ellipse, which is symboled as r1, this method is called three times for the three point
- The algorithm then calculates the x and y coordinates of the ellipse path using findEllipticalPoint2() methid which uses the ellipseEquationX and ellipseEquationY methods
- The algotithm alos plots the circles with the respective ellipses using the method showing_withalldiag()
- The main function does the binding and calling of the various methods mentioned above

## The inputs used here

Red point: (20,24)
Green point: (20,22)
Blue point: (20,20)

Outer circle :
Center=(20,20)
Radius=20

Inner Circle :
Center=(20,30)
Radius=10
