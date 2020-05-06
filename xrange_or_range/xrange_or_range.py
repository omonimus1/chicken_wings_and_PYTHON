#!/usr/local/bin/python
"""
Author: Davide Pollicino
Date: 06/05/2020

range() – This returns a range object (a type of iterable).
xrange() – This function returns the generator object that can be used to 
display numbers only by looping. Only particular range is displayed on demand 
and hence called “lazy evaluation“
"""

# initializing a with range() 
a = list(range(1,10000)) 
  
# initializing a with xrange() 
"""
In python 3 there is not anymore range adn xrange. 
If we want a range object of type iterable we now need to do for example list(range(1, 1000))
"""
try:
    # Python 2
    x = xrange(1,10000)
except NameError:
    xrange = range
    x = xrange(1,10000)


# testing the type of a 
print ("The return type of range() is : ") 
print (type(a)) 
# print (a) -> Output: ALl the numbers between 1 and 1000

# testing the type of x 
print ("The return type of xrange() is : ") 
print (type(x)) 
print (x)  # Output: range(1,1000)