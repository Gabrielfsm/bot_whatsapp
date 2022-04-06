#bibliotecas necessarias, caso não tenha instalada em sua máquina basta executar os comandos (pip instal....)
from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
import time

#Abre o Chrome
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
time.sleep(15) #da um sleep de 15 segundos, tempo para scannear o QRCODE

#Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serão enviadas as mensagens
contatos = ['Gabriel']

#Mensagem - Mensagem que sera enviada
mensagem = 'Olá, pessoa!'

#Função que pesquisa o Contato/Grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Função que envia a mensagem
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(str(mensagem))
    campo_mensagem[1].send_keys(Keys.ENTER)

#Percorre todos os contatos/Grupos e envia as mensagens
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)      
    time.sleep(1)
