from selenium import webdriver
from time import sleep

seconds_to_sleep = 2
driver = webdriver.Firefox()

driver.get("https://google.com")
sleep(seconds_to_sleep)

driver.get("https://facebook.com")
sleep(seconds_to_sleep)

driver.get("https://stackoverflow.com")
sleep(seconds_to_sleep)

driver.back()
sleep(seconds_to_sleep)

driver.back()
sleep(seconds_to_sleep)

driver.forward()
sleep(seconds_to_sleep)

driver.refresh()
sleep(seconds_to_sleep)

driver.maximize_window()
sleep(seconds_to_sleep)

size = driver.get_window_size()
print(f"Width: {size['width']}")
print(f"Height: {size['height']}")
sleep(seconds_to_sleep)

driver.quit()