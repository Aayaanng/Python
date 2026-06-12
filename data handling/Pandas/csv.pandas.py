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
import os
import pandas as pd

# 1. Define your folder name
target_folder = "data handling/Pandas"

# 2. Create the folder automatically if it doesn't exist yet
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 3. Combine the folder name with your file names
csv_path = os.path.join(target_folder, 'students_updated.csv')
json_path = os.path.join(target_folder, 'students.json')
excel_path = os.path.join(target_folder, 'students.xlsx')

# 4. Save the files directly into the PANDAS folder
df.to_csv(csv_path, index=False)
df.to_json(json_path, orient='records', indent=4)
df.to_excel(excel_path, index=False)