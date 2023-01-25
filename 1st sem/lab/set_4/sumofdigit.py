n = int(input("enter the number : "))
sum = 0
temp = n
while temp>0:
    d = temp % 10
    sum += d
    temp //= 10
if sum!=0:
    print("sum of digits : ",sum)