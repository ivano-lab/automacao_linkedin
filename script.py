from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar o WebDriver
driver_path = 'caminho/para/o/chromedriver'
driver = webdriver.Chrome(driver_path)

# Função para procurar vagas e aplicar
def procurar_vagas(url, keywords):
    driver.get(url)

    try:
        # Esperar o campo de busca estar disponível e procurar por palavras-chave
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'search'))
        )
        search_box.send_keys(keywords)
        search_box.send_keys(Keys.RETURN)

        # Esperar os resultados da busca
        job_listings = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-listing-class'))
        )

        for job in job_listings:
            try:
                # Verificar se a vaga tem candidatura simplificada
                if "Candidatura Simplificada" in job.text:
                    job.click()
                    apply_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, 'apply-button-class'))
                    )
                    apply_button.click()
                    # Preencher o formulário de candidatura, se necessário
                    # ...
                    print(f'Aplicado para a vaga: {job.text}')
                driver.back()
            except Exception as e:
                print(f'Erro ao tentar aplicar para a vaga: {e}')
                driver.back()
    except Exception as e:
        print(f'Erro ao procurar vagas: {e}')
    finally:
        driver.quit()

# URL do site de busca de vagas
url = 'https://www.exemplo.com/vagas'
keywords = 'Desenvolvedor Python'

procurar_vagas(url, keywords)
