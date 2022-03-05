from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Servfrom selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "Your driver path"

driver_service = Service(executable_path=chrome_driver_path)


class InternetSpeedTwitterBot():
    
    def __init__(self):
        self.driver = webdriver.Chrome(service=driver_service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """gets the internet speed when called"""
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        go = self.driver.find_element(by=By.XPATH,
                                      value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(120)
        download_speed = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                     '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                     '1]/div[2]/div/div[2]/span').text

        upload_speed = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                      '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div['
                                                      '2]/span').text
        self.up = float(upload_speed)
        self.down = float(download_speed)

    def tweet_at_provider(self, upload, download):

        self.driver.get("https://twitter.com/login")

        time.sleep(3)
        
        email = self.driver.find_element(by=By.NAME, value='text')
        email.send_keys("Your email or username")
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(3)

        password = self.driver.find_element(by=By.NAME,
                                            value='password')
        password.send_keys("Your twitter password")

        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(2)

        bot_text = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                               '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                               '1]/div/div/div/div[2]/div['
                                                               '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                               '1]/div/div/div/div/div[2]/div/div/div/div')
        bot_text.send_keys(f"MTNNigeria's network is so bad where I am. This is my current internet speed. Upload "
                           f"speed: {upload}mb/s \nDownload speed: {download}mb/s")

        tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                   '2]/main/div/div/div/div/div/div[2]/div/div['
                                                                   '2]/div[1]/div/div/div/div[2]/div[3]/div/div/div['
                                                                   '2]/div[3]')
        tweet_button.click()
