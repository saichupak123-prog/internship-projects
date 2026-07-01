import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("books.csv")

# Display column names
print("Columns:", df.columns.tolist())

# Clean the Price column
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.strip()
)

# Convert Price to float
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Price"])

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=15)
plt.title("Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.savefig("price_distribution.png")
plt.show()

# Rating Bar Chart
if "Rating" in df.columns:
    rating_counts = df["Rating"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    plt.bar(rating_counts.index.astype(str), rating_counts.values)
    plt.title("Books by Rating")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.savefig("rating_chart.png")
    plt.show()

# Top 10 Expensive Books
if "Title" in df.columns:
    top10 = df.sort_values(by="Price", ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    plt.barh(top10["Title"], top10["Price"])
    plt.title("Top 10 Expensive Books")
    plt.xlabel("Price (£)")
    plt.tight_layout()
    plt.savefig("top10_books.png")
    plt.show()

# Box Plot
plt.figure(figsize=(6, 5))
plt.boxplot(df["Price"])
plt.title("Price Box Plot")
plt.ylabel("Price (£)")
plt.savefig("boxplot.png")
plt.show()

print("Visualization completed successfully.")
