import os.path
from time import sleep

import pyperclip
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


## Setup chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--user-data-dir=~/.config/google-chrome")
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
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
    # Get page
    browser.get(f"https://web.whatsapp.com/send?phone={phone_number}")
    try:
        browser.implicitly_wait(30)
        browser.find_element(By.XPATH, '//*[@aria-label="Scan me!"]')
        input(
            "The first time you need to register, scan the code in the browser and press enter"
        )
    except NoSuchElementException:
        pass
        # if browser.find_element(By.XPATH, '//*[@aria-label="Scan me!"]'):
        #     input("The first time you need to register, scan the code in the browser and press enter")
        #     return

        # Extract description from page and print
        description = browser.find_element(By.NAME, "description").get_attribute(
            "content"
        )
        print(f"{description}")

    except Exception as e:
        raise e


# fd365im1 to2l77zo bbv8nyr4 gfz4du6o ag5g9lrv bze30y65 bdf91cm1 mwp4sxku
def send(textOrImoji: str, press_enter: bool = False, checkTextOrEmoji: str = ""):
    try:
        browser.implicitly_wait(30)
        text = browser.find_element(
            By.XPATH, '//*[@data-testid="conversation-compose-box-input"]'
        )
        if checkTextOrEmoji == "text":
            # print(checkTextOrEmoji, textOrImoji, text)
            text.send_keys(f"{textOrImoji}")
        elif checkTextOrEmoji == "emoji":
            # elif not textOrImoji[1]:
            # print(textOrImoji.encode("utf-8").decode("unicode_escape"), press_enter)
            pyperclip.copy(textOrImoji)
            text.send_keys(Keys.CONTROL, "v")
        # text.send_keys(Keys.ENTER)
        if press_enter:
            text.send_keys(Keys.ENTER)
            print(f"{text.text} sent successfully")
    except Exception as e:
        raise e


def closeBrowser():
    sleep(5)
    browser.quit()

# def browerMain():
