# Design and write program to calculate the area of a circle. The user will enter the radius of the circle and the program will print the area.


#Get the radius from the user
rad = input("Enter the radius of a circle:")
#Calculate the area which is: a = Pi * Radius^2
area = 3.14 * ( int(rad) * int(rad) )
areastr = str(area)
print("The area of your circle with the radius of " + str(rad) + "  is " + areastr)
