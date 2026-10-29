
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read employee data
df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df)

# Step 2: Calculate average salary by department
avg_salary = df.groupby("department")["salary"].mean()

# Chart 1: Bar chart
plt.figure(figsize=(8, 5))

bars = plt.bar(
    avg_salary.index,
    avg_salary.values,
    color="skyblue",
    edgecolor="black"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.bar_label(bars, fmt="%.2f", padding=3)

plt.tight_layout()
plt.savefig("average_salary_by_department.png", dpi=300)
plt.close()


# Chart 2: Histogram with 5 bins
plt.figure(figsize=(8, 5))

plt.hist(
    df["salary"],
    bins=5,
    color="lightgreen",
    edgecolor="black"
)

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("salary_histogram.png", dpi=300)
plt.close()


# Chart 3: Scatter plot of ID vs salary by department
plt.figure(figsize=(8, 5))

for department in sorted(df["department"].dropna().unique()):
    department_data = df[df["department"] == department]

    plt.scatter(
        department_data["id"],
        department_data["salary"],
        label=department,
        s=80
    )

plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("employee_id_vs_salary.png", dpi=300)
plt.close()


# Chart 4: Monthly sales line chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    linestyle="-",
    color="blue",
    label="Monthly Sales"
)

plt.title("Monthly Sales from January to June")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.tight_layout()
plt.savefig("monthly_sales.png", dpi=300)
plt.close()

print("\nAll four charts have been saved successfully!")


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)

plt.show()