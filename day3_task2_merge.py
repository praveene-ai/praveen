import pandas as pd


orders_data = """order_id,customer_id,amount
1,101,500
2,102,600
3,101,700
4,103,300
5,104,900"""

with open("orders.csv", "w") as f:
    f.write(orders_data)

orders_df = pd.read_csv("orders.csv")
orders_df = orders_df.drop_duplicates()
orders_df["amount"] = pd.to_numeric(orders_df["amount"]).fillna(
    orders_df["amount"].median()
)
orders_df["customer_id"] = orders_df["customer_id"].astype(int)


customers_data = """customer_id,customer_name,city
101,Arun,Chennai
102,Priya,Mumbai
103,Rahul,Chennai
105,Divya,Bangalore"""

with open("customers.csv", "w") as f:
    f.write(customers_data)

customers_df = pd.read_csv("customers.csv")
print("--- Customers Data ---")
print(customers_df)


print("\n--- 1. Inner Join Result ---")
inner_merged = pd.merge(orders_df, customers_df, on="customer_id", how="inner")
print(inner_merged)


print("\n--- 2. Left Join (Customers with no orders) ---")
left_merged = pd.merge(
    customers_df, orders_df, on="customer_id", how="left", indicator=True
)
no_orders = left_merged[left_merged["order_id"].isna()]
print(no_orders[["customer_id", "customer_name", "city"]])


print("\n--- 3. Outer Join (Finding orders with no customer record) ---")
outer_merged = pd.merge(
    orders_df, customers_df, on="customer_id", how="outer", indicator=True
)
unmatched_orders = outer_merged[outer_merged["customer_name"].isna()]
print(unmatched_orders)