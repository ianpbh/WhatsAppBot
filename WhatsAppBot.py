from selenium import webdriver
import os
import time
import json
import numpy as np
import cv2 as opencv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def flood(navegador):
    i = 0
    while True:
        navegador.find_element_by_class_name('_3u328').send_keys(i)
        navegador.find_element_by_class_name('_3M-N-').click()
        i = i +1

def loginWhatsapp(navegador):
    navegador.get("http://web.whatsapp.com")
    time.sleep(3)
    navegador.save_screenshot('qrcode/qrcode.png')
    image = opencv.imread('qrcode/qrcode.png')
    time.sleep(2)
    opencv.imshow('QR Code (Pressione qualquer tecla quando tiver escaneado)',image)
    time.sleep(2)
    while True:
        try:
            opencv.waitKey(1)
            navegador.find_element_by_class_name('_2rZZg')
            time.sleep(1)
            opencv.destroyAllWindows()
            break
        except:
            time.sleep(1)
    time.sleep(5)
    buscaConversas(navegador)
    # flood(navegador)
    
def buscaConversas(navegador):
    navegador.execute_script("document.getElementById('pane-side').scroll(0,3000)")
    time.sleep(2)
    conversas = navegador.find_elements_by_class_name('_2WP9Q')
    for conversa in conversas:
        nomeChat = conversa.find_element_by_class_name("_19RFN")
        print(bcolors.WARNING + "Conversa com: " + nomeChat.text + bcolors.ENDC)
        conversa.click()
        time.sleep(3)
        for i in range(10):
            navegador.execute_script("document.getElementsByClassName('_1_keJ')[0].scroll(0,0)")
            time.sleep(0.5)
        mensagens = navegador.find_elements_by_class_name('_12pGw')
        for mensagem in mensagens:
            try:
                messageSide = mensagem.find_element_by_xpath("../../..").get_attribute('class')
                textoMensagem = mensagem.find_element_by_xpath(".//span/span").text 
                if(messageSide.split(' ')[2]) == "message-out":
                    indicador = bcolors.OKBLUE + mensagem.find_element_by_xpath("..").get_attribute('data-pre-plain-text')
                else:
                    indicador = mensagem.find_element_by_xpath("..").get_attribute('data-pre-plain-text')
                print(indicador + textoMensagem + bcolors.ENDC)
            except:
                print(bcolors.FAIL + "Mensagem inválida"+ bcolors.ENDC)

while True:
    opcaoNavegador = input("Deseja visualizar o navegador? (S/N) ")
    if opcaoNavegador.upper() == "S" or opcaoNavegador.upper() == "N":
        break
    else:
        print(bcolors.FAIL + "Opção inválida" + bcolors.ENDC)

profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
opcoes = webdriver.FirefoxOptions()
opcoes.add_argument('--user-data-dir=./User_Data')
if opcaoNavegador.upper() == "S":
    navegador = webdriver.Firefox(firefox_profile=profile)
else:
    opcoes.add_argument('-headless')
    navegador = webdriver.Firefox(options=opcoes,firefox_profile=profile)

loginWhatsapp(navegador)