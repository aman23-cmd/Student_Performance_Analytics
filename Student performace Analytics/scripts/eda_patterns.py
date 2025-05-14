# Identifying patterns, trends, and anomalies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("engineered_data.csv")

# Correlation heatmap
sns.heatmap(data[['math_score', 'reading_score', 'writing_score']].corr(), annot=True, cmap='coolwarm')
plt.title("Subject-wise Score Correlation")
plt.show()

# Score distribution by gender
sns.boxplot(x='gender', y='average_score', data=data)
plt.title("Performance by Gender")
plt.show()
