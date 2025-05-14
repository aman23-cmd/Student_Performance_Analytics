# Identifying and sourcing relevant datasets
import pandas as pd

# Load the dataset
data = pd.read_csv("StudentsPerformance.csv")

# Show basic info
print(data.head())
print(data.columns)
