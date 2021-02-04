from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(chrome_options=chrome_options)

#driver = webdriver.Chrome()

urldni = "https://eldni.com/index.php/pe/buscar-por-dni"
urlname = "https://eldni.com/index.php/pe/buscar-por-nombres"



driver.get(urlname)

#coord = driver.find_element_by_link_text("Buscar por DNI")
#coord.click()
#################################################################
#POR DNI
#dni = driver.find_element_by_id("dni")
#dnisend = "73800375"
#dni.send_keys(dnisend)
#datos = driver.find_element_by_id("buscar-por-dni")
#datos.click()
##############################################################3###
#POR NOMBRES

name = driver.find_element_by_id("nombres")
apellido_p = driver.find_element_by_id("apellido_p")
apellido_m = driver.find_element_by_id("apellido_m")

nameSend = "Juan Rojer"
apellidoPSend = "Roque"
apellidoMSend = "Rojas"

name.send_keys(nameSend)
apellido_p.send_keys(apellidoPSend)
apellido_m.send_keys(apellidoMSend)

dat = driver.find_element_by_tag_name("button")
dat.click()

#body = driver.find_element_by_xpath("/html/body/div/table/tbody/tr")
#tr = body.find_element_by_xpath("./*/th")
#print(tr.text)

id = "column-center"
table = driver.find_element_by_id(id)
tr = table.find_element_by_xpath("//thead")
td = table.find_element_by_xpath("//tbody")
os.system("cls")
print (tr.text)
print (td.text)

#classe = driver.find_elemet_by_class_name("table table-striped table-scroll")
#print(classe.text)