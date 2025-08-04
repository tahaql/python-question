import pandas as pd
from io import StringIO

data = StringIO("""
date,product,price
2025-07-01,product_A,120000
2025-07-01,product_B,80000
2025-07-02,product_A,120000
2025-07-03,product_C,150000
2025-07-03,product_B,80000
2025-07-04,product_A,120000
2025-07-04,product_B,80000
2025-07-04,product_C,150000
""")

df = pd.read_csv(data, parse_dates=["date"])
print(df)

total_sales = df["price"].sum()
print("🔹 مجموع کل فروش:", total_sales,"\n")

average_price = df["price"].mean()
print("🔹 میانگین مبلغ فروش:", average_price,"\n")

sales_by_day = df.groupby("date")["price"].sum()
max_sales_day = sales_by_day.idxmax()
max_sales_amount = sales_by_day.max()

print(f"🔹 بیشترین فروش مربوط به تاریخ {max_sales_day.date()} با مبلغ {max_sales_amount} تومان بوده.","\n")

sales_count_per_day = df.groupby("date").size()
print("🔹 تعداد فروش در هر روز:")
print(sales_count_per_day,"\n")