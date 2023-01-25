matrix = [[2, 2, 1], [3, 4, 8],[12, 4, 0]]
r = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix)):
   for j in range(len(matrix[0])):
       r[j][i] = matrix[i][j]