import pandas as pd

# Read the CSV file from a different location
df = pd.read_csv(r"C:\Users\91798\OneDrive\Desktop\input.txt")

# Print the DataFrame to see what it looks like
print(df.head())

# Save it to a new CSV (optional)
df.to_csv("output.csv", index=False)

print("CSV read and saved successfully.")
