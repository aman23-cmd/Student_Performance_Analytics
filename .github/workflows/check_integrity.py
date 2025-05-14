# Ensuring data integrity and consistency
import pandas as pd

data = pd.read_csv("engineered_data.csv")

# Check duplicates
print("Duplicates:", data.duplicated().sum())

# Check data types
print("Data types:\n", data.dtypes)

# Ensure scores are in 0-100 range
print("Score range check:")
print(data[['math_score', 'reading_score', 'writing_score']].describe())
