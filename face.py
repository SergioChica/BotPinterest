#Librerias exportadas
from selenium import webdriver#Permite controlar un navegador web, en este caso Chrome
from selenium.webdriver.support import expected_conditions as EC#Se utiliza para condiciones de espera y para localizar elementos
from selenium.webdriver.common.by import By#Se utiliza para condiciones de espera y para localizar elementos
from selenium.webdriver.support.wait import WebDriverWait#Se utiliza para dar espera a condiciones
from selenium.webdriver.common.keys import Keys #Se utiliza para simular pulsaciones de teclas
import time#Se utiliza para tiempos y esperas entre elementos
import random

chrome_options = webdriver.ChromeOptions()#Se utiliza para configurar opciones y preferencias que afectan el comportamiento de chrome cuando se controla con selenium.
chrome_options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'#Se utiliza para tener la ubicacion de chrome (Una de las opciones y preferencias que se alteran)


driver = webdriver.Chrome(options=chrome_options)#Se utiliza para crear una instancia de chromedirver

#abrir pagina
driver.get("https://co.pinterest.com/")#Se utiliza para abrir pinterest


#Variables:
# WebDriverWait(driver, 10) = Se utiliza para dar un tiempo para continuar
# until = Se tuliza para accionar la condicion despues de cumplir con el tiempo establecido
# EC.element_to_be_clickable = Se utiliza para que en un elemento se pueda dar click
# By.CSS_SELECTOR = Se utiliza para seleccionar un elemento usando selector css
# "button[class='RCK Hsu USg adn CCY NTm KhY iyn oRi lnZ wsz YbY']" = Se utiliza indicar el elemento en css
# clear() = Se utiliza para limpiar el elemento seleccionado
# send_keys("") = Se utiliza para introducir un texto al elemento seleccionado

#Iniciar sesion
login = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='RCK Hsu USg adn CCY NTm KhY iyn oRi lnZ wsz YbY']"))).click()#Boton de iniciar sesion

#email
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='D8X Hsu tBJ dyH iFc sAJ L4E Bvi iyn H_e pBj qJc TKt LJB xD4 z-6']")))#Input para Email

#username.clear()#limpiar Email

#correo
username.send_keys("sergiochica7@gmail.com")#Introducir el Email

#password
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='D8X Hsu tBJ dyH iFc sAJ L4E Bvi iyn H_e pBj qJc TKt LJB xD4 BMi z-6']")))#Input para Password

#Contraseña
password.send_keys("hola123")#Introducir el password

time.sleep(1)#Tiempo de espera

#Iniciar sesion
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='red SignupButton active']"))).click()#Boton iniciar sesion

#Busqueda
search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='searchBoxInput']")))#Boton de busqueda

#search.clear()#limpiar Email
search.send_keys("meme")#Introducir la busqueda

search.send_keys(Keys.ENTER)#Presionar enter

time.sleep(10)#Tiempo de espera

#Imagen
img = driver.find_elements(By.CSS_SELECTOR, "div[data-grid-item='true'] a")#Buscamos las diferentes imagenes el feet

# Seleccionar imagen 
random_image = random.choice(img)#Selecciona una imagen aleatoria

#click
random_image.click()#Hacer clic en la imagen seleccionada

time.sleep(3)

#Me encanta
like = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='reaction']"))).click()#Presionar me encanta

time.sleep(10)#Tiempo de espera

#Comentario
coment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='Jea XbT jar jzS lnZ rDA ujU zI7 iyn Hsu']"))).click()#Seleccionamos comentar

#Comentario
coment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='notranslate public-DraftEditor-content']"))).send_keys("nice meme")#Agregamos comentario

time.sleep(2)#Tiempo de espera

#Publicar
publicate = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='publicar']"))).click()#Presionamos boton de publicar

time.sleep(2)#Tiempo de espera

#Opciones
options = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Más opciones']"))).click()#Boton de opciones

time.sleep(1)#Tiempo de espera

#Instalar
install = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='pin-action-dropdown-item-0']"))).click()#Boton de instalacion

time.sleep(1000)#Tiempo de espera

driver.quit()