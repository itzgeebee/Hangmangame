# A script that uses beautifulsoup to scrape for the price of a product and sends an email when the price codition you set is met
from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

amazon_site = "https://www.amazon.com/ASUS-Display-R9-5900HX-Keyboard-G513QR-ES96/dp/B08SJTW9LK/ref=sr_1_3?keywords=asus+rog&qid=1646175658&sr=8-3"
headers = {"Accept-Language": "en-US,en;q=0.9",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
           "Accept-Encoding":"gzip, deflate",
           "Accept":"text/html,application/xhtml+xml,"
                    "application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
           }
#scrape amazon
response = requests.get(url=amazon_site, headers=headers).text

soup = BeautifulSoup(response, "lxml")
output = soup.find(name="span", class_="a-offscreen").get_text()
new_output = float(output.replace("$","").replace(",",""))
print(new_output)

#send mail
my_email = ""
password = ""
email = ""
if new_output <= 1800:

    with smtplib.SMTP("smtp.gmail.com") as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=password)
        new_connection.sendmail(from_addr=my_email, to_addrs=email,
                                msg=f"Subject: Low price alert!. \n\n price for ASUS rog is below {new_output}")

