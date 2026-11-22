# Pandas Series and DataFrame
import pandas as pd
marks = pd.Series([95, 81, 88, 68, 75],
index=["A", "B", "C", "D", "E"])
print("--- Pandas Series ---")
print(marks)
data = {
"RollNo": [121, 122, 123, 124, 125],
"Name": ["Aishwarya", "Rafiya", "Ranjani", "Sakthi", "Arshitha"],
"Department": ["IT", "AIDS", "AIML", "CSE", "ECE"],
"Mark": [95, 81, 88, 68, 75]
}
df = pd.DataFrame(data)
print("\n--- DataFrame ---")
print(df)
print("\nAverage Mark:", round(df["Mark"].mean(), 2))
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])