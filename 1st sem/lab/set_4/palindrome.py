n = int(input("enter the number : "))
temp = n
rev = 0
while n!=0:
    rem = n % 10
    rev = rev * 10 + rem
    n //= 10
if rev == temp:
    print("it is a palindrome")
else:
    print("it is not a palindrome")