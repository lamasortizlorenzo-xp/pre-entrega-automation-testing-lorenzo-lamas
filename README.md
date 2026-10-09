# Automatización de Pruebas Web — SauceDemo

## Descripción

Proyecto de automatización de pruebas web desarrollado con Python, Selenium WebDriver y Pytest. El objetivo es verificar funcionalidades principales del sitio de práctica SauceDemo mediante pruebas automatizadas.

## Tecnologías utilizadas

- **Python:** lenguaje utilizado para desarrollar las pruebas.
- **Selenium WebDriver:** automatización de las interacciones con el navegador.
- **Pytest:** ejecución y organización de las pruebas.
- **Pytest HTML:** generación del reporte de resultados en formato HTML.
- **Google Chrome:** navegador utilizado durante la ejecución.

## Pruebas automatizadas

El proyecto incluye tres pruebas:

1. **Inicio de sesión exitoso:** comprueba el acceso con credenciales válidas.
2. **Verificación del catálogo:** comprueba que se muestren los productos y sus precios.
3. **Interacción con el carrito:** agrega un producto y verifica que aparezca en el carrito.

## Estructura del proyecto

```text
pre-entrega-automation-testing-lorenzo-lamas-ortiz/
├── reports/
│   ├── capturas/
│   ├── ejecucion.log
│   └── reporte.html
|── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_saucedemo.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
|
├── .gitignore
├── README.md
└── requirements.txt
```

## Instalación

Se requiere tener Python y Google Chrome instalados.

Desde la carpeta principal del proyecto, instalar las dependencias con:

```bash
python -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Ejecutar todas las pruebas y generar el reporte HTML con:

```bash
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

El reporte se genera en `reports/reporte.html`.

## Evidencias y registros

- **Reporte HTML:** contiene los resultados de la ejecución de las pruebas.
- **Registro de ejecución:** `reports/ejecucion.log` registra el inicio y el resultado de las pruebas.
- **Capturas de pantalla:** se guardan automáticamente en `reports/capturas/` cuando una prueba falla y el navegador está disponible.

## Credenciales de prueba

El sitio SauceDemo proporciona estas credenciales para las pruebas:

- **Usuario:** `standard_user`
- **Contraseña:** `secret_sauce`

Sitio utilizado: https://www.saucedemo.com/

## Resultado de la última ejecución registrada

Las tres pruebas automatizadas finalizaron correctamente en la ejecución realizada durante el desarrollo.

Para comprobar los resultados más recientes, ejecutar nuevamente el comando de pruebas indicado anteriormente.