import pandas as pd

df = pd.read_csv('ct1.csv')
df['pass'].replace(['yes', 'no'], [0, 1], inplace=True)
print(df)