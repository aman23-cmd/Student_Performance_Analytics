# Feature selection and engineering
import pandas as pd

data = pd.read_csv("cleaned_data.csv")

# Creating average score column
data['average_score'] = data[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

# Grading system
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'D'

data['grade'] = data['average_score'].apply(assign_grade)

data.to_csv("engineered_data.csv", index=False)
