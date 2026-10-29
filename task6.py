import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


os.makedirs("reports/figures", exist_ok=True)


sns.set_theme(style="whitegrid")
PRIMARY_COLOR = "#2b5c8f"


df = pd.read_csv("employees.csv")


plt.figure(figsize=(8, 5))
dept_salary = df.groupby("department")["salary"].mean().reset_index()

sns.barplot(
    data=dept_salary, x="department", y="salary", color=PRIMARY_COLOR
)
plt.title("Average Salary by Department", fontsize=14, pad=12)
plt.xlabel("Department", fontsize=11)
plt.ylabel("Average Salary (INR)", fontsize=11)
plt.tight_layout()
plt.savefig("reports/figures/01_bar_chart.png", dpi=300, bbox_inches="tight")
plt.close()
print(
    "Insight 1 (Bar Chart): Finance records the highest average salary (90,000 INR), whereas Sales displays the lowest."
)


plt.figure(figsize=(8, 5))
sns.histplot(
    df["salary"], bins=5, kde=True, color=PRIMARY_COLOR, edgecolor="black"
)
plt.title("Employee Salary Distribution", fontsize=14, pad=12)
plt.xlabel("Salary (INR)", fontsize=11)
plt.ylabel("Employee Count", fontsize=11)
plt.tight_layout()
plt.savefig("reports/figures/02_histogram.png", dpi=300, bbox_inches="tight")
plt.close()
print(
    "Insight 2 (Histogram): Most employee salaries are concentrated between 40,000 and 70,000 INR."
)


plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, x="id", y="salary", hue="city", s=120, palette="Set1"
)
plt.title("Employee ID vs Salary by City Location", fontsize=14, pad=12)
plt.xlabel("Employee ID", fontsize=11)
plt.ylabel("Salary (INR)", fontsize=11)
plt.legend(title="City", loc="upper left")
plt.tight_layout()
plt.savefig(
    "reports/figures/03_scatter_plot.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(
    "Insight 3 (Scatter Plot): Employees in Bangalore and Mumbai generally occupy higher salary tiers compared to Chennai."
)


plt.figure(figsize=(8, 5))
df_sorted = df.sort_values(by="salary").reset_index(drop=True)

plt.plot(
    df_sorted["name"],
    df_sorted["salary"],
    marker="o",
    linewidth=2,
    color=PRIMARY_COLOR,
    label="Salary",
)
plt.title("Sorted Employee Salary Progression", fontsize=14, pad=12)
plt.xlabel("Employee Name", fontsize=11)
plt.ylabel("Salary (INR)", fontsize=11)
plt.xticks(rotation=45)
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("reports/figures/04_line_chart.png", dpi=300, bbox_inches="tight")
plt.close()
print(
    "Insight 4 (Line Chart): Employee compensation scales steadily from Arun (30,000 INR) up to Karthik (90,000 INR)."
)


plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="department", y="salary", palette="Blues")
plt.title("Salary Distribution Across Departments", fontsize=14, pad=12)
plt.xlabel("Department", fontsize=11)
plt.ylabel("Salary (INR)", fontsize=11)
plt.tight_layout()
plt.savefig("reports/figures/05_box_plot.png", dpi=300, bbox_inches="tight")
plt.close()
print(
    "Insight 5 (Box Plot): The IT department shows the widest salary spread ranging from 60,000 to 75,000 INR."
)

print("\nAll 5 charts successfully generated and saved in reports/figures/")