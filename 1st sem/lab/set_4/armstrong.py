n = int(input("enter the number : "))
sum = 0
temp = n
while temp>0:
    d = temp % 10
    sum += d ** 3
    temp //= 10

if n == sum:
    print(n," is a armstrong number")
else:
    print(n," not a armstrong number")