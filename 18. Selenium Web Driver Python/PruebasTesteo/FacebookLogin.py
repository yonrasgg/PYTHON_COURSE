from selenium import webdriver #Importamos la libreria de Selenium
from selenium.webdriver.support import expected_conditions as EC #Importamos la libreria de Selenium
from selenium.webdriver.common.by import By  #Importamos la libreria de Selenium
from selenium.webdriver.support.ui import WebDriverWait #Importamos la libreria de Selenium
import time

options = webdriver.ChromeOptions() #Creamos una variable para las opciones
options.add_argument("start-maximized") #Maximizar la ventana
options.add_experimental_option("excludeSwitches", ["enable-automation"]) #Quitar notificaciones de Chrome  
options.add_experimental_option('useAutomationExtension', False) #Quitar notificaciones de Chrome
options.add_argument("--disable-blink-features=AutomationControlled") #Quitar notificaciones de Chrome
options.add_argument("--disable-notifications") #Quitar notificaciones de Chrome

# Path del driver de Chrome
executable_path="Drivers\chromedriver.exe"  

# Abrimmos la pagina de Facebook    
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")

#Inicio de sesion
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
username.clear() #Limpiamos el campo de usuario
password.clear() #Limpiamos el campo de contraseña
username.send_keys("tu_email@gmail.com") #Escribimos el usuario
password.send_keys("tu_contraseña") #Escribimos la contraseña

#Click en el boton de login
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']"))).click()

time.sleep(1000) #Tiempo de espera para ver el resultado

driver.quit() #Cerrar el navegador 

print("Prueba finalizada") #Mensaje de finalizacion de la prueba
