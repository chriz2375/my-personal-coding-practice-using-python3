"""
 List comprehension is a concise and elegant way to create lists in Python. 
It allows you to create a new list by applying an expression to each item
in an iterable (e.g., list, tuple, string, etc.) and optionally including a filtering condition. 
The general syntax of a list comprehension is as follows:

new_list = [expression for item in iterable if condition]

"""

# numbers = [x for x in range(100) if x % 2 == 0]
# print(numbers)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # declaring the matrix

# implementing list comprehension without any condition
elem_matrix = [x**2 for row in matrix for x in row]
print(elem_matrix)
elem_matrix1 = [] 

# using manual loop to iterate each element of the matrix
for row in matrix:
    for ele in row:
        elem_matrix1.append(ele**2)
print(elem_matrix1)

# using list comprehension with a condition (display only the odd elements)
elem_matrix = [x**2 for row in matrix for x in row if x**2 % 2 != 0]
print(elem_matrix)
