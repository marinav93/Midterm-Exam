"""
===================   TASK 1   ====================
* Name: Area Of Circle
*
* Write a function `area_of_circle` that will
* return area enclosed by a circle of radius `r`.
* Consider that only float value for radius will
* be passed. Negative values should be considered
* as typo and function should ignore sign of a
* number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here



def main():
    from math import pi

    r = float(input("Input the radius of the circle : "))
    print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))



main()
