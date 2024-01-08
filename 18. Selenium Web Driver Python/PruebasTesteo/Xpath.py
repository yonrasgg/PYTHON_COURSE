from selenium import webdriver 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# Configuración de las opciones de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Ruta a tu instalación de Chrome
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Deshabilitar las notificaciones
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Configuración del servicio del controlador de Chrome
executable_path = "Drivers/chromedriver.exe"

# Iniciar el navegador Chrome con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# Abrir el sitio web y realizar el inicio de sesión
driver.get("https://www.facebook.com/")

user = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@name='email']")))
user.send_keys("tu_email@gmail.com") # Ruta a tu instalación de Chrome colocar tu email

password = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@name='pass']")))
password.send_keys("tu_password") # Ruta a tu instalación de Chrome colocar tu password

button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@name='login']"))).click()

time.sleep(1000)
driver.quit()
