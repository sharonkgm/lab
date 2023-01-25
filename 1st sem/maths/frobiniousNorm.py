from math import sqrt
n = 2
def frobinious(matrix):
    sumsqrt = 0
    for i in range(n):
        for j in range(n):
            sumsqrt += pow(matrix[i][j], 2)
    r = sqrt(sumsqrt)
    return r
matrix = [[2 ,6],[7 ,3]]
print(frobinious(matrix))

