import pandas as pd

def minimum(column1):
    min = 9999
    for i in column1:
        if column1[i] < min:
            min = column1[i]
    return min

def maximum(column1):
    max = -9999
    for i in column1:
        if column1[i] > max:
            max = column1[i]
    return max


def mean(column1):
    sum = 0
    for i in range(0,len(column1)):
        sum += column1[i]
    mn = sum/len(column1)
    return mn

dataset = pd.read_csv("sample4.csv")
column1 = dataset["length"]
column2 = dataset["no"]

print(minimum(column1))
print(maximum(column1))
print(mean(column1))





