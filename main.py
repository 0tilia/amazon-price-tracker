import smtplib

import requests
from bs4 import BeautifulSoup
import lxml

my_email = ""
my_pass = ""

PRODUCT_URL = "https://www.amazon.com/Pocmimut-Makeup-Cosmetic-Toiletry-Reusable/dp/B08R3QJJWL/ref=sr_1_15?keywords=makeup%2Bbag&qid=1668521389&sprefix=make%2Caps%2C190&sr=8-15&th=1"


response = requests.get(url=PRODUCT_URL, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ro;q=0.8",
})

# print(response.text)

soup = BeautifulSoup(response.content, "lxml")

# print(soup.prettify())

data = soup.find(name="span", class_="a-offscreen").get_text()
price = float(data.split("$")[1])
print(price)

title = "bag"

buy_price = 12

if price < buy_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:Amazon Price Alert! \n{PRODUCT_URL}")
        connection.close()
