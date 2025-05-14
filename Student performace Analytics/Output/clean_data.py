import pandas as pd

# Load raw dataset
data = pd.read_csv("data/StudentsPerformance.csv")

# Basic cleaning: drop NA, strip whitespace, normalize text
data.dropna(inplace=True)
data.columns = data.columns.str.strip()
data["gender"] = data["gender"].str.lower()
data["lunch"] = data["lunch"].str.lower()

# Save cleaned data
data.to_csv("output/cleaned_data.csv", index=False)
print("✅ Cleaned data saved as 'cleaned_data.csv'")
