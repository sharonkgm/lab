#function for string matching
def string_matching(string_arr,substring_arr,i,j,start):
    while i < len(string_arr) and j < len(substring_arr):
        if string_arr[i] == substring_arr[j]:
            i += 1
            j += 1
        else:
            i = start + 1
            start = i
            j = 0
    if j == len(substring_arr):
        print(f"substring found from {start} to {i - 1} ")
        if i != len(string_arr):
            #resetting substring index
            j = 0
            #recursive call of string matching function
            string_matching(string_arr,substring_arr,i,j,i)
                    
    else:
        print("not found")

string = input("enter the string : ")
substring = input("enter the substring to search :")
string_arr = []
substring_arr = []
for i in string :
    string_arr.append(i)

for j in substring:
    substring_arr.append(j)
#calling string matching function
string_matching(string_arr,substring_arr,0,0,0)