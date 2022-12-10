import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/home/cow/Documents/System/Development/chromedriver"

TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self):

        s = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s)
        self.down = 0
        self.up = 0

        pass

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]',
        )

        go_button.click()
        print("go button has been clicked after 5 seconds")

        # Try speedtest for desktop popup comes up
        time.sleep(60)
        back_to_test = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a',
        )
        back_to_test.click()
        print("Back to test has been clicked")

        time.sleep(2)
        # Copy down and up speeds
        down_speed = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        )
        up_speed = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        )

        self.down = down_speed.text
        self.up = up_speed.text

    def tweet_at_provider(self):

        self.driver.get("https://twitter.com/")
        # twitter login button
        time.sleep(10)
        login_button = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a',
        )
        login_button.click()

        # Now on login page
        time.sleep(10)
        notification = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/span/span',
        )

        notification.click()

        time.sleep(10)
        email = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
        )
        email.send_keys("MY EMAIL")
        email.send_keys(Keys.ENTER)

        time.sleep(5)
        password = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
        password.send_keys("MY PASSWORD")
        password.send_keys(Keys.ENTER)

        # Now on twitter page, time to tweet
        time.sleep(10)
        tweet = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div',
        )

        try:
            tweet.send_keys(
                f"Hello Internet Provider! Why is my Internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}/up?"
            )
            tweet_button = self.driver.find_element(
                by=By.XPATH,
                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]',
            )
            tweet_button.click()

        except NoSuchElementException:
            print("something happen here man")

        while True:
            continue


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()
