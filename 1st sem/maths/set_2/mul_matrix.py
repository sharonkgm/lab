matrix1 = [[2,3,4],[1,9,0],[2,4,4]]
matrix2 = [[9,3,1],[8,5,1],[-3,6,8]]
m= [[0,0,0],[0,0,0],[0,0,0]]


for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
           m[i][j] += matrix1[i][k] * matrix2[k][j]

for k in m:
    print(k)
