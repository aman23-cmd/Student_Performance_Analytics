import pandas as pd

# Sample data similar to the StudentsPerformance.csv dataset
data = {
    "gender": ["female", "male", "female", "male", "female"],
    "race/ethnicity": ["group B", "group C", "group B", "group A", "group C"],
    "parental level of education": ["bachelor's degree", "some college", "master's degree", "associate's degree", "high school"],
    "lunch": ["standard", "free/reduced", "standard", "free/reduced", "standard"],
    "test preparation course": ["none", "completed", "none", "none", "completed"],
    "math score": [72, 69, 90, 47, 76],
    "reading score": [72, 90, 95, 57, 78],
    "writing score": [74, 88, 93, 44, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("StudentsPerformance.csv", index=False)
print("✅ CSV file 'StudentsPerformance.csv' created successfully!")

# Now load the same CSV
data = pd.read_csv("StudentsPerformance.csv")
print("\n📊 Loaded Data:")
print(data.head())
