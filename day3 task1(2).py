
import pandas as pd

df = pd.read_csv("employees.csv")

print("First 5 rows:")
print(df.head())

print("\nDataFrame information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

print("\nName column:")
print(df["name"])

print("\nName and salary:")
print(df[["name", "salary"]])

print("\nChennai employees:")
chennai = df.loc[df["city"] == "Chennai", "name"]
print(", ".join(chennai))

print("\nILOC slice:")
print(df.iloc[0:3, 1:3])

high_salary = df[df["salary"] > 50000]
print("\nSalary above 50000:", len(high_salary), "employees")

it_employees = df[df["department"] == "IT"]
print("IT department:", ", ".join(it_employees["name"]))
print("IT department count:", len(it_employees))
