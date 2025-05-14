# Final save of processed and cleaned data
import pandas as pd

data = pd.read_csv("final_cleaned_data.csv")
data.to_csv("StudentPerformance_FinalReady.csv", index=False)
print("Data saved successfully!")
