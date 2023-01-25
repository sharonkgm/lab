
r = int(input("enter the number of rows"))
c = int(input("enter the number of columns"))
m = []
for i in range(r):
  a = []
  for j in range(c):
    a.append(input())
  m.append(a)
print("entered matrix :")
for i in range(r):
    for j in range(c):
      print(m[i][j], end = " ")
    print()

