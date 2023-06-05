import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
url = "https://twitter.com/i/flow/login"
driver.get(url)

username = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
username.send_keys("adwaithrajeev@gmail.com")
username.send_keys(Keys.ENTER)

password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password.send_keys("AdwaithEzio")
password.send_keys(Keys.ENTER)

time.sleep(10)

tweet = "Hello Everyone! This is a tweet that I am sending from a selenium automated script written in Python ( It " \
        "feels really awesome (: ) . \n If you too want to learn this supercool trick then visit Hack Club " \
        "Workshops.\n https://workshops.hackclub.com"

tweetInputField = wait.until(EC.visibility_of_element_located((By.XPATH, 'input[aria-label="Tweet text"]')))
tweetInputField.send_keys(tweet)

tweetButton = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
tweetButton.click()

time.sleep(1)

tweetButton.click()
