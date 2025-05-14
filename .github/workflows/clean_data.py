# Cleaning and handling missing values
import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")

# Check missing values
print("Missing values:\n", data.isnull().sum())

# Clean column names
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")

# Fill NA if needed (though dataset is usually clean)
data.fillna(method='ffill', inplace=True)

# Save cleaned version
data.to_csv("cleaned_data.csv", index=False)
