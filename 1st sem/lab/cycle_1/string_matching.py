string = input("enter the string : ")
substring = input("enter the substring to search :")
string_arr = []
substring_arr = []
for i in string :
    string_arr.append(i)

for j in substring:
    substring_arr.append(j)

stringIndex = 0
substringIndex = 0
start = stringIndex
while substringIndex < len(substring_arr) and stringIndex < len(string_arr):
    if string_arr[stringIndex] == substring_arr[substringIndex]:
        stringIndex += 1
        substringIndex += 1
    else:
        stringIndex = start + 1
        start = stringIndex
        substringIndex = 0
if substringIndex == len(substring_arr):
    print(f"substring found from {start} to {stringIndex - 1} ")
else:
    print("not found")