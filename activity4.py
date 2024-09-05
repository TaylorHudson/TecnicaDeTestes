from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()

driver.get('https://estudante.ifpb.edu.br/cursos/')

cidade_xpath = '//*[@id="id_cidade"]'
modalidade_xpath = '//*[@id="id_modalidade"]'
pesquisar_button_xpath = '/html/body/div[2]/div/div/div[2]/div[2]/div/form/div[1]/button'
curso_xpath = '/html/body/div[2]/div/div/div[2]/div[4]/div[1]/div/a' 

cidade_select = Select(driver.find_element(By.XPATH, cidade_xpath))
cidade_select.select_by_visible_text('Monteiro/PB')

sleep(2)

modalidade_select = Select(driver.find_element(By.XPATH, modalidade_xpath))
modalidade_select.select_by_visible_text('Presencial')

sleep(2)

driver.find_element(By.XPATH, pesquisar_button_xpath).click()

sleep(2)

driver.find_element(By.XPATH, curso_xpath).click()

sleep(5)

driver.quit()