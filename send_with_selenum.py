import time
import os.path

import pyperclip
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


## Setup chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--user-data-dir=~/.config/google-chrome")#/home/mefathim-tech-29/.config/google-chrome")
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_argument("--no-default-browser-check")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--disable-default-apps")
# chrome_options.add_argument("--new-window")

# firefox_options = Options()
# firefox_options.add_argument("--headless") # Ensure GUI is off
# firefox_options.add_argument("--no-sandbox")
# # firefox_options.add_argument("--user-data-dir=/home/mefathim-tech-29/.config/google-chrome")
# firefox_options.add_argument("--no-default-browser-check")
# firefox_options.add_argument("--disable-extensions")
# firefox_options.add_argument("--disable-popup-blocking")
# firefox_options.add_argument("--disable-default-apps")
# firefox_options.add_argument("--new-window")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)


def openBrowser(phone_number):
    # Choose Chrome Browser
    try:
        # Get page
        browser.get(f"https://web.whatsapp.com/send?phone={phone_number}")
        browser.implicitly_wait(30)
        if browser.find_element(By.XPATH, '//*[@aria-label="Scan me!"]'):
            input("The first time you need to register, scan the code in the browser and press enter")
            return

        # Extract description from page and print
        description = browser.find_element(By.NAME, "description").get_attribute("content")
        print(f"{description}")

    except Exception as e:
        raise e


def send(textOrImoji, press_enter=False):
    try:
        browser.implicitly_wait(30)
        text = browser.find_element(By.XPATH,
                                    '//*[@class="fd365im1 to2l77zo bbv8nyr4 gfz4du6o ag5g9lrv bze30y65 bdf91cm1 mwp4sxku"]')
        pyperclip.copy(textOrImoji)
        text.send_keys(Keys.CONTROL, 'v')
        if press_enter:
            text.send_keys(Keys.ENTER)
            print(f"{text.text} sent successfully")
    except Exception as e:
        raise e


def closeBrowser():
    # Wait for 10 seconds
    time.sleep(10)
    browser.quit()
