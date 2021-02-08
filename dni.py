from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from colorama import Fore, init
import sys
import time
init()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(chrome_options=chrome_options)
os.system("cls")
#driver = webdriver.Chrome()
#driverdni = webdriver.Chrome()



urlname = "https://eldni.com/index.php/pe/buscar-por-nombres"






def text(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def home():
    os.system("cls")
    print(Fore.YELLOW+"Bienvenido al programa de WebScraping, automatizamos el uso de herramientas para mejorar vidas y notas\n"+Fore.RESET)

    names()
    
    



def dni():
    #urldni = "https://eldni.com/index.php/pe/buscar-por-dni"
    #driverdni.get(urldni)
    #coord = driverdni.find_element_by_xpath("//button")
    #coord.click()
#################################################################
#POR DNI
    dni = driverdni.find_element_by_id("dni")
    dnisend = input("Ingrese DNI: ")
    dni.send_keys(dnisend)
    datos = driver.find_element_by_link_text("Buscar nombres")
    datos.click()
    body = driver.find_element_by_xpath("/html/body/div/table/tbody/tr")
    tr = body.find_element_by_xpath("./*/th")
    print(tr.text)
##############################################################3###
#POR NOMBRES
def names():
    driver.get(urlname)
    name = driver.find_element_by_id("nombres")
    apellido_p = driver.find_element_by_id("apellido_p")
    apellido_m = driver.find_element_by_id("apellido_m")

    nameSend = input("Ingrese solo nombres(maria alejandra):")
    apellidoPSend = input("Ingrese Apellido Paterno: ")
    apellidoMSend = input("Ingrese Apellido Materno: ")

    name.send_keys(nameSend)
    apellido_p.send_keys(apellidoPSend)
    apellido_m.send_keys(apellidoMSend)

    dat = driver.find_element_by_tag_name("button")
    dat.click()
    id = "column-center"
    table = driver.find_element_by_id(id)
    tr = table.find_element_by_xpath("//thead")
    td = table.find_element_by_xpath("//tbody")
    
    print ("\n"+Fore.YELLOW+str(tr.text)+Fore.RESET)
    print (Fore.RED+str(td.text+Fore.RESET+"\n"))
    
    names()


home()

#classe = driver.find_elemet_by_class_name("table table-striped table-scroll")
#print(classe.text)