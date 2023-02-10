matrix = [[12,7],
    [4 ,5],
    [3 ,8]]

r = [[0,0,0],
         [0,0,0]]
print("given matrix :")
for x in matrix:
    print(x)
for i in range(len(matrix)):
   for j in range(len(matrix[0])):
       r[j][i] = matrix[i][j]
print("\ntranspose of given matrix is :")
for k in r:
   print(k)
