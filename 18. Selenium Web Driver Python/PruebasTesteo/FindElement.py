from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

executable_path="Drivers\chromedriver.exe"

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

email = driver.find_element(By.NAME, 'email')
passw = driver.find_element(By.NAME, 'pass')

email.send_keys('tu_correo@gmail.com')
passw.send_keys('tu_contraseña')

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']"))).click()

time.sleep(1000)
driver.quit()