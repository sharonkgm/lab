

def bs(sorted_array, l, h, element):
    if h >= l:

        m = (h + l) //2
        if sorted_array[m] == element:
            print(f"\nfound at position {m}:")
        elif sorted_array[m] > element:
            return bs(sorted_array, l, m-1, element)
        elif sorted_array[m] < element:
            return bs(sorted_array, m + 1, h, element)
        else:
            print("not found")

n=int(input("Number of elements in the array :"))
array =[]
print("enter the array elements :")
for k in range(0,n):
    l = int(input())
    array.append(l)
sorted_array = sorted(array)
print("sorted array :\n")
print(sorted_array)
element = int(input("enter the element to search :"))
result = bs(sorted_array, 0, n-1,element)
print(result)










