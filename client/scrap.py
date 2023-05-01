from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json

def extract_data_from_amazon(link):
    chrome_options = Options()
    driver = webdriver.Chrome("chromedriver.exe"
                              ,options=chrome_options)
    driver.get(link)
    wait = WebDriverWait(driver, 15)
    titulo = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text
    import time
    #time.sleep(5)
    subtitulo = wait.until(EC.presence_of_element_located((By.ID, "productSubtitle"))).text
    preco = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'price')]"))).text
    
    ul_element = wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"]')))
    book_details = ul_element.text.splitlines()
    isbn_13 = None
    for detail in book_details:
        if "ISBN-13" in detail:
            isbn_13 = detail.split(" : ")[1]
            break
    print(isbn_13)
    
    end_img = wait.until(EC.visibility_of_element_located((By.ID, "imgBlkFront"))).get_attribute("src")


    data = [titulo, subtitulo, isbn_13, end_img, preco]
    print(data)
    driver.quit()
    return data

def extract_data_from_mundosInfinitos(link):
    import re
    chrome_options = Options()
    driver = webdriver.Chrome("chromedriver.exe"
                              ,options=chrome_options)
    driver.get(link)
    wait = WebDriverWait(driver, 5)
    try:
        # carregue os cookies salvos anteriormente
        import pickle
        with open('cookies.pkl', 'rb') as f:
            cookies = pickle.load(f)

        # adicione os cookies à sessão atual do driver
        for cookie in cookies:
            driver.add_cookie(cookie)
    except:
        pass
    try:
        # Espera até que o botão "Aceitar cookies" esteja visível
        cookies_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-politicas botaoespaco')))
        cookies_button.click()
    except:
        # Se o botão não for encontrado, continue sem clicar nele
        pass
    titulo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "titulo-produto"))).text
    subtitulo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "subtitulo"))).text
    try:
        preco = wait.until(EC.presence_of_element_located((By.ID, "preco-por-html"))).text
    except:
        preco = wait.until(EC.presence_of_element_located((By.ID, "preco-capa-html"))).text

    isbn13 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapseOne"]/div/ul/li[5]'))).text
    padrao = r'ISBN:\s*(\d+[-\d]*)'
    print(isbn13)
    isbn_match = re.search(padrao, isbn13)
    if isbn_match:
        isbn = isbn_match.group(1)
        # Remover os hífens da string do ISBN
        isbn = isbn.replace('-', '')
    else:
        isbn = None

    end_img = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="galeria-carousel"]/div[1]/div/div[1]/div/img'))).get_attribute("src")

    data = [titulo, subtitulo, isbn, end_img, preco]
    print(data)
    return data
