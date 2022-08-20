from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

link = 'https://cadastramento-demo.mercafacil.com/#/home'
cnpj = '43.226.378/0001-10'
razao_social = 'Silvana e Emilly Publicidade e Propaganda ME'
celular = '(62) 98751-7969'
tel_contato = '(62) 3568-7729'
email = 'cobranca@silvanaeemillypublicidadeepropagandame.com.br'
cep = '74483-410'
numero = '45'


# Acessando a pagina de cadastro CNPJ

nav = webdriver.Chrome()
nav.get(link)
nav.maximize_window()
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/section/div/div[2]/button').click()
sleep(3)
nav.find_element(By.ID,'input-19').send_keys(cnpj)
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div[2]/div/div/div[2]/button').click()
sleep(3)

# validando os campos de cadastro

nav.find_element(By.ID,'input-46').send_keys(Keys.TAB)
sleep(3)
nav.find_element(By.ID,'input-46').send_keys(razao_social)
sleep(2)
nav.find_element(By.ID,'input-50').send_keys(celular)
sleep(3)
nav.find_element(By.ID,'input-50').send_keys(Keys.TAB)
sleep(3)
nav.find_element(By.ID,'input-54').send_keys(Keys.TAB)
sleep(2)
nav.find_element(By.ID,'input-54').send_keys(tel_contato)
sleep(2)
nav.find_element(By.ID,'input-58').send_keys(email)
sleep(2)
nav.find_element(By.ID,'input-75').send_keys(Keys.TAB)
sleep(2)
nav.find_element(By.ID,'input-75').send_keys(cep)
sleep(2)
nav.find_element(By.ID,'input-102').send_keys(Keys.DOWN)
sleep(2)
nav.find_element(By.ID,'input-102').send_keys(numero)
sleep(2)
nav.find_element(By.ID,'input-102').send_keys(Keys.TAB)
sleep(2)
nav.find_element(By.ID,'input-102').send_keys(Keys.PAGE_DOWN)
sleep(3)

# marcando os termos de adesão

nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div/div[2]/div/div/div/div[9]/div[1]').click()
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div/div/div[2]/button[1]').click()
sleep(3)
nav.delete_all_cookies()
sleep(2)
nav.close()

