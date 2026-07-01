import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("books.csv")

data["Price"] = data["Price"].str.replace("£", "", regex=False)
data["Price"] = data["Price"].astype(float)

plt.hist(data["Price"])

plt.title("Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.show()
