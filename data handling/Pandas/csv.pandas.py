import pandas as pd
from pathlib import Path

file_path = Path(r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\data handling\CSV\data.csv")


df = pd.read_csv(file_path)
# Instantly see the data
print(df)
print(df.shape)      # How many rows and columns?
print(df.head(3))    # First 3 rows
# Access a single COLUMN
print(df['name'])    # All names
print(df['score'])   # All scores
# Access a single ROW by position
print(df.iloc[0])    # First row (index 0)
print(df.iloc[-1])   # Last row
# Access a specific CELL
print(df.iloc[0]['name'])   # 'Alice'
print(df.at[2, 'score'])    # Charlie's score: 92
#saving dataframes to files
# After you have changed the data, save it back


# Define the folder prefix
folder = "PANDAS"

# Save back to CSV in the specific folder
df.to_csv(folder + 'students_updated.csv', index=False)

# Save to JSON format in the specific folder
df.to_json(folder + 'students.json', orient='records', indent=4)

# Save to Excel format in the specific folder
df.to_excel(folder + 'students.xlsx', index=False)