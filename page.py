from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ajuste o caminho para o chromedriver conforme sua instalação
CHROMEDRIVER_PATH = '/path/to/chromedriver'
SITE_PATH = 'file:/AtividadesFaculdade/index.html'

# Configura o driver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

try:
    # Abre a página HTML
    driver.get(SITE_PATH)

    # Localiza campos do formulário
    nome_input = driver.find_element(By.ID, 'name')
    email_input = driver.find_element(By.ID, 'email')
    message_input = driver.find_element(By.ID, 'message')
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')

    # Preenche o formulário
    nome_input.send_keys('João Silva')
    email_input.send_keys('joao.silva@gmail.com')
    message_input.send_keys('Esta é uma mensagem de teste.')

    # Envia o formulário
    submit_btn.click()

    # Aguarda resultado
    wait = WebDriverWait(driver, 5)
    result_div = wait.until(
        EC.text_to_be_present_in_element((By.ID, 'result'), 'Obrigado,')
    )

    # Verifica o texto de confirmação
    result_text = driver.find_element(By.ID, 'result').text
    assert 'Obrigado, João Silva!' in result_text
    print('Teste passou: mensagem de confirmação detectada.')

finally:
    time.sleep(2)
    driver.quit()
