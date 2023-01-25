a =[]
n = int(input("enter the number elements : "))
for i in range(n):
    a.append(input("enter elements : "))
if not a:
    for i in range(n-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
    print(a)
else:
    print("no elements to sort")