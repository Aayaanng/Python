import pandas as pd
from pathlib import Path

file_path = Path(r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\data handling\CSV\data.csv")
df = pd.read_csv(file_path)

new_student = {
    'name': 'Rahul', 'age': 10, 'city': 'Pune', 'score': 83
}
# pd.concat is the modern way to add rows (replaces deprecated .append)
new_row = pd.DataFrame([new_student])
df = pd.concat([df, new_row], ignore_index=True)
print(df)  # Rahul now appears at the bottom!

# --- CREATE: Add a new COLUMN ---
# Add a 'grade' column based on score
def get_grade(score):
    if score >= 90: return 'A'
    elif score >= 75: return 'B'
    else: return 'C'

df['grade'] = df['score'].apply(get_grade)
print(df)  # New 'grade' column added!
# --- READ: Multiple ways to explore data ---

# View all data
print(df)                           # Print entire DataFrame

# View specific columns
print(df[['name', 'score']])        # Only name and score columns
print(df['score'].mean())           # Average score
print(df['score'].max())            # Highest score
print(df['score'].min())            # Lowest score
print(df['score'].sum())            # Total of all scores

# Filter specific rows
print(df[df['score'] >= 90])        # Students with A grade
print(df[df['city'] == 'Delhi'])    # Students from Delhi

# Find a student by name
alice = df[df['name'] == 'Alice']
print(alice)
# --- UPDATE: Change existing values ---

# Update ONE student's score (Alice at index 0)
df.at[0, 'score'] = 91             # Alice's score corrected to 91
print(df.head(2))

# Update ALL scores in a column (give everyone 5 bonus points)
df['score'] = df['score'] + 5
print(df)

# Update based on a condition (update city for Bob only)
df.loc[df['name'] == 'Bob', 'city'] = 'Bangalore'
print(df)

# Rename a column
df = df.rename(columns={'score': 'total_score'})
print(df.columns)  # 'score' is now 'total_score'
# --- DELETE: Remove rows or columns ---

# Delete a ROW by index
df = df.drop(index=0)              # Remove row 0 (Alice)
df = df.reset_index(drop=True)     # Fix the index numbers after deletion
print(df)

# Delete a COLUMN
df = df.drop(columns=['grade'])    # Remove the grade column
print(df.columns)

# Delete MULTIPLE rows at once
df = df.drop(index=[0, 2])         # Remove rows 0 and 2
df = df.reset_index(drop=True)
print(df)

# Delete rows WHERE a condition is True
df = df[df['total_score'] >= 70]   # Keep only students with score >= 70
df = df.reset_index(drop=True)     # Fix index
print(df)
