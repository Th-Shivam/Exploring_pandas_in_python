import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import random as rn

# Load dataset
data = pd.read_csv('winequality-red.csv', sep=';')

# Print dataset columns
print(data.columns)

# Define features and binarize target variable
X = data[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides"]]
Y = (data["quality"] >= 5).astype(int)  # Binarize quality: >=5 -> 1, <5 -> 0

# Split the dataset into training and testing sets
rn.seed(1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=1)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Make predictions
Y_pred = model.predict(X_test)

# Print accuracy score
print(f"Accuracy: {accuracy_score(Y_test, Y_pred)}")
