# Notes about python

* [Object](#Object)
* [List](#List)
* [Set](#Set)
* [Stack](#Stack)
* [Queue](#Queue)
* [Typle](#Tuple)

# Object

```
# Base or Super class
class Person(object):
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False

# Employee subclass
class Employee(Person):
    def __init__(self, name, eid):

        ''' In Python 3.0+, "super().__init__(name)"
            also works''' 
        super(Employee, self).__init__(name)
        self.empID = eid
        
    def isEmployee(self):
        return True
        
    def getID(self):
        return self.empID

# Driver code
emp = Employee("Geek1", "E101") 
print(emp.getName(), emp.isEmployee(), emp.getID())
```

# Lambda

Labda is an anonymous functtions usually very short. 
```
def cube(y):
    return y*y*y;

g = lambda x: x*x*x
print(g(7))

print(cube(5))
```

# List
### Insert elements

List: dynamic sized arrays that contains duplicate values even of different data-types.
append(): add a single element at the end of the list
insert(): add element in specific index. ```list_name.insert(index, value_to_add)```
extend():  add multiple elements passing a list as argument ```list_number.extend([1,2,3])```

### Multidimensional lists
Multidimensional list: 
```
myList = [['Davide', 'Pollicino'], [1,2,3]]
print(List[0][1]) # Will print out Davide 
```
### Remove elements from the list
```
# Raise an error if the element that does exists
list_name.remove(element_to_remove)

## Remove multiple element at the same time from index 0 to 4
for i in range(1, 5):
    list_name.remove(i)

# Remove last eleemnt 
list_name.pop()
```

### Slicing a list

Slicing is one of the wayus used to print a list, using the ":" operator. 
Print list in reverse order [::-1]
From begin to end [:]
```
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)
```

### Get index of first occurency of an element 

```
list_numbers = [1,2,3, 3,4]
# Raise an error because 5 does not exists
print(list_numbers.index(5))
# Will print 2
pritn(list_numbers.index(3))
```

sum : Ritorns the sum of the elements in the list```print(sum(my_list))```
count : Ritorns the occurency of an element in the list ```print(my_list.count(element))```
# Set

Unrdered and unindexed collection. If you insert multiple times in the set it will not
raise an error but once you print the content of the set you will see just isngle occurrencies of the elements
```
# Creat a set
my_set = {1,2,3,1}
# Convert list in Set
my_Set = set(list_name[1,3,4])

# Add a new element
my_Set.add(6)
# Add multiple elements 
my_Set.update([8,9])
```

###  Union of two list
```
def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list
```
### Union of three or more list
```
def Union(lst1, lst2, lst3):
    final_list = list(set().union(lst1, lst2, lst3))
    return final_list
```

### Intersaction of two list

With an intersaction operation we get all the element that are common between 
the two lists.
```
def get_intersaction(list1, list2):
    intersaction = [value for value in list1 if value in list2]
    return intersaction
```

```
def get_intersaction(list1, list2)
    return set(list1).intersaction(list2)
```

# Stack

In python we can implement a stack just usign a list, with its built in functions append() and pop().

# Queue
```
from collections import deque
my_queue = queue(["Davide", "Pino", "Alessio"])
print(my_queue)
my_queue.append("Antonino")
print(my_queue)
print(my_queue.pop())
print(my_queue)
```

# Tuple

Immutable that datastruct (we cannot add / remove) any elemet.
```
# Create an empty list
my_tuple = ()
```