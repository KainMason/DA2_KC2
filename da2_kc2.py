import pandas as pd

# Read the CSV file
file_path = 'weather.csv'
data = pd.read_csv(file_path)

# Check for any null values in the data
print("# Check for any null values in the data")
print(data.isnull().sum())

# Issue 1: Remove rows with null values in the 'events' column
data.dropna(subset=['events'], inplace=True)

# Issue 2: Fill null values in the 'high' column with 0
data['high'].fillna(0, inplace=True)

# Verify that the null values have been removed and filled
print(" Verify that the null values have been removed and filled")
print(data.isnull().sum())

# Save the cleaned data to a new CSV file
cleaned_file_path = 'weather_cleaned.csv'
data.to_csv(cleaned_file_path, index=False)

# Display the first few rows of the cleaned data
print(" Display the first few rows of the cleaned data")
print(data.head())
