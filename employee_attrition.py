import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("employee-attrition.csv")

# Display dataset shape
print("Dataset Shape (Rows, Columns):", df.shape)

# Display first 5 rows
print("\nFirst 5 Rows of Dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()
