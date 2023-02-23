N = int(input("enter the number of queen"))
m = [[0]*N for _ in range(N)]

def is_attack(i, j):
    
    for k in range(0,N):
        if m[i][k]==1 or m[k][j]==1:
            return True
   
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if m[k][l]==1:
                    return True
    return False


def queen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(is_attack(i,j))) and (m[i][j]!=1):
                m[i][j] = 1
                if queen(n-1)==True:
                    return True
                m[i][j] = 0

    return False


queen(N)
for i in m:
    print(i)
