# A linkedin job application bot created using selenium. Currently I modifed the functionality to save jobs only
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PHONE: "Your phone number"

chrome_driver_path = "Your chrome driver path"
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)
driver.get("https://your job search url")
driver.maximize_window()


def sign_in():
    """signs into linkedin with your provided details"""
    email = "your email acct"
    password = "your password"

    signup_btn = driver.find_element(by=By.CSS_SELECTOR, value=".nav__button-secondary")
    time.sleep(1)
    signup_btn.click()
    email_input= driver.find_element(by=By.CSS_SELECTOR, value="#username")
    time.sleep(1)
    email_input.send_keys(email)
    time.sleep(1)
    password_input = driver.find_element(by=By.CSS_SELECTOR, value="#password")
    password_input.send_keys(password)
    sign_in_btn = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
    time.sleep(1)
    sign_in_btn.click()
sign_in()

def apply():
    apply_btn = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-apply-button")
    apply_btn.click()
    time.sleep(2)
    phone_number_form = driver.find_element(by=By.NAME, value='urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2940288010,9,phoneNumber~nationalNumber)")"urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2940288010,9,phoneNumber~nationalNumber)')
    phone_number_form.send_keys(PHONE)
    try:

        next_btn = driver.find_element(by=By.CSS_SELECTOR, value="#ember766")
        next_btn.click()
    except NoSuchElementException:
        pass

def save_job():
    time.sleep(2)
    save_btn = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
    save_btn.click()

all_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".jobs-search-results__list")

for i in all_jobs:
    time.sleep(1)
    i.click()
    save_job()



#driver.quit()
