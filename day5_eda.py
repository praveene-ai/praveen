import pandas as pd
import numpy as np


df = pd.read_csv("clean_data.csv")

df["department"] = df["department"].replace({
    "It": "IT",
    "Hr": "HR"
})
print("Cleaned dataset loaded successfully!")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())


print("\n========== SUMMARY STATISTICS ==========")

salary_summary = df["salary"].agg([
    "mean",
    "median",
    "min",
    "max",
    "std"
])

print(salary_summary)


print("\n========== DEPARTMENT SALARY SUMMARY ==========")

department_summary = df.groupby("department").agg(
    employee_count=("salary", "count"),
    average_salary=("salary", "mean"),
    median_salary=("salary", "median"),
    minimum_salary=("salary", "min"),
    maximum_salary=("salary", "max")
)

print(department_summary)


print("\n========== CITY SALARY SUMMARY ==========")

city_summary = df.groupby("city").agg(
    employee_count=("salary", "count"),
    average_salary=("salary", "mean"),
    median_salary=("salary", "median"),
    minimum_salary=("salary", "min"),
    maximum_salary=("salary", "max")
)

print(city_summary)

print("\n========== CORRELATION ==========")

numeric_df = df.select_dtypes(include="number")

correlation_matrix = numeric_df.corr()

print(correlation_matrix)


import matplotlib.pyplot as plt

print("\n========== SALARY VISUALIZATION ==========")

plt.figure(figsize=(8, 5))

plt.bar(df["name"], df["salary"])

plt.xlabel("Employee")
plt.ylabel("Salary")
plt.title("Employee Salary Comparison")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("employee_salary_chart.png")

print("Chart saved successfully as employee_salary_chart.png")

plt.show()

print("\n========== MERGE DEPARTMENT SUMMARY ==========")

department_summary = pd.read_csv("department_summary_output.csv")

merged_df = pd.merge(
    df,
    department_summary,
    on="department",
    how="left"
)

print(merged_df)


print("\n========== AVERAGE SALARY BY DEPARTMENT ==========")

plt.figure(figsize=(8, 5))

plt.bar(
    merged_df["department"],
    merged_df["avg_salary"]
)

plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")

plt.tight_layout()

plt.savefig("average_salary_by_department.png")

print("Chart saved successfully as average_salary_by_department.png")

plt.show()