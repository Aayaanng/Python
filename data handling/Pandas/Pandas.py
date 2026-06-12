import pandas as pd

data = {
    'name':  ['Alice', 'Bob', 'Charlie', 'Priya'],
    'age':   [10, 11, 10, 11],
    'city':  ['Delhi', 'Mumbai', 'Chennai', 'Kolkata'],
    'score': [88, 75, 92, 95]
}
df = pd.DataFrame(data)
print(df)
# These are the FIRST commands you run on any new DataFrame

print(df.head(3))     # First 5 rows (use df.head(3) for 3 rows)
print(df.tail(3))     # Last 5 rows
print(df.shape)      # (rows, columns) — e.g., (4, 4)
print(df.columns)    # List of column names
print(df.dtypes)     # Data type of each column
print(df.info())     # Summary — rows, columns, types, memory
print(df.describe()) # Statistics: min, max, mean, count for numbers
