# import packages and libraries needed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "Your chrome driver path"
driver_service = Service(executable_path=chrome_driver_path)

# This class contains the google form filling algorithm(optional)
class InputGoogleForms():

    def __init__(self):
        self.driver = webdriver.Chrome(service=driver_service)

    def enter_data(self, major, ecp, mcp):
        self.driver.get(
            "Your google form link")

        time.sleep(1)
        major = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

        major.send_keys(major)

        time.sleep(1)

        early_career_pay = self.driver.find_element(by=By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        early_career_pay.send_keys(ecp)

        time.sleep(1)

        mid_career_pay = self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        mid_career_pay.send_keys(mcp)

        time.sleep(2)

    

        submit = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()

# This class contains the algorithm for scraping data from the payscale site
class ScrapeEngine():

    def __init__(self):

        self.driver = webdriver.Chrome(service=driver_service)
        self.driver.get(
            "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
        self.major = []
        self.ecp = []
        

    def get_details(self):
        major = self.driver.find_elements(by=By.CSS_SELECTOR, value=".csr-col--school-name .data-table__value")
        for i in major:
            self.major.append(i.text)

        ecp = self.driver.find_elements(by=By.CSS_SELECTOR, value=".csr-col--right .data-table__value")
        for i in ecp:
            self.ecp.append(i.text)
        time.sleep(5)

    def click_button(self):
        nxt_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".pagination__next-btn")
        nxt_button.click()
        time.sleep(2)
