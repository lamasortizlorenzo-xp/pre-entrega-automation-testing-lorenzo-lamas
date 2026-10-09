
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import obtener_driver, login_saucedemo


@pytest.fixture
def setup():
    """Inicia el navegador y lo cierra al finalizar cada prueba."""
    driver = obtener_driver()
    yield driver
    driver.quit()


def test_login_exitoso(setup):
    """Prueba 1: Login con credenciales válidas."""
    driver = setup
    login_saucedemo(driver, "standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)

    assert "inventory.html" in driver.current_url

    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    ).text

    assert titulo == "Products"


def test_verificacion_catalogo(setup):
    """Prueba 2: Verificación del catálogo de productos."""
    driver = setup
    login_saucedemo(driver, "standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)

    productos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    assert len(productos) > 0

    primer_nombre = driver.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    primer_precio = driver.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    print(
        f"\n[INFO] Primer producto: {primer_nombre} "
        f"| Precio: {primer_precio}"
    )

    assert primer_nombre != ""
    assert primer_precio != ""


def test_interaccion_carrito(setup):
    """Prueba 3: Agregar un producto y verificar el carrito."""
    driver = setup
    login_saucedemo(driver, "standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)

    boton_agregar = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//button[text()='Add to cart'])[1]")
        )
    )
    boton_agregar.click()

    contador_badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    ).text

    assert contador_badge == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    items_carrito = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    assert len(items_carrito) == 1



