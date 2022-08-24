from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Webdriver é um browser para o selenium interagir com a web
url = 'https://www.google.com/'
#url pra acessar
driver = webdriver.Chrome()
#seta o webdriver no chrome
driver.get(url)
#inicia o webdriver na url
messageField = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
#puxa o elemento pelo css selector
messageField.send_keys("pokemon")
#manda a mensagem para o input
asking = driver.find_element(By.CSS_SELECTOR, '.RNmpXc')
#vai no botão estou com sorte
driver.implicitly_wait(10)
#joga uma leve pausa para fechar os elementos que estão tapando o botão
asking.click()
#clica na Pesquisa  
wait = WebDriverWait(driver, 10)
pokemonlink = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gus-wrapper"]/div/div[1]/div/ul/span/li[3]/a')))
#seleciona o link assim que ele estiver disponível
pokemonlink.click()