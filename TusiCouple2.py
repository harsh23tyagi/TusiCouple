
# coding: utf-8

# In[71]:


'''

~Created by Harsh Tyagi~

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
It is highly recommended you read these release notes
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

~External resources used:
~MatPlotlib python library for generating aof graphs and figures
~
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CODE EXECUTION SUMMARY:

- The below executed code takes in the input of the center points of the outer circle and inner circle
- The code then finds the path of the rgb points as mentioned in the figure on the web portal
- Algo explained below in the algorithm section
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
FUNCTIONS/METHODS USED:

- create_twocircles(): This method takes in the inputs such as the center of the outer circle, and the y-coordinate for the center of the inner circle
- take_ColorCoordinate(): This method takes in the y-coordinates of the RGB color points, assuming that they are on the diameter chord of the inner circle which is vertically aligned with the diameter of the outer circle
- dis_ColorFromInnerCenter(): This method finds the distance between a center point and the coordinate passed as parameter
- r2_calculation(): This method finds the x-axis length of the ellipse
- ellipseEquationX(): This method is used to find the x coordinates of the path of the ellipse
- ellipseEquationY(): This method is used to find the y coordinates of the path of the ellipse
- findEllipticalPoint2(): This method is used to create a list of the x-coordinates and y-coordinates of the ellipse
- showing_withalldiag(): This method is called by the findEllipticalPoint2() method to plot the circles and the ellipse path of the RGB points in their respective colors
- main(): the main method calling all the other methods and performs the binding and essential tasks for the code
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

-The inputs used here
Red point: (20,24)
Green point: (20,22)
Blue point: (20,20)

Outer circle :
Center=(20,20)
Radius=20

Inner Circle :
Center=(20,30)
Radius=10


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Thanks for giving me the opportunity for this challenge, I hope i make it through


'''



import matplotlib.pyplot as plt
import math
radius1=0
radius2=0
yred=0
yblue=0
ygreen=0
centerx=0
centery=0
centerxS=0
centeryS=0

def create_twocircles():
    #Taking in the inputs for outer circle and calculating inputs for the inner circle 
    #we are assuming that the inner circle's diameter coincides with the diameter of the outer circle and is arranged vertically as a starting point
       
    global radius1, radius2, centerx, centery, centerxS, centeryS
    
    print("Enter the radius of the inner circle (Only Integer accepted)")
    radius1 = int(input())
    print("Enter the x coordinate of the center for the outer circle (in integers)")
    centerx = int(input())
    print("Enter the y coordinate of the center for the outer circle (in integers)")
    centery = int(input())


    radius2 = (int)(radius1/2)

    print(radius2)

    centerxS = centerx
    centeryS = centery+radius2

    print("X coordinate of inner circle: "+(str)(centerxS))
    print("Y coordinate of inner circle: "+(str)(centeryS))


def take_ColorCoordinate(color, cxS, cyS, radius):
    print("Give y coordinate for color "+color)
    temp = (int)(input())
    if((temp>(centeryS+radius)) or (temp < (centeryS-radius))):
        print("Invalid Y Coordinate")
        return 0
    return temp



def dis_ColorFromInnerCenter(center, coordinate ):
    distance = center - coordinate
    return distance

def r2_calculation(distanceInner, radius2, r1):
    if(distanceInner == 0):
        r2= radius2
    else:
        r2= (radius2+ distanceInner)
    return r2
        
def ellipseEquationX(centerx, degrees, r2_rad):
    newX_coordinate = centerx + r2_rad*(math.cos(math.radians(degrees)))
    return newX_coordinate

def ellipseEquationY(centery, degrees, r1_rad):
    newY_coordinate = centery + r1_rad*(math.sin(math.radians(degrees)))
    return newY_coordinate


def findEllipticalPoint2(centerx, centery, cxs, cys, rad1, rad2,color1, r1val, r2val):
    print("\n")
    print("List of Coordinates for color "+color1)
    list_xCoordinate = []
    list_yCoordinate = []
    for i in range(0,375,15):
        list_xCoordinate.append(ellipseEquationX(centerx, i, r2val))
        
    for j in range(0,375,15):
        list_yCoordinate.append(ellipseEquationY(centery,j, r1val))
    print(list_xCoordinate)
    print(list_yCoordinate)
    showing_withalldiag(centerx,centery,cxs,cys,rad1,rad2,list_xCoordinate,list_yCoordinate,color1)
    
    
def showing_withalldiag(centerx, centery, cxs,cys, rad1, rad2, list1, list2, colo):
    fig=plt.figure(1)
    plt.axis([0,50,0,50])
    ax=fig.add_subplot(1,1,1)
    circ=plt.Circle((centerx,centery), radius=rad1, color='g', fill=False)
    circ2=plt.Circle((cxs,cys),radius=rad2,color='b',fill=False)
    plt.plot(list1,list2, color = colo)
    ax.add_patch(circ)
    ax.add_patch(circ2)
    
    
    
    plt.show()
# main function for calling all the other functions
def main():
    global radius1, radius2, centerx, centery, centerxS, centeryS, yRed, yGreen, yBlue
    
    create_twocircles()
    
    yred = take_ColorCoordinate('Red', centerxS, centeryS, radius2)
    if (yred==0):
        print('Invalid Color Coordinate Red')
    ygreen = take_ColorCoordinate('Green', centerxS, centeryS, radius2)
    if (ygreen==0):
        print('Invalid Color Coordinate Green')
    yblue = take_ColorCoordinate('Blue', centerxS, centeryS, radius2)
    if (yblue==0):
        print('Invalid Color Coordinate Blue')
    
    rDist_y = dis_ColorFromInnerCenter(centeryS, yred)
    gDist_y = dis_ColorFromInnerCenter(centeryS, ygreen)
    bDist_y = dis_ColorFromInnerCenter(centeryS, yblue)
    
    #distance from the center of outer circle, which is also the center of the ellipse path formed 
    #r1 of the ellipse path formed by the rotation of the rgb points on the chord of the inner circle
    
    r1_red = yred - centery
    r1_green = ygreen - centery
    r1_blue = yblue - centery
    
    #distance from the center of the outer circle, which is also the center of the ellipse path formed
    #r2 of the ellipse path formed by the rotation of the rgb points on the chord of the inner circle
    r2_red = r2_calculation(rDist_y, radius2, rDist_y)
    r2_green = r2_calculation(gDist_y, radius2, gDist_y)
    r2_blue = r2_calculation(bDist_y, radius2, bDist_y)
    #since r2 is for x axis it will be used to find x coordinates
    #r1 will be used to find y coordinates
    # we will use ellipse coordinate equation
    #centerx, centery, cxs, cys, rad1, rad2,color1, r1val, r2val):
    findEllipticalPoint2(centerx, centery, centerxS, centeryS, radius1, radius2, 'Red',r1_red, r2_red)
    findEllipticalPoint2(centerx, centery, centerxS, centeryS, radius1, radius2,'Green', r1_green,r2_green)
    findEllipticalPoint2(centerx, centery, centerxS, centeryS, radius1, radius2,'Blue',r1_blue,r2_blue)
    

def check():
    #print(ellipseEquationY(20,90,12))
    showing_withalldiag(20,20,20,30,20,10)
    
if __name__ == "__main__":
    main()
    #check()

