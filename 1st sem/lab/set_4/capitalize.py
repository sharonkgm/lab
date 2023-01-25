s = str(input("enter a string :  "))
l = len(s)
s = s[0:1].upper() + s[1:l-1] + s[l-1:l].upper()
print(s)