import pandas as pd


csv_data = """order_id,customer_id,amount
1,101,500
2,102,
3,101,700
3,101,700
4,103,300
5,104,900"""

with open("orders.csv", "w") as f:
    f.write(csv_data)

df = pd.read_csv("orders.csv")


missing_count = df["amount"].isna().sum()
duplicate_count = df.duplicated().sum()
print(f"Missing: amount {missing_count} | Duplicates: {duplicate_count}")


df = df.drop_duplicates()


df["amount"] = pd.to_numeric(df["amount"])
df["order_id"] = df["order_id"].astype(str)


median_val = df["amount"].median()
print(f"Median used: {median_val}")
df["amount"] = df["amount"].fillna(median_val)


result = df.groupby("customer_id").agg(
    total=("amount", "sum"), orders=("order_id", "count")
)
print(result)