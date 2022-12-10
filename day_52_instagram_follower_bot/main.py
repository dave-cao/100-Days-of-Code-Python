import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=/home/cow/.config/google-chrome/")
# options.add_argument("profile-directory=Profile 6")

load_dotenv()

CHROME_DRIVER_PATH = "/home/cow/Documents/System/Development/chromedriver"
SIMILAR_ACCOUNT = "the.coding.train"


class InstaFollower:
    def __init__(self):
        s = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s, options=options)

        pass

    def login(self):

        # get login page
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        # Fill in form
        login = self.driver.find_element(
            by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        password = self.driver.find_element(
            by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input'
        )

        login.send_keys(os.environ.get("MY_EMAIL"))
        password.send_keys(os.environ.get("MY_PASS"))
        time.sleep(2)
        print("Logging in...")
        password.send_keys(Keys.ENTER)

        time.sleep(4)

    def find_followers(self):

        print("opening account page...")
        self.driver.get(f"https://instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)

        # Click on followers
        follower_button = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a",
        )
        print("Opening followers popup...")
        follower_button.click()

        time.sleep(5)

        f_body = self.driver.find_element(By.XPATH, "//div[@class='_aano']")

        # scroll
        print("Start scrolling")
        scrolling = True
        scroll_count = 0
        while scrolling:
            if scroll_count > 5:
                scrolling = False
            scroll_height = self.driver.execute_script(
                "return arguments[0].scrollHeight", f_body
            )
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", f_body
            )
            time.sleep(2)
            scroll_height_new = self.driver.execute_script(
                "return arguments[0].scrollHeight", f_body
            )
            if scroll_height_new == scroll_height:
                print("Reached the end of the followers list 🥵")
                scrolling = False

            scroll_count += 1

        # get follower buttons

    def follow(self):

        # Followers body popup
        follower_count = 0
        f_body = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        followers_list = f_body.find_elements()
        followers_list = self.driver.find_elements(
            by=By.CSS_SELECTOR, value="div div div div button"
        )
        followers_list = [
            follower for follower in followers_list if follower.text == "Follow"
        ]
        for follower in followers_list:
            try:
                follower_count += 1
                follower.click()
                print(f"Follows: {follower_count}")
                time.sleep(3)

            except NoSuchElementException:
                print("No Followers Here")
                pass
            except ElementClickInterceptedException:
                print("Limit error occured. Try again next time")
                break


follower = InstaFollower()
follower.login()
follower.find_followers()
follower.follow()
