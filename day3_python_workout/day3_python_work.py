import pandas as pd

# 1. Read your workout CSV file into a DataFrame
df = pd.read_csv("employees.csv")
print("--- 1. First 3 Rows of Data ---")
print(df.head(3))

# 2. Check for missing values and duplicates
print("\n--- 2. Data Cleaning Check ---")
print("Missing values per column:\n", df.isna().sum())
print("Duplicate rows count:", df.duplicated().sum())

# 3. Filter data (Find employees in Chennai)
print("\n--- 3. Filtered Employees (Chennai) ---")
chennai_team = df[df["city"] == "Chennai"]
print(chennai_team[["name", "department"]])

# 4. Group and Aggregate (Salary summary by department)
print("\n--- 4. Groupby Summary by Department ---")
dept_summary = df.groupby("department").agg(
    total_salary=("salary", "sum"),
    avg_salary=("salary", "mean"),
    employee_count=("name", "count"),
)
print(dept_summary)


# 5. Save the cleaned/aggregated data to a new CSV file
dept_summary.to_csv("department_summary_output.csv")
print("\n--- 5. Saved summary to 'department_summary_output.csv' ---")

# 6. Write/Export data to an Excel file (using openpyxl)
df.to_excel("employees_exported.xlsx", sheet_name="EmployeesData", index=False)
print("--- 6. Exported full data to Excel successfully ---")