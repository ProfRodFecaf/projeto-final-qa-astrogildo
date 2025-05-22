# Instalar o Selenium e outras dependências
!pip install selenium
!apt-get update
!apt install -y wget unzip

# Baixar e configurar o ChromeDriver
!wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
!unzip chromedriver_linux64.zip
!mv chromedriver /usr/bin/chromedriver
!chown root:root /usr/bin/chromedriver
!chmod +x /usr/bin/chromedriver

# Instalar o Chrome
!apt-get install -y chromium-browser

# Configurar as opções do Chrome para rodar em modo headless
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Inicializar o WebDriver
driver = webdriver.Chrome('chromedriver', options=chrome_options)

# Abrir a página da calculadora (substitua pela URL da sua calculadora)
driver.get("http://www.calculator.com")

# Encontrar os elementos da calculadora
input_field = driver.find_element_by_name("input")  # Substitua pelo seletor correto
button_7 = driver.find_element_by_xpath("//button[contains(.,'7')]")  # Substitua pelo seletor correto
button_plus = driver.find_element_by_xpath("//button[contains(.,'+')]")  # Substitua pelo seletor correto
button_3 = driver.find_element_by_xpath("//button[contains(.,'3')]")  # Substitua pelo seletor correto
button_equals = driver.find_element_by_xpath("//button[contains(.,'=')]")  # Substitua pelo seletor correto

# Realizar uma operação simples (7 + 3)
button_7.click()
button_plus.click()
button_3.click()
button_equals.click()

# Verificar o resultado
result = input_field.get_attribute("value")
assert result == "10", f"Resultado esperado: 10, Resultado obtido: {result}"

# Fechar o navegador
driver.quit()

