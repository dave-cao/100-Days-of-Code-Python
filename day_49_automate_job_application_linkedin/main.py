# Automate job applications
import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASS = os.environ["MY_PASS"]

chrome_driver_path = "/home/cow/Documents/System/Development/chromedriver"
s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
search_url = "https://www.linkedin.com/jobs/search/?currentJobId=3385396665&f_AL=true&f_E=1&f_WT=2&geoId=101174742&keywords=developer&location=Canada&refresh=true&sortBy=R"
driver.get(search_url)


# click on sign in button
sign_in_button = driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]"
)
sign_in_button.click()

# Now we are in sign field -- fill in info and sign in
email_input = driver.find_element(by=By.ID, value="username")
password_input = driver.find_element(by=By.ID, value="password")

email_input.send_keys(MY_EMAIL)
password_input.send_keys(MY_PASS)
password_input.send_keys(Keys.ENTER)

# Instead of applying to jobs, just save the job listing
job_cards = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-list__title")
# get the links of each job
job_links = [job.get_attribute("href") for job in job_cards]

# Go through each job link and click on the save button
for job in job_links:
    driver.get(job)
    save_button = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
    save_button.click()


time.sleep(10)
