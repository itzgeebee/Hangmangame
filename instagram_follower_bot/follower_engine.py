# A simple bot made using selenium that follows the users of any account you specify
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "Your driver path"
driver_service = Service(executable_path=chrome_driver_path)

handle = "https://www.instagram.com/eminem/"
USERNAME = "Your IG username"
PASSWORD = "Your Ig password"

class InstaFollowers():

    def __init__(self):
        self.driver = webdriver.Chrome(service=driver_service)

    def login(self):
        self.driver.get(handle)
        time.sleep(2)

        log_in = self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
        log_in.click()
        time.sleep(2)

        user_name = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(USERNAME)
        time.sleep(2)

        password = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(2)

        enter = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
        enter.click()
        time.sleep(5)

        not_now = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
        time.sleep(3)

    def find_followers(self):
        followers = self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')

        followers.click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)

    def follow(self):
        follow = self.driver.find_elements(by=By.CLASS_NAME, value='sqdOP')
        for i in follow:
            if i.text == "Following":
                continue
            else:
                i.click()
                time.sleep(2)

