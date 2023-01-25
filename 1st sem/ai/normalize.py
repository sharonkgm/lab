from sklearn import preprocessing
import pandas as pd
import numpy as np

def normalize(column1):
    r = sorted(column1)
    l = len(column1)
    min = r[0]
    max = l-1
    for i in range(0,l):
        nm = ((column1[i] - min)/(max - min))
        print(nm)



dataset = pd.read_csv("sample4.csv")
column1 = dataset["length"]
column2 = dataset["no"]
normalize(column1)


