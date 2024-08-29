from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

seconds_to_sleep = 3
long_seconds_to_sleep = 6
name_xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
last_name_xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
email_xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
div_text_xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[1]/div/div[1]/span[1]/div[2]'
textarea_xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
div_first_box_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div'
div_second_box_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div'
next_button_xpath = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span'
div_second_text_xpath = '//*[@id="i1"]/span[1]/div[2]'
second_textarea_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea'
second_page_div_first_box_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div'
second_page_div_second_box_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div'
send_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span'

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdD_Elp2jj-E-kZYS1zcTr6bmirujG_LdnlGRNg9Gbk3Yl7Qg/viewform")
driver.maximize_window()
sleep(seconds_to_sleep)

web_driver_wait = WebDriverWait(driver, 3)

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, name_xpath)))
name_input = driver.find_element(By.XPATH, name_xpath)

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, last_name_xpath)))
last_name_input = driver.find_element(By.XPATH, last_name_xpath)

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, email_xpath)))
email_input = driver.find_element(By.XPATH, email_xpath) 

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, div_text_xpath)))
text = driver.find_element(By.XPATH, div_text_xpath).text

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, textarea_xpath)))
textarea_input = driver.find_element(By.XPATH, textarea_xpath)

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, div_first_box_xpath)))
first_box_option_1 = driver.find_element(By.XPATH, f"{div_first_box_xpath}//span[contains(text(), 'opção 1')]")
first_box_option_3 = driver.find_element(By.XPATH, f"{div_first_box_xpath}//span[contains(text(), 'opção 3')]")

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, div_second_box_xpath)))
second_box_option_4 = driver.find_element(By.XPATH, f"{div_second_box_xpath}//span[contains(text(), 'opção 4')]")

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, next_button_xpath)))
next_button = driver.find_element(By.XPATH, next_button_xpath)

ActionChains(driver)\
  .move_to_element(name_input)\
  .send_keys_to_element(name_input, "Taylor")\
  .pause(seconds_to_sleep)\
  .move_to_element(last_name_input)\
  .send_keys_to_element(last_name_input, "Hudson")\
  .pause(seconds_to_sleep)\
  .move_to_element(email_input)\
  .send_keys_to_element(email_input, "taylor.hudson@academico.ifpb.edu.br")\
  .pause(seconds_to_sleep)\
  .move_to_element(textarea_input)\
  .send_keys_to_element(textarea_input, text)\
  .pause(seconds_to_sleep)\
  .move_to_element(first_box_option_1)\
  .click(first_box_option_1)\
  .pause(seconds_to_sleep)\
  .move_to_element(first_box_option_3)\
  .click(first_box_option_3)\
  .pause(seconds_to_sleep)\
  .move_to_element(second_box_option_4)\
  .click(second_box_option_4)\
  .pause(seconds_to_sleep)\
  .move_to_element(next_button)\
  .click(next_button)\
  .pause(long_seconds_to_sleep)\
  .perform()

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, div_second_text_xpath)))
second_text = driver.find_element(By.XPATH, div_second_text_xpath).text

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, second_textarea_xpath)))
second_textarea_input = driver.find_element(By.XPATH, second_textarea_xpath)

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, second_page_div_first_box_xpath)))
second_page_first_box_option_2 = driver.find_element(By.XPATH, f"{second_page_div_first_box_xpath}//span[contains(text(), 'opção 2')]")
second_page_first_box_option_4 = driver.find_element(By.XPATH, f"{second_page_div_first_box_xpath}//span[contains(text(), 'opção 4')]")

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, second_page_div_second_box_xpath)))
second_page_second_box_option_1 = driver.find_element(By.XPATH, f"{second_page_div_second_box_xpath}//span[contains(text(), 'opção 1')]")

web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, send_button_xpath)))
send_button = driver.find_element(By.XPATH, send_button_xpath)

ActionChains(driver)\
  .move_to_element(second_textarea_input)\
  .send_keys_to_element(second_textarea_input, second_text)\
  .move_to_element(second_page_first_box_option_2)\
  .click(second_page_first_box_option_2)\
  .pause(seconds_to_sleep)\
  .move_to_element(second_page_first_box_option_4)\
  .click(second_page_first_box_option_4)\
  .pause(seconds_to_sleep)\
  .move_to_element(second_page_second_box_option_1)\
  .click(second_page_second_box_option_1)\
  .pause(seconds_to_sleep)\
  .move_to_element(send_button)\
  .click(send_button)\
  .pause(seconds_to_sleep)\
  .perform()

sleep(long_seconds_to_sleep)
driver.quit()