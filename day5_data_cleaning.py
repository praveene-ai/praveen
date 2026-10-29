import pandas as pd
import numpy as np


df = pd.read_csv("employees.csv")

before_rows = len(df)
before_missing = df.isnull().sum().sum()
before_duplicates = df.duplicated().sum()

print("Dataset loaded successfully!")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())


print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())


print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nNumber of rows before cleaning:")
print(len(df))

text_columns = ["name", "department", "city"]

for column in text_columns:
    df[column] = df[column].str.strip().str.title()

print("\nText standardisation completed.")


print("\nUnique names:")
print(df["name"].unique())

print("\nUnique departments:")
print(df["department"].unique())

print("\nUnique cities:")
print(df["city"].unique())



Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["salary"] < lower_limit) |
    (df["salary"] > upper_limit)
]

print("\nSalary Outlier Detection:")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Number of outliers:", len(outliers))


after_rows = len(df)
after_missing = df.isnull().sum().sum()
after_duplicates = df.duplicated().sum()

print("\n========== FINAL SUMMARY ==========")

print("Rows:", before_rows, "->", after_rows)
print("Missing values:", before_missing, "->", after_missing)
print("Duplicates:", before_duplicates, "->", after_duplicates)


df.to_csv("clean_data.csv", index=False)

print("\nClean data saved successfully!")
print("File created: clean_data.csv")

