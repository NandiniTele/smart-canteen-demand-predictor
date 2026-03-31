import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Encode categorical columns
encoders = {}

for column in ["day","meal","item","weather","event"]:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    encoders[column] = le

# Features
X = data[["day","meal","item","weather","event"]]

# Target
y = data["demand"]

# Train model
model = RandomForestRegressor()
model.fit(X,y)

# Save model
pickle.dump(model,open("model.pkl","wb"))
pickle.dump(encoders,open("encoders.pkl","wb"))

print("Model trained successfully")