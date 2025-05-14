# Handling outliers and data transformations
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("engineered_data.csv")

# Visualizing outliers
for subject in ['math_score', 'reading_score', 'writing_score']:
    sns.boxplot(x=data[subject])
    plt.title(f"{subject.title()} Outliers")
    plt.show()

# Optionally: Apply transformations or remove outliers
# Example: Remove entries with any score > 100 or < 0
data = data[(data['math_score'] <= 100) & (data['reading_score'] <= 100) & (data['writing_score'] <= 100)]

data.to_csv("final_cleaned_data.csv", index=False)
