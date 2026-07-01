import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("books.csv")

data["Rating"].value_counts().plot(kind="bar")

plt.title("Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.show()
