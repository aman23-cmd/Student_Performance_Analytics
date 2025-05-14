import pandas as pd

# Load final cleaned data
data = pd.read_csv("output/final_cleaned_data.csv")

# Sort by performance and average_score
data.sort_values(by=["performance", "average_score"], ascending=[True, False], inplace=True)

# Save final ready dataset
data.to_csv("output/StudentPerformance_FinalReady.csv", index=False)
print("✅ Final ready data saved as 'StudentPerformance_FinalReady.csv'")
