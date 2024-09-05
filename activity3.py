import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://estudante.ifpb.edu.br/")
sleep(5)

links = driver.find_elements(By.TAG_NAME, "a")
print(f"A página inicial do IFPB tem {len(links)} links")

invalid_links = 0
for link in links:
  url = link.get_attribute('href')
  if url:
    try:
      response = requests.head(url=url, timeout=5)
      status = response.status_code
      if status >= 400:
        invalid_links += 1
        print(f"Link inválido: {url} - Código HTTP: {status}")
    except Exception as e:
      print(f"Link inválido: {url} - Erro: {e}")

print(f"A página inicial do IFPB tem {invalid_links} links inválidos")

driver.quit()