import pandas as pd

file_path = "data/car_dataset_india.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Original number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five records:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nMissing values per column:")
print(df.isnull().sum())

duplicate_count = df.duplicated().sum()
print("\nDuplicate rows found:", duplicate_count)

df = df.drop_duplicates()

print("Duplicate rows removed:", duplicate_count)
print("Rows after removing duplicates:", df.shape[0])

cleaned_file_path = "data/car_dataset_india.csv"
df.to_csv(cleaned_file_path, index=False)

print("\nCleaned dataset saved successfully!")

print("\nNumerical summary:")
print(df.describe())