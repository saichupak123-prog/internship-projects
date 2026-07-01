import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("books.csv")

data["Rating"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Book Ratings")
plt.ylabel("")

plt.show()
