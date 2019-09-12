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
    time.sleep(10)
    navegador.save_screenshot('qrcode.png')
    image = opencv.imread('qrcode.png')
    time.sleep(2)
    opencv.imshow('QR Code (Pressione qualquer tecla quando tiver escaneado)',image)
    time.sleep(2)
    while True:
        try:
            navegador.find_element_by_class_name('_2rZZg')
            time.sleep(2)
            opencv.waitKey(0)
            opencv.destroyAllWindows()
            break
        except:
            print("Não aberto")
            time.sleep(5)
    time.sleep(10)
    buscaConversas(navegador)
    # flood(navegador)
    # pegaCookies(navegador)
    
def buscaConversas(navegador):
    conversas = navegador.find_elements_by_class_name('_2WP9Q')
    for conversa in conversas:
        conversa.click()
        time.sleep(2)
        mensagens = navegador.find_elements_by_class_name('_12pGw')
        for mensagem in mensagens:
            try:
                messageSide = mensagem.find_element_by_xpath("../../..").get_attribute('class')
                textoMensagem = mensagem.find_element_by_xpath(".//span/span").text 
                if(messageSide.split(' ')[2]) == "message-out":
                    indicador = bcolors.OKBLUE + "Você: "
                else:
                    indicador = bcolors.OKGREEN + "Pessoa: "
                print(indicador + textoMensagem + bcolors.ENDC)
            except:
                print("Mensagem inválida")

def pegaCookies(navegador):
    print(navegador.get_cookies())

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