matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print(matrix)
print(matrix[1][0])
matrix[2][2] = 31
print(matrix)

for rows in matrix:
    for items in rows:
        print(items)
