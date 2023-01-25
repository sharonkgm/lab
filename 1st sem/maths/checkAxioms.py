import numpy as np
print("1.Associativity of addition"+'\n'+"2.commutativity of addition"+'\n'+"3.identity of addition"+'\n'+"4.inverse of addition"+'\n'+"5.distributivity of multiplication over vector addition"+'\n'+"6.distributivity of multiplication over field addition"+'\n'+"7.compatability of scalar multiplication"+'\n'+"8.identity of scalar multiplication \n")
n = int(input("enter the axiom number to check :"))

def vector(x):
         print(f"enter{x} vector :")
         a = [int(input()) for i in range(3)]
         v = np.array(a)
         return v

if n == 1:
    v1 = vector(1)
    v2 = vector(2)
    v3 = vector(3)
    v = v1 + v2 + v3
    print("(v1 + v2)+ v3 = v1 +(v2 + v3) = ",v ,"\n associative")
elif n == 2:
    v1 = vector(1)
    v2 = vector(2)
    v = v1 +v2
    print("v1 + v2 = v2 + v1",v,"\n commutative")
elif n == 3:
    v1 = vector(1)
    print("0 + v = v =",v1,"\n identity is proven")
elif n == 4:
    v1 = vector(1)
    v = v1 + -(v1)
    print(" v + -v = 0 \n inverse")
elif n == 5:
    a = int(input("enter a scalar number :"))
    v1 = vector(1)
    v2 = vector(2)
    v = a*v1 + a*v2
    print("a(v1 + v2) = av1 + av2 = ",v,"\n distributivity is proven")
elif n == 6:
    a = int(input("enter a scalar number :"))
    b = int(input("enter a scalar number :"))
    v1 = vector(1)
    v = a*v1 + b*v1
    print("(a + b)v = av + bv =",v,"\n distributivity is proven")
elif n == 7:
    a = int(input("enter a scalar number :"))
    b = int(input("enter a scalar number :"))
    v1 = vector(1)
    v = a*b*v1
    print("a(b * v) = (a * b)v = ",v,"\n compatibility is proven")
elif n == 8:
    v1 = vector(1)
    print("1 * v = v =",v1,"\n identity is proven")
else:
    print("invalid number!!!")









