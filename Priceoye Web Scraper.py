import requests
from bs4 import BeautifulSoup
import csv

url = "https://priceoye.pk/mobiles/apple"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

names = soup.find_all("div", class_="p-title bold h5")
names_list = []
for i in names:
    names_data = i.text.strip()
    names_list.append(names_data)

current_prices = soup.find_all("div", class_="price-box p1")
current_prices_list = []
for i in current_prices:
    current_prices_data = i.text.strip()
    current_prices_list.append(current_prices_data)

original_price = soup.find_all("div", class_="price-diff-retail")
original_price_list = []
for i in original_price:
    original_price_data = i.text.strip()
    original_price_list.append(original_price_data)

off_percentage = soup.find_all("div", class_="price-diff-saving")
off_percentage_list = []
for i in off_percentage:
    off_percentage_data = i.text.strip()
    off_percentage_list.append(off_percentage_data)

# Specify the CSV file name
csv_file = "apple_products.csv"

# Open the CSV file for writing
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)

    # Write headers (column names) to the CSV
    writer.writerow(["Name", "Current Price", "Original Price", "Discount"])

    # Iterate through all the products and write each one to the CSV
    for i in range(len(names_list)):
        try:
            writer.writerow([names_list[i], current_prices_list[i], original_price_list[i], off_percentage_list[i]])
        except IndexError:
            # Handle missing data gracefully by writing placeholders
            writer.writerow([names_list[i], current_prices_list[i], "", ""])

print(f"Data has been saved to {csv_file}")
