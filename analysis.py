import pandas as pd

# Load dataset
df = pd.read_csv("movies.csv")

# Display first 5 rows before cleaning
print("\nFirst 5 rows of the dataset (Before Cleaning):")
print(df.head())

# Check for missing values
print("\nMissing Values in Dataset (Before Cleaning):")
print(df.isnull().sum())

# Convert Released_Year to numeric (handling errors)
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")

# Drop rows where Released_Year couldn't be converted and create a copy
df = df.dropna(subset=["Released_Year"]).copy()

# Convert it to an integer type
df["Released_Year"] = df["Released_Year"].astype(int)

# Fill missing Certificate values with 'Unknown' using .loc to avoid SettingWithCopyWarning
df.loc[:, "Certificate"] = df["Certificate"].fillna("Unknown")

# Fill missing Meta_score with the mean
df.loc[:, "Meta_score"] = df["Meta_score"].fillna(df["Meta_score"].mean())

# Convert Gross column to numeric (remove commas first)
df["Gross"] = df["Gross"].astype(str).str.replace(",", "", regex=True)

# Convert Gross to float
df["Gross"] = pd.to_numeric(df["Gross"], errors="coerce")

# Fill missing Gross values with 0
df["Gross"].fillna(0, inplace=True)  # OR df["Gross"].fillna(df["Gross"].mean(), inplace=True)

# Display first 5 rows after cleaning
print("\nFirst 5 rows of the dataset (After Cleaning):")
print(df.head())

# Check for missing values after cleaning
print("\nMissing Values in Dataset (After Cleaning):")
print(df.isnull().sum())

# Get dataset information
print("\nDataset Info:")
print(df.info())

# Get summary statistics
print("\nStatistical Summary:")
print(df.describe())


