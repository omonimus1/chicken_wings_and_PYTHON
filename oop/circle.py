"""
Author: Davide Pollicino 
Date: 11/05/2020
Summary: Providing in Input the radius of a circle, provide area, perimeter and diameter.
    -- You must to use OOP
"""
# (object): is the new style base classes. It will inheritate from object
class Circle(object):
    pi = 3.142
    # __init__ : is a class initializer. When we create an object 
    # this is the method that we call first
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pow(self.radius, 2) * self.pi

    def perimeter(self):
        return 2 * self.pi * self.radius

    def diameter(self):
        return 2 * self.radius


if __name__ == '__main__':
    circle1 = Circle(2.50)
    print('area: ' + str(circle1.area()))
    print('Perimeter: ' + str(circle1.perimeter()))
    print('Diameter: ' + str(circle1.diameter()))