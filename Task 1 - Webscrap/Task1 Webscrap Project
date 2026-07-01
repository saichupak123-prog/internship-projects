import requests
from bs4 import BeautifulSoup
import csv

with open("books.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)
    writer.writerow(["Book Name", "Price", "Rating"])

    for page in range(1, 51):

        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        print("Scraping Page:", page)

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:

            name = book.h3.a["title"]

            price = book.find("p", class_="price_color").text.replace("Â", "")

            rating = book.find("p", class_="star-rating")["class"][1]

            writer.writerow([name, price, rating])

print("All 1000 books saved successfully!")
