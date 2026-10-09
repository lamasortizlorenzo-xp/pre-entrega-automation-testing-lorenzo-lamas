# Automatización de Pruebas Web - SauceDemo

## Descripción
Proyecto de automatización de pruebas web desarrollado con Python, Selenium WebDriver y Pytest sobre el sitio SauceDemo.

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML

## Pruebas automatizadas

1. **Login exitoso:** se verifica que el usuario pueda iniciar sesión con datos válidos.
2. **Verificación del catálogo:** comprueba que se muestren los productos y sus precios.
3. **Interacción con el carrito:** agrega un producto y verifica que aparezca correctamente en el carrito.

## Estructura del proyecto

```text
pre-entrega-automation-testing/
│
├── reports/
│   └── reporte.html
├── tests/
│   ├── __init__.py
│   └── test_saucedemo.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Instalación

Instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

Ejecutar desde la carpeta principal del proyecto:

```bash
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

## Datos de prueba

- Usuario: `standard_user`
- Contraseña: `secret_sauce`

## Resultado

Las tres pruebas automatizadas se ejecutaron correctamente: inicio de sesión, verificación del catálogo e interacción con el carrito.