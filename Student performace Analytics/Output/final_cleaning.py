import pandas as pd

# Load engineered data
data = pd.read_csv("output/engineered_data.csv")

# Final cleaning: rename columns, drop duplicates
data.columns = data.columns.str.replace(" ", "_")
data.drop_duplicates(inplace=True)

# Save final cleaned data
data.to_csv("output/final_cleaned_data.csv", index=False)
print("✅ Final cleaned data saved as 'final_cleaned_data.csv'")
