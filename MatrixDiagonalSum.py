# Problem Statement: Given a square grid of numbers (a 2D list/matrix), calculate the sum of the numbers on its primary diagonal (from the top-left to the bottom-right).

def diagonal_sum(matrix):
    total = 0
    n = len(matrix)

    for i in range(n):
        total+=matrix[i][i]

    return total

grid = [
    [10,20,30],
    [23,34,45],
    [11,22,33]
]

print("Sum of diagonal is: ", diagonal_sum(grid))