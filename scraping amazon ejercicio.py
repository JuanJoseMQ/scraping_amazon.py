# Importamos paquetes
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

# Definimos que queremos buscar
busqueda1 = 'iphone 13'

# Activamos el navegador y accedemos a la web de amazon
browser = webdriver.Chrome()
browser.get("https://www.amazon.es")

# Pulsamos en aceptar cookies
time.sleep(1)
boton = browser.find_element(by=By.XPATH, value=('//*[@id="sp-cc-accept"]'))
boton.click()

# Procedemos a nuestra primera busqueda (iphone 13)
barra_busqueda = browser.find_element(by=By.XPATH, value='//*[@id="twotabsearchtextbox"]').send_keys(busqueda1 + Keys.ENTER)
time.sleep(1)

def extraer_url():
    try:
        num_page = browser.find_element(By.XPATH, value="//*[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div[58]/div/div/span/span[4]")
    except NoSuchElementException:
        num_page = browser.find_element(By.CLASS_NAME, value='a-last').click()
    browser.implicitly_wait(3)
    url_list = []
    for i in range(int(num_page.text)):
        page_ = i + 1
        url_list.append(browser.current_url)

        browser.implicitly_wait(4)
        click_next = browser.find_element(By.CLASS_NAME, value='a-last').click()
        print("Page " + str(page_) + " grabbed")

    browser.quit()
    return url_list

def extraer_informacion():
    paginas = extraer_url()

    browser = webdriver.Chrome()

    for pagina in paginas:

        time.sleep(2)
        #boton = browser.find_element(by=By.XPATH, value=('//*[@id="sp-cc-accept"]'))
        #boton.click()
        browser.get(pagina)
        panel = browser.find_element(by=By.CLASS_NAME, value="s-main-slot s-result-list s-search-results sg-row".replace(" ", "."))
        moviles = panel.find_elements(by=By.XPATH, value="//div[@data-component-type='s-search-result']")

        for movil in moviles:

            titulo = movil.find_element(by=By.TAG_NAME, value="H2")
            imagen = movil.find_element(by=By.CLASS_NAME, value="s-image".replace(" ", ".")).get_attribute("src")
            try:
                precio = movil.find_element(by=By.CLASS_NAME, value="a-price-whole")
            except:
                pass
            link = movil.find_element(by=By.CLASS_NAME, value= "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal".replace(" ",".")).get_attribute("href")

            print(titulo.text)
            print(imagen)
            print(precio.text)
            print(link)

        print('Fin pagina' + pagina)
        print('--------------------')
    browser.quit()
extraer_informacion()




