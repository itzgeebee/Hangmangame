# A price scraping bot for zillow website that gets the prices for specified house-type in a particular location

from selenium_input import InputGoogleForms
from scrape_engine import ScrapeEngine

scrape = ScrapeEngine()
input_forms = InputGoogleForms()

address = scrape.get_details()
print(len(scrape.link))
for i in range(len(scrape.link)):
    input_forms.enter_data(add=scrape.address[i], pr=scrape.price[i], lnk=scrape.link[i])



