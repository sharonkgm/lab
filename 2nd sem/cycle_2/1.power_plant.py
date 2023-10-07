# Build a linear regression model on the given power plant dataset. Create the 
# training and testing set. Make predictions of the datapoints in the test set.
# Evaluate the model using appropriate performance matrix.



# pip install openpyxl


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset 
data = pd.read_excel(r'2nd sem\cycle_2\dataset\Power Plant.xlsx')

# Assuming your dataset has columns 'AT', 'V', 'AP', 'RH', and 'PE' (where 'Y' is the target variable)

# Split the data into features (X) and the target variable (Y)
X = data[['AT', 'V', 'AP', 'RH']]
Y = data['PE']

# Split the dataset into training and testing sets (e.g., 80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions on the test set
Y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(Y_test, Y_pred)

# Calculate R-squared (R2)
r2 = r2_score(Y_test, Y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")
