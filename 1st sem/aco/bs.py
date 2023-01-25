

def bs(n2, l, h, b):
    if h >= l:

        m = (h + l) //2
        if n2[m] == b:
            return m
        elif n2[m] > b:
            return bs(n2, l, m-1, b)
        elif n2[m] < b:
            return bs(n2, m + 1, h, b)
        else:
            print("not found")

a=int(input("Number of elements in the array :"))
n=list(map(int, input("elements of array :").strip().split()))
n2 = sorted(n)
print(n2)
b = int(input("enter the element to search :"))
r = bs(n2, 0, a-1, b)
print(r)










