from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "aakifkhan.100daysofcode@gmail.com"
ACCOUNT_PASSWORD = '4ViZ%N&aT4op$gu&'
PHONE = "1234567890"


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com")

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()

time.sleep(5)
user_name = driver.find_element(By.ID, value="username")
user_name.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.ID, value="password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(30)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".button jobss-apply-button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

       
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)