#function for insertion sort
def insertionsort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while key<=array[j] and j>=0:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key


n =int(input("enter the number of elements :"))
array = []
print("enter the array to sort :")
for k in range(0,n):
    l = int(input())
    array.append(l)
print("enterd array :")
print(array)
insertionsort(array)
print("sorted array :")
print(array)
