# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AaZQMwWkJSk2Ge8Vbs5T1PVs9mxCSLVZ

# Egypt Gold Prices

Is a project to visualize and analyze daily gold prices in Egyptian pounds per gram, leveraging a dataset created to bridge the gap between global market gold prices and the local Egyptian gold market. The dataset was systematically collected from Egypt. Gold price today to record these daily prices.

# Imports Section.
"""

"""Standard library imports."""

import pandas as pd  # Pandas for data manipulation and analysis.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler   # MinMaxScaler from scikit-learn for feature scaling
from sklearn.model_selection import train_test_split  # train_test_split from scikit-learn for splitting the dataset
from sklearn.linear_model import LinearRegression   # LinearRegression from scikit-learn for linear regression modeling
from sklearn.linear_model import Ridge  # Ridge regression is a linear regression model with L2 regularization
from sklearn.model_selection import cross_val_score  # cross_val_score for cross-validation
from sklearn.feature_selection import RFE  # Recursive Feature Elimination (RFE) for feature selection
from sklearn.tree import DecisionTreeRegressor  #  DecisionTreeRegressor from scikit-learn for Decision Tree Regressor modeling
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor  #  RandomForestRegressor from scikit-learn for Random Forest Regressor modeling
from sklearn.ensemble import GradientBoostingRegressor #  GradientBoostingRegressor from scikit-learn for Gradient Boosting Regressor modeling
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import Lasso
from keras.models import load_model
import h5py

"""# Read csv.

"""

# Read the CSV file into a Pandas DataFrame.
# The read_csv function reads the data from the CSV file and stores it in a tabular format.
# You can specify various parameters like delimiter, header, and encoding based on the file's characteristics.


data = pd.read_csv('/content/data/data.csv')

# Display the first few rows of the 'data' DataFrame.
# The head() method is used to show a preview of the data, which is useful for initial exploration.
# By default, it displays the first 5 rows, but you can specify the number of rows by passing an argument.

data.head()

"""# Check For Missing."""

# Calculate the number of missing values in each column of the 'data' DataFrame.

missing = data.isnull().sum()
missing

# Calculate the number of missing values in each column of the 'globall' DataFrame.

# missing = globall.isnull().sum()
# missing

# Perform one-hot encoding on the 'local' DataFrame to convert categorical variables into binary columns.

# local = pd.get_dummies(local)
# local

# Perform one-hot encoding on the 'data' DataFrame to convert categorical variables into binary columns.

data = pd.get_dummies(data)
data

"""# spliting data"""

# Extracting buy prices as labels
# iloc[:, [1, 3, 5, 7, 9, 11]] selects all rows (:) and columns at indices 1, 3, 5, 7, 9, 11

labels = data.iloc[:, [1, 3, 5, 7, 9, 11]]
labels.head()

# Extracting sell prices as features
# iloc[:,[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]] selects all rows (:) and columns at indices 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

features = data.iloc[:, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]]
features.head()

"""# preprocessing"""

# Creating a MinMaxScaler instance
scale = MinMaxScaler()

# Transforming the features using Min-Max scaling
# fit_transform() scales the features to a specified range (default is [0, 1])

features = scale.fit_transform(features)
features

scale2 = MinMaxScaler()

# Transforming the labels using Min-Max scaling
# fit_transform() scales the labels to a specified range (default is [0, 1])

labels = scale2.fit_transform(labels)
labels

# Splitting the dataset into training and testing sets
# features and labels are split into x_train, x_test, y_train, and y_test
# test_size=0.2 indicates that 20% of the data will be used for testing, and 80% for training
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

print(len(features))

print(len(x_train))

print(len(x_test))

# # Number of features
# num_features = X_train.shape[1]

# # Set up positions for bars on the x-axis
# bar_width = 0.35
# index = np.arange(num_features)

# # Plotting bar chart for features
# fig, ax = plt.subplots(figsize=(10, 6))
# rects1 = ax.bar(index, np.mean(X_train, axis=0), bar_width, label='Features', color='blue', alpha=0.7)

# # Customize chart
# ax.set_xlabel('Feature Index')
# ax.set_ylabel('Mean Value')
# ax.set_title('Comparison of Mean Values for Features')
# ax.set_xticks(index)
# ax.set_xticklabels([f'Feature {i+1}' for i in range(num_features)])
# ax.legend()

# plt.show()

"""# LinearRegression

"""

model = LinearRegression()
model.fit(x_train,y_train)

# Evaluating the model's performance on the test set
# model.score(x_test, y_test) computes the coefficient of determination (R²)
# to assess how well the model predicts the target variable y_test based on the features x_test

model.score(x_test,y_test)

"""# Regularization with Ridge Regression

"""

# Create a Ridge regression model with regularization strength (alpha)
ridge_model = Ridge(alpha=0.1)

# Train the model
ridge_model.fit(x_train, y_train)

# Evaluate the model
ridge_score = ridge_model.score(x_test, y_test)
print("Ridge Regression Score:", ridge_score)

"""# Cross-Validation"""

# Perform cross-validation to get a more robust estimate of performance
scores = cross_val_score(LinearRegression(), features, labels, cv=5)
print("Cross-Validation Scores:", scores)

"""# Feature Selection with Recursive Feature Elimination (RFE)"""

# Use RFE for feature selection
model = LinearRegression()
rfe = RFE(model, n_features_to_select=6)  # Adjust the number of features as needed
x_train_rfe = rfe.fit_transform(x_train, y_train)
x_test_rfe = rfe.transform(x_test)

# Train and evaluate the model with selected features
model.fit(x_train_rfe, y_train)
rfe_score = model.score(x_test_rfe, y_test)
print("RFE Score:", rfe_score)

"""# DecisionTreeRegressor

"""

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels,  test_size=0.2, random_state=42)

decision_tree_model = DecisionTreeRegressor(random_state=42)

decision_tree_model.fit(X_train, y_train)

predictions = decision_tree_model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

mse

r2

"""# RandomForestRegressor"""

random_forest_model = RandomForestRegressor(random_state=42)

# Train the model
random_forest_model.fit(X_train, y_train)

# Make predictions on the test set
predictions_rf = random_forest_model.predict(X_test)

# Evaluate the model
mse_rf = mean_squared_error(y_test, predictions_rf)
r2_rf = r2_score(y_test, predictions_rf)

mse_rf

r2_rf

"""# GradientBoostingRegressor"""

# Initialize the Gradient Boosting Regressor
base_model = gradient_boosting_model = GradientBoostingRegressor(random_state=42)

# Create a MultiOutputRegressor with the Gradient Boosting model
multi_output_model = MultiOutputRegressor(base_model)

# Train the model
multi_output_model.fit(X_train, y_train)

# Make predictions on the test set
predictions_multi_output = multi_output_model.predict(X_test)

# Calculate R-squared for each output
r2_multi_output = r2_score(y_test, predictions_multi_output, multioutput='raw_values')

# Express R-squared as a percentage
r2_percentage_multi_output = r2_multi_output * 100

from sklearn.metrics import mean_absolute_error
import numpy as np

# Assuming y_test and predictions_multi_output are NumPy arrays
mae_multi_output = mean_absolute_error(y_test, predictions_multi_output, multioutput='raw_values')

# Calculate MAE as a percentage of the mean of the true values
mae_percentage_multi_output = (mae_multi_output / np.mean(y_test, axis=0)) * 100

r2_multi_output

mae_multi_output

"""# Lasso Regression"""

# Create Lasso regression model with alpha (regularization strength)
lasso_model = Lasso(alpha=0.01)

# Train the Lasso model
lasso_model.fit(X_train, y_train)

# Make predictions on the test set
predictions_lasso = lasso_model.predict(X_test)

# Calculate R-squared and Mean Absolute Error
r2_lasso = r2_score(y_test, predictions_lasso)
mae_lasso = mean_absolute_error(y_test, predictions_lasso)

print("Lasso Regression - R-squared:", r2_lasso)
print("Lasso Regression - MAE:", mae_lasso)

# Plotting the actual vs predicted values
plt.figure(figsize=(10, 6))

for i in range(y_test.shape[1]):
    plt.subplot(2, 3, i + 1)
    plt.scatter(y_test[:, i], predictions_lasso[:, i], color='blue')
    plt.plot([min(y_test[:, i]), max(y_test[:, i])], [min(y_test[:, i]), max(y_test[:, i])], linestyle='--', color='red')
    plt.title(f'Gold Price {i + 1}')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')

plt.tight_layout()
plt.show()

# Number of output variables
num_outputs = y_test.shape[1]

# Plotting scatter plots for each output variable
for i in range(num_outputs):
    plt.scatter(y_test[:, i], predictions_lasso[:, i], label=f'Output {i+1}')

# Add labels and a legend
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Scatter Plot of Actual vs. Predicted Values')
plt.legend()
plt.show()

"""# using the model weights in new data"""

# Create and fit the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Save the coefficients to an HDF5 file
with h5py.File('/content/data/data.h5', 'w') as hf:
    # Create a dataset named 'coefficients' and save the model coefficients
    hf.create_dataset('coefficients', data=linear_model.coef_)

# Later, you can load the coefficients back
with h5py.File('/content/data/data.h5', 'r') as hf:
    # Access the 'coefficients' dataset to get the saved coefficients
    loaded_coefficients = hf['coefficients'][:]