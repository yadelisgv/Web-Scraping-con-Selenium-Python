# Web-Scraping-con-Selenium-Python

Este proyecto es un web scraper que extrae información de los inmuebles en venta de la página web de Idealista para los municipios de Málaga. Utiliza Python, Flask, Selenium, y Beautiful Soup para automatizar la navegación por la página web y extraer los datos relevantes.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación utilizado para desarrollar la lógica del scraper.
- **Flask**: Framework de Python utilizado para crear la aplicación web.
- **Selenium**: Herramienta utilizada para automatizar la navegación web y la interacción con la página de Idealista.
- **Beautiful Soup**: Biblioteca de Python utilizada para analizar y extraer datos de páginas web.
- **Undetected Chromedriver**: Librería para usar el controlador de Chrome sin ser detectado.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

- **Web-Scraping-con-Selenium-Python**: Carpeta principal del proyecto.
  - **app.py**: Código de la aplicación Flask que maneja las rutas y la lógica del scraper.
  - **templates**: Carpeta que contiene los archivos HTML para la interfaz web.
    - **index.html**: Interfaz web donde se muestra el menú desplegable y la tabla con los datos de los inmuebles.
  - **static**: Carpeta opcional que podría contener archivos estáticos como CSS o JavaScript.

## Uso

1. Clona este repositorio en tu máquina local.
2. Navega hasta el directorio del proyecto.
3. Instala las dependencias del proyecto ejecutando `pip install -r requirements.txt`.
4. Ejecuta la aplicación utilizando el comando `python app.py`.
5. Abre un navegador web y navega a `http://localhost:5000` para interactuar con la aplicación.

## Funcionalidades

- Permite seleccionar un municipio de Málaga desde un menú desplegable en una interfaz web.
- ![1](https://github.com/yadelisgv/Web-Scraping-con-Selenium-Python/assets/40398052/1b599202-8d11-4ac7-b093-4a64a0bf09fb)

- Abre una ventana de Google Chrome de forma automática para navegar por la página de Idealista correspondiente al municipio seleccionado.
- ![2](https://github.com/yadelisgv/Web-Scraping-con-Selenium-Python/assets/40398052/e02fe86c-c19e-4ec4-a3bb-6c6ec21e7759)

- Extrae información detallada de los primeros 6 inmuebles en venta, incluyendo título, ubicación, precio, características básicas, características adicionales y ubicación detallada.
- Muestra los datos extraídos en una tabla en la interfaz web.
- ![4](https://github.com/yadelisgv/Web-Scraping-con-Selenium-Python/assets/40398052/ae5c97d6-1d4d-47c7-b31f-8b3d652ab53c)
