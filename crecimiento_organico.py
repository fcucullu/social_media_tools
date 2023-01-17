# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:00:27 2022

@author: eugef
"""


# import module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
  


#################################################
# Inputs
usuario = 'stificrew'
contraseña = 'Stifins'
cuenta_objetivo = 'yisucrist'
num_cuentas_a_seguir = 50

# Funciones
def entrar_insta(usuario, contraseña):
    # Abrimos la pagiina web de intagram
    driver = webdriver.Chrome(r"./driver/chromedriver")
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    time.sleep(2)
    # aceptamos las cookies
    driver.find_element("xpath", '//div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
    time.sleep(2)
    # nos logueamos
    driver.find_element("xpath", '//div/div[1]/div/label/input').send_keys(usuario)
    driver.find_element("xpath", '//div/div[2]/div/label/input').send_keys(contraseña)
    time.sleep(2)
    driver.find_element("xpath", '//div/div[3]/button/div').click()
    time.sleep(10)
    
    # pinchamos en que no guarde la info
    driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
    time.sleep(2)
    
    # pinchamos en que no mande notificaciones
    driver.find_element("xpath", '//div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(2)
    
    return driver
    
    

# le damos a seguira 50
# creamos una función que abra el instagram del publico objetivo, vaya pinchando en los seguidores, y siguiendo
# uno a uno, teniendo que volver continuamente a la cuenta del publico objetivo
# nota, comprobar si ya seguimos a la cuenta
def seguir_cuentas(cuenta_objetivo, numero_cuenta, driver):
    #vamos al buscador
    try :
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div').click()
        time.sleep(5)
        print('pimchamos buscador')
    
    except:
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div').click()
        print('pimchamos buscador')

    # escribimos la cuenta de nuestro publico objetivo
    try:
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys(cuenta_objetivo)
        time.sleep(2)        
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys(Keys.RETURN)
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys(Keys.RETURN)
        time.sleep(2)
        print('escribimos cuenta de publico objetivo')
    except:
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys(cuenta_objetivo)
        time.sleep(2)
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys(Keys.RETURN)
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys(Keys.RETURN)
        time.sleep(2)
        print('escribimos cuenta de publico objetivo')

    # Pinchamos en el boton de seguidores
    driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div').click()
    time.sleep(5)
    print('Pinchamos en el boton de seguidores')
    # vamos a la cuenta
    try:
        driver.find_element("xpath", '//div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div['+str(numero_cuenta)+']/div[1]/div/div/a/img').click()
        time.sleep(5)
        print('vamos a la cuenta')
    except:
        driver.find_element("xpath", '//div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div['+str(numero_cuenta)+']/div[1]/div/div/span/img').click()
        time.sleep(5)
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/header/div[2]/div[1]/div/a/img').click()
        time.sleep(5)
        print('vamos a la cuenta')


    #comprobamos si la seguimos
    if driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').text == 'Seguir':
        driver.find_element("xpath", '//div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()
        time.sleep(5)
        print('comprobamos si seguimos la cuenta')
        return 1
    else:
        return 0
        


driver = entrar_insta(usuario, contraseña)
j = 0
i = 1
#while j < num_cuentas_a_seguir:
while j < 5:
    j += seguir_cuentas(cuenta_objetivo, i, driver)
    i += 1


def completo(usuario, contraseña,cuenta_objetivo):
    driver = entrar_insta(usuario, contraseña)
    j = 0
    i = 1
    #while j < num_cuentas_a_seguir:
    while j < 5:
        j += seguir_cuentas(cuenta_objetivo, i, driver)
        i += 1

completo(usuario, contraseña,cuenta_objetivo)

entrar_insta(usuario, contraseña)
# creamos un bucle para que siga a 50 cuentas
j = 0
i = 1
#while j < num_cuentas_a_seguir:
while j < 5:
    try:
        j += seguir_cuentas(cuenta_objetivo, i)
        i += 1
    except:
        pass




