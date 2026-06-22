import pandas as pd

df = pd.read_csv("Superstore sales dataset.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Step 3 starts here

import matplotlib.pyplot as plt
import seaborn as sns

category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)

plt.figure(figsize=(8,5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()
#visualization first Total sales by category end


region_profit = df.groupby("Region")["Profit"].sum()

print(region_profit)

plt.figure(figsize=(8,5))

sns.barplot(
    x=region_profit.index,
    y=region_profit.values
)
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()
#visualization second Total profit by region end

# Monthly Sales Trend
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True
)

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

print(monthly_sales)

plt.figure(figsize=(12,6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.grid(True)

plt.show()

#visualization third Monthly sales trend end

# =========================
# Visualization 4
# Correlation Heatmap
# =========================

numeric_columns = df[
    ["Sales", "Profit", "Quantity", "Discount"]
]

correlation_matrix = numeric_columns.corr()

print(correlation_matrix)

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

#visualization fourth Correlation Heatmap end

# =========================
# Visualization 5
# Top 10 Best Selling Products
# =========================

top_products = df.groupby(
    "Product Name"
)["Sales"].sum().sort_values(
    ascending=False
).head(10)

print(top_products)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 10 Best Selling Products")
plt.xlabel("Sales")
plt.ylabel("Product Name")

plt.show()

#visualization fifth Top 10 Best Selling Products end



