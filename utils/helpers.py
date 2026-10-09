
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def obtener_driver():
    """Inicializa y retorna el navegador Chrome."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    return driver


def login_saucedemo(driver, usuario, password):
    """Realiza el login en SauceDemo."""
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    user_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    pass_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")

    user_input.send_keys(usuario)
    pass_input.send_keys(password)
    login_btn.click()
