"""
A list is traditionally created using square brackets. 
But with a list comprehension, these brackets contain an expression followed by a 
for clause and then if clauses, when necessary. Evaluating the given expression in the 
context of these for and if clauses produces a list.
"""

old_list = [1,2,3,-1,-56]
new_list = [x**2 for x in old_list if x >0]
print(new_list)