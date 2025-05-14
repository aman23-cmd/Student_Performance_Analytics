import pandas as pd

# Load cleaned data
data = pd.read_csv("output/cleaned_data.csv")

# Feature Engineering: Add average score and performance label
data["average_score"] = data[["math score", "reading score", "writing score"]].mean(axis=1)

def grade_label(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    else:
        return "Poor"

data["performance"] = data["average_score"].apply(grade_label)

# Save engineered data
data.to_csv("output/engineered_data.csv", index=False)
print("✅ Feature engineered data saved as 'engineered_data.csv'")
