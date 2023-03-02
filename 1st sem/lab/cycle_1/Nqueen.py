def check_attack(i, j):
    #checking column and row for attack
    for k in range(0,N):
        if matrix[i][k]==1 or matrix[k][j]==1:
            return True
    #checking diagonal for attack
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if matrix[k][l]==1:
                    return True
    return False


def queen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(check_attack(i,j))) and (matrix[i][j]!=1):
                matrix[i][j] = 1
                #backtracking
                if queen(n-1)==True:
                    return True
                matrix[i][j] = 0

    return False

N = int(input("enter the number of queen :"))
matrix = [[0]*N for _ in range(N)]
print(f"\nsolutio of placing {N} queens without attack :\n")
queen(N)
for i in matrix:
    print(i)
