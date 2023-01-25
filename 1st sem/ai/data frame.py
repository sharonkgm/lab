import pandas as pd

sr = {'rollno': [1,2,3,4,5], 'name': ["akshay","roshan","anu","sam","anjali"],
      'sub1': [90,78,88,80,70], 'sub2': [94,85,80,90,89],
      'sub3': [88,70,83,91,79], 'sub4': [84,77,80,69,86],
      'sub5': [95,90,89,96,76]}
df = pd.DataFrame(sr)
print(df)
print("name   ","mark")
for i in range(1,6):
      m = f'sub{i}'
      nm = df['name'].loc[df[m].idxmax()]
      mk = df[m].max()
      print(nm,mk)
