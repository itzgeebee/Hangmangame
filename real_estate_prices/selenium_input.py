# This class is responsible for filling the google forms with the data from the zillow website
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/gb/Documents/chromedriver.exe"
driver_service = Service(executable_path=chrome_driver_path)


class InputGoogleForms():

    def __init__(self):
        self.driver = webdriver.Chrome(service=driver_service)

    def enter_data(self, add, pr, lnk):
        self.driver.get(
            "https://docs.google.com/forms/d/e/1FAIpQLSdLmy8IxuN0l_RzoZ0oW77KjKv-Utjc8kWNOPb_YD8dUk9GZQ/viewform")

        time.sleep(2)
        address = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                              '1]/div/div/div[2]/div/div[1]/div/div[1]/input')

        address.send_keys(add)

        time.sleep(2)

        price = self.driver.find_element(by=By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')
        price.send_keys(pr)

        time.sleep(2)

        link = self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                              '1]/div/div[1]/input')
        link.send_keys(lnk)

        time.sleep(2)

        submit = self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()


