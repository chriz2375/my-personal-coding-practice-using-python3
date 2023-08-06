"""
    Calculate the diagonal difference of  a given matrix 
    and return the difference with absolute value
"""

def diagonal_absolute_difference(matrix):
    # Calculate the size of the square matrix (assuming it is square)
    n = len(matrix)

    # Initialize the sums of the diagonals to zero
    left_to_right_sum = 0
    right_to_left_sum = 0

    # Iterate through the matrix to calculate the sums of the diagonals
    for i in range(n):
        left_to_right_sum += matrix[i][i]
        right_to_left_sum += matrix[i][n - i - 1]

    # Calculate the absolute difference between the sums
    absolute_difference = abs(left_to_right_sum - right_to_left_sum)

    return absolute_difference

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

result = diagonal_absolute_difference(matrix)
print(result)  # Output: 2
