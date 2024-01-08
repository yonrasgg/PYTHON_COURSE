from selenium import webdriver

# Configuración de las opciones del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("executable_path=Drivers/chromedriver.exe")  # Ruta al controlador de Chrome

# Crear una instancia del navegador Chrome con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Abrir la página de Facebook
driver.get("https://www.facebook.com/")

# Cerrar el navegador
driver.quit()
