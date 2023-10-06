#Convert Text Features using one hot Encoding


import pandas as pd


#pip install pandas

data = {'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue'],
        'Size': ['Small', 'Large', 'Medium', 'Medium', 'Small']}

df = pd.DataFrame(data)

encoded_df = pd.get_dummies(df, columns=['Color', 'Size'])

print(encoded_df)
