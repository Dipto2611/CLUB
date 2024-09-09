import pandas as pd

# Create a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Get basic statistical summary
print(df.describe())
