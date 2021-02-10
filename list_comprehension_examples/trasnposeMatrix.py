"""
transponse two arrays, making a couple using the values in the same position of both arrays 
A = [1, 2, 3, 4] B = [4, 5, 6, 8]
matrix = [A, B]
Trasnposed = [[1, 4], [2, 5], [3, 6], [4, 8]]
"""

transposed = []
A = [1, 2, 3, 4]
B = [4, 5, 6, 8]
matrix = [A, B]

for i in range(len(A)):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(f"transposed with loops: {transposed}")


"""
same implementation with list comprehensions
"""
transpose_list = [[row[i] for row in matrix] for i in range(len(A))]
print (f"transposed with list comprehension: {transpose_list}")