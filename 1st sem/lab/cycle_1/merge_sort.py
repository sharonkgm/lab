def mergesort(array):
    if len(array)>1:
        mid = len(array)//2
        sub_array1 = array[:mid]
        sub_array2 = array[mid:]

        mergesort(sub_array1)
        mergesort(sub_array2)

        i=j=k=0
        while i<len(sub_array1) and j<len(sub_array2):
            if sub_array1[i]<sub_array2[j]:
                array[k] = sub_array1[i]
                i += 1
            else:
                array[k] = sub_array2[j]
                j += 1
        while i<len(sub_array1):
            array[k] = sub_array1[i]
            i += 1
            k += 1
        while j<len(sub_array2):
            array[k] = sub_array2[j]
            j += 1
            k += 1

n =int(input("enter the number of elements :"))
array = []
print("enter the array to sort :")
for k in range(0,n):
    l = int(input())
    array.append(l)
print("enterd array :")
print(array)
mergesort(array)
print("sorted array :")
print(array)