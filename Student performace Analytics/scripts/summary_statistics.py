# Summary statistics and insights
import pandas as pd

data = pd.read_csv("engineered_data.csv")

# Overall description
print(data.describe())

# Value counts for categorical data
print("Gender count:\n", data['gender'].value_counts())
print("Grade distribution:\n", data['grade'].value_counts())
