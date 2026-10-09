

from pathlib import Path
import logging
import re

import pytest


# Carpetas de evidencias
REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "capturas"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

# Configuración del archivo de logs
LOG_FILE = REPORTS_DIR / "ejecucion.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def registrar_inicio(request):
    """Registra el inicio de cada prueba."""
    logger.info("INICIO: %s", request.node.nodeid)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Registra el resultado y captura la pantalla si falla la prueba."""
    outcome = yield
    report = outcome.get_result()

    # Solo procesamos el resultado de la ejecución de la prueba.
    if report.when != "call":
        return

    if report.passed:
        logger.info("RESULTADO: %s", item.nodeid)
        return

    if report.failed:
        logger.error("FALLO: %s", item.nodeid)

        # Recuperamos el navegador mientras la prueba todavía se ejecuta.
        driver = item.funcargs.get("setup")

        if driver is None:
            logger.warning(
                "No se encontró el navegador para capturar la pantalla."
            )
            return

        nombre = re.sub(r"[^A-Za-z0-9_.-]", "_", item.name)
        ruta = SCREENSHOTS_DIR / f"{nombre}.png"

        try:
            guardada = driver.save_screenshot(str(ruta))

            if guardada and ruta.exists():
                logger.info("CAPTURA GUARDADA: %s", ruta)
            else:
                logger.warning("No se pudo guardar la captura.")
        except Exception:
            logger.exception("Error al guardar la captura.")
