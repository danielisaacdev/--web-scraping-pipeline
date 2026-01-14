Web Scraping & Data Automation Mini Project
Overview

This project showcases a simple, production-ready web scraping and data processing pipeline using Python.
Public data is collected, cleaned, normalized, and exported into a CSV file optimized for spreadsheets and automation workflows.

The goal is to demonstrate clean data handling, structure, and real-world usability.

Tech Stack

Python 3

Requests

BeautifulSoup (lxml)

Pandas

How It Works

Scrapes structured data from a public website

Cleans and normalizes text fields

Structures the data into a tabular format

Exports a clean CSV file ready for further use

Output

The generated CSV contains:

id

quote

author

tags (pipe-separated)

The file is formatted and encoded for maximum compatibility with Excel and CRM systems.

How to Run
pip install -r requirements.txt
python scraper.py

Data Ethics

Uses only publicly available data

No authentication or private information

Intended for educational and demonstration purposes

Mini-proyecto de Web Scraping y Automatización de Datos
Descripción

Este proyecto demuestra un flujo simple y listo para uso real de scraping, limpieza y exportación de datos en Python.
Los datos públicos se recopilan, normalizan y exportan a un CSV compatible con Excel y flujos de automatización.

Tecnologías

Python 3

Requests

BeautifulSoup (lxml)

Pandas

Flujo de trabajo

Extracción de datos desde un sitio público

Limpieza y normalización del texto

Estructuración tabular

Exportación a CSV

Resultado

Archivo CSV con:

id

quote

author

tags

Preparado para hojas de cálculo y sistemas externos.

Ejecución
pip install -r requirements.txt
python scraper.py

Ética

Uso exclusivo de datos públicos

Proyecto demostrativo y educativo