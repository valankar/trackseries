#!/usr/bin/python
# A script that marks all seasons as watched on trackseries.tv. This is useful
# for subscribing to a new show which has tons of old seasons (Frontline,
# Horizon, etc).
#
# It uses Selenium and Firefox.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

# Get cookies and stuff from this Firefox profile
PROFILE = "/home/valankar/.mozilla/firefox/6vc454j2.default-release"

ffprofile = webdriver.FirefoxProfile(PROFILE)
driver = webdriver.Firefox(firefox_profile=ffprofile)
driver.get("https://www.trackseries.tv/")
input("Go to series page and hit Enter")
num_seasons = len(driver.find_elements_by_xpath("/html/body/div/div[3]/div[2]/div/div[4]/div/ul/li"))
print("Found {} seasons".format(num_seasons))

max_delay = 5
for i in range(1, num_seasons+1):
    # Click the season image
    image_xpath = "/html/body/div/div[3]/div[2]/div/div[4]/div/ul/li[{}]/a/img".format(i)
    driver.find_element_by_xpath(image_xpath).click()
    time.sleep(1)

    try:
        watched_button = WebDriverWait(driver, max_delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/div[2]/div/div[6]/div[1]/div[1]/div[2]/button")))
        watched_button.click()
    except TimeoutException:
        print("Timed out waiting for season {} watched button".format(i))
    time.sleep(5)
