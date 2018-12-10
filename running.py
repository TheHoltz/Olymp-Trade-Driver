from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from db import *

driver = webdriver.Chrome()
driver.maximize_window()

def digitar(elemento, string):
    driver.find_element_by_xpath(elemento).send_keys(Keys.CONTROL + "a");
    return(driver.find_element_by_xpath(elemento).send_keys(string))

def click(elemento):
    return(driver.find_element_by_xpath(elemento).click())

def clickwait(elemento):
    time.sleep(.7)
    return(driver.find_element_by_xpath(elemento).click())

def goto(elemento):
    return(driver.get(elemento))

def login():
    return(goto('https://olymptrade.com/home'))

def changeCurrency(curr):
    click('//*[@id="pair-managing-add-btn"]')
    click(btn_db[curr])
    click('//*[@id="page-container"]/div/div[1]/div[6]/div/div[2]/div[3]/div[1]/div/header/label')
    click('//*[@id="page-container"]/div/div[1]/div[6]/div/div[2]/div[3]/div[1]/div/header/label')
    click('//*[@id="page-container"]/div/div[1]/div[6]/div/div[2]/div[1]/button')

def buy(value):
    digitar('//*[@id="opcion"]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/input',
    value)
    click('//*[@id="opcion"]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/button')

def sell(value):
    digitar('//*[@id="opcion"]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/input',
    value)
    click('//*[@id="opcion"]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button')

def changeTime(time):
    click('//*[@id="opcion"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[1]')
    click(time_db[time])

def changeGraph(type):
    click('//*[@id="opcion"]/div[1]/div[2]/div[2]/div/div[1]/ul/li[3]/div/div/div[1]')
    click(graph_type_db[type])



# d9b480aa12@mailox.fun
login()
while(1):
    entrada = input("Insira um comando:")
    entrada = entrada.split(" ")
    try:
        eval(entrada[0]+'("'+str(entrada[1])+'")')
    except:
        print("Caro usuário, houve um erro ao processar o comando. Tente novamente.")
