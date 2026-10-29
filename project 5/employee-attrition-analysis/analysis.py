import pandas as pd

# Load dataset from the data folder
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
print('=== 1. SHAPE ===')
print(df.shape)

print('\n=== 2. INFO ===')
print(df.info())

print('\n=== 3. DESCRIBE ===')
print(df.describe())

print('\n=== 4. MISSING VALUES ===')
print(df.isna().sum())

print('\n=== 5. DUPLICATES ===')
print(df.duplicated().sum())