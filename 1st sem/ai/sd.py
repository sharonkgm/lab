import pandas as pd
import math

dataset = pd.read_csv("sample4.csv")
mpg = dataset["length"]
mpg1 = dataset["no"]
sum = 0
l = len(mpg)
for i in range(0,l):
    sum = mpg[i] + sum
mean = sum/l
s = 0
for i in range(0,l):
    s += ((mpg[i] - mean) ** 2)
r = math.sqrt(s)
sd = r/(l-1)
print(sd)

