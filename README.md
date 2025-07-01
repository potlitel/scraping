# Web Scraping con Scrapy

Repositorio para la extracción automatizada de datos web utilizando el framework Scrapy en Python.

## 🚦Descripción

Este proyecto implementa un scraper basado en Scrapy, un framework potente y flexible para la recolección de datos estructurados desde sitios web. El objetivo es automatizar la extracción de información relevante para análisis, almacenamiento o procesamiento posterior

## 🔥Características

- Extracción eficiente de datos estructurados.
- Soporte para paginación automática.
- Exportación de resultados a formatos como CSV o JSON.
- Fácil configuración y extensión mediante spiders personalizados

## 💥Requisitos
- Python 3.9+
- Scrapy (instalable vía pip)

## 👉 Instalación
1- Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```
2- (Opcional) Crea y activa un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
3- Instala las dependencias:
```bash
pip install scrapy
```

## 🕷️ Ejemplo de Spider

```python
import scrapy

class MiSpider(scrapy.Spider):
    name = "ejemplo"
    start_urls = ['https://ejemplo.com/']

    def parse(self, response):
        for elemento in response.css('selector_elemento'):
            yield {
                'titulo': elemento.css('selector_titulo::text').get(),
                'precio': elemento.css('selector_precio::text').get(),
            }
        siguiente_pagina = response.css('a.siguiente::attr(href)').get()
        if siguiente_pagina:
            yield response.follow(siguiente_pagina, callback=self.parse)

```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, revisa el archivo `CONTRIBUTING.md` para conocer las reglas y el proceso para enviar pull requests[2][5].

## 🏃 Roadmap

- Añadir más spiders.
- Incluir endpoints que muestren la info extraída y almacenada en postgres sql.
- Crear una interfaz web para visualización de tableros con inteligencia de negocios que potencien la toma de desiciones.

## ✒️ Autores y Créditos

- **potlitel** - Trabajo inicial y mantenimiento
- Consulta la lista de [colaboradores](https://github.com/potlitel/scraping/graphs/contributors) que han participado en este proyecto.

```bash

CREATE TABLE IF NOT EXISTS cubadebate_news (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    url TEXT,
    tags VARCHAR(255),
    image_text VARCHAR(255),
    shore_text TEXT
	);

```


## Output

#### This is an example of an output segment from the scraping process.

```bash
...
{
'title': 'Portugal se impone en penales a España y es el campeón de la UEFA Nations League', 
'url': 'http://www.cubadebate.cu/noticias/2025/06/08/portugal-se-impone-en-penales-a-espana-y-es-el-campeon-de-la-uefa-nations-league/', 
'tags': ['Noticias', 'Deportes'], 
'image_text': 'http://media.cubadebate.cu/wp-content/uploads/2025/06/Portugal-UEFA-Nations-League-150x125.jpg', 
'shore_text': 'Nuevamente Múnich fue el escenario para erigir un campeón. Si hace días fue el PSG, en la Champions League, ahora fue el turno para\xa0Portugal. La cuarta edición de la UEFA Nations League fue para los lusos. El combinado que dirige Roberto Martínez superó en la gran definición a España en tanda de penales. Francia se impuso a Alemania por el tercer puesto.'
}
...

```
