#Responsible for getting price data from zillow.com
from bs4 import BeautifulSoup
import requests
import lxml

headers = {"Accept-Language": "en-US,en;q=0.9",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
           "Accept-Encoding":"gzip, deflate",
           "Accept":"text/html,application/xhtml+xml,"
                    "application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
           }

zillow_site = (
    "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22"
    "%3A%7B%22west%22%3A-122.87930525732422%2C%22east%22%3A-121.98735274267578%2C%22south%22%3A37.31307310749719%2C"
    "%22north%22%3A38.23463797317142%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max"
    "%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B"
    "%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A"
    "%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C"
    "%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")

response = requests.get(zillow_site, headers=headers)
real_estate_webpage = response.text
class ScrapeEngine():

    def __init__(self):
        self.soup = BeautifulSoup(real_estate_webpage, "lxml")
        self.address = []
        self.price = []
        self.link = []

    def get_details(self):
        address = self.soup.find_all(name="address", class_ = "list-card-addr")
        for i in address:
            self.address.append(i.text.split(" | ")[-1])

        price = self.soup.find_all(name="div", class_="list-card-price")
        for i in price:
            self.price.append(i.text)

        link = self.soup.find_all(name="a", class_="list-card-link")
        for i in link:
            a = i.get("href")
            if "http" not in a:
                self.link.append(f"https://www.zillow.com/{a}")
            else:
                self.link.append(a)






# print(soup)
#all_anchor_tags = soup.find_all(name="a")

"""for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))"""
