# Line equation

# Classwork Example1

def line_inputs():
    (x1,y1)= input("Enter the first value of the x,y coordinate of the line equation: ")
    (x1)=int(x1)
    (y1)=int(y1)
    (x2,y2)= input("Enter the second value of the x,y coordinate of the line equation: ")
    (x2)=int(x2)
    (y2)=int(y2)
    x= input("Enter the new value of the x coordinate of the line equation: ")
    (x)=int(x)
    return (x,x1,y1,x2,y2)

def line_equation(x,x1,y1,x2,y2):
    y = (((y2-y1)/(x2-x1))*(x-x1)) + y1
    return y

(x,x1,y1,x2,y2)=line_inputs()
y= line_equation(x,x1,y1,x2,y2)
print(y)


def line_equation(x,x1,y1,x2,y2):
    y = (((y2-y1)/(x2-x1))*(x-x1)) + y1
    return y

y= line_equation(x,x1,y1,x2,y2)
print(y)



def line_equation(x,x1,y1,x2,y2):
    y = (((y2-y1)/(x2-x1))*(x-x1)) + y1
    return y

x1=2 
x2=3 
y1=2 
y2=3 
y= line_equation(x,x1,y1,x2,y2)
print(y)


#     Write a unit test for this function before you code the function itself.
#     Add instructor as a collaborator to your repository and create an issue that links to this unit test. Add the instructor as an assignee.
#     Develop the function.
#     If you find that your function has multiple steps that can be broken down into smaller functions, do so, and then write a test for the smaller functions as well.
#     Make sure your function passes your unit tests.
#     Open a second issue that links to the completed function and add instructor as an assignee.

# Additional Work:

#     Develop a function that takes (x1, y1), (x2, y2) and a third point (x3, y3) and returns True if the third point is on the line defined by the first two points. Otherwise, it returns False.
#     Write unit tests that test this function for both True and False results. -->

# receives as parameters two tuples, (x1, y1), (x2, y2), that represent two (x, y) coordinates on a plane,
# receives a parameter, x, that is a new value on the x-coordinate of the above plane,
# returns a value y that is on the line created by the first two points.


# import pytest

# list_of_points=[(1, 2),(2, 3),(3,4),(4,5)]
# @pytest.mark.parametrize("x,expected", 
# list_of_points)
# def test_line_equation(x,expected):
#     answer=line_equation(x)
#     assert answer==expected

# Direct method to print value of y for each value of x

# import numpy as np
# x=np.array([1,2,3,4,5])
# x1=2
# x2=3
# y1=2
# y2=3
# for inputs in x:
#     y =(((y2-y1)/(x2-x1))*(x-x1)) + y2
# print (y[0],y[1],y[2],y[3])