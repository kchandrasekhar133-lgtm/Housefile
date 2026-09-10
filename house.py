import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset  
df = pd.read_csv("house_data.csv")

# Select required columns
columns = [
    "bedrooms",
    "bathrooms",
    "floors",
    "yr_built",
    "price"
]

df = df[columns]

# Input features
X = df[["bedrooms", "bathrooms", "floors", "yr_built"]]

# Target
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Create model
lr = LinearRegression()

# Train model
lr.fit(X_train, y_train)

# Save NEW model
with open("model.pkl", "wb") as file:
    pickle.dump(lr, file)

print("Model trained successfully!")
print("New model.pkl created successfully.")
print("Model score:", lr.score(X_test, y_test))

