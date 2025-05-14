# Initial visual representation of key findings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("final_cleaned_data.csv")

# Average score per grade
sns.barplot(x='grade', y='average_score', data=data, estimator=lambda x: round(x.mean(), 2))
plt.title("Average Score by Grade")
plt.ylabel("Average Score")
plt.show()

# Count plot by gender and lunch
sns.countplot(x='gender', hue='lunch', data=data)
plt.title("Gender-wise Lunch Type")
plt.show()
