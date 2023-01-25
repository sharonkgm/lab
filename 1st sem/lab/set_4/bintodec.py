n = int(input("enter a binary number : "))
base = 1
dec =0
while n!=0:
    rem = n % 10
    dec = dec + rem * base
    n //= 10
    base *= 2
print("decimal format is : ",dec)