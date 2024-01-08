from selenium import webdriver #Importamos la libreria de Selenium
from selenium.webdriver.support import expected_conditions as EC #Importamos la libreria de Selenium
from selenium.webdriver.common.by import By  #Importamos la libreria de Selenium
from selenium.webdriver.support.ui import WebDriverWait #Importamos la libreria de Selenium
import time

#Quitar notificaciones de Chrome    
options = webdriver.ChromeOptions() #Creamos una variable para las opciones
options.add_argument("start-maximized") #Maximizar la ventana
options.add_experimental_option("excludeSwitches", ["enable-automation"]) #Quitar notificaciones de Chrome  
options.add_experimental_option('useAutomationExtension', False) #Quitar notificaciones de Chrome
options.add_argument("--disable-blink-features=AutomationControlled") #Quitar notificaciones de Chrome
options.add_argument("--disable-notifications") #Quitar notificaciones de Chrome

# Path del driver de Chrome
executable_path="Drivers\chromedriver.exe"  

# Abrimos la página de Facebook
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")

# Enlace de recuperar contraseña
link_recov_pass = driver.find_element(By.PARTIAL_LINK_TEXT, 'Forgot password?')
link_recov_pass.click()

time.sleep(1000) # Tiempo de espera para ver el resultado

driver.quit() # Cerrar el navegador