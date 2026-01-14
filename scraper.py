import requests
import pandas as pd
from bs4 import BeautifulSoup
import html

URL = "https://quotes.toscrape.com"

def clean_text(text: str) -> str:
    """
    Limpia texto para CSV profesional:
    - Decodifica entidades HTML
    - Normaliza comillas
    - Elimina saltos de línea
    - Elimina espacios extra
    """
    if not text:
        return ""

    # Decodifica entidades HTML (&ldquo; etc.)
    text = html.unescape(text)

    # Normaliza comillas “ ” ‘ ’
    replacements = {
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)

    # Elimina saltos de línea y tabs
    text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")

    # Espacios múltiples → uno solo
    text = " ".join(text.split())

    return text.strip()


def scrape_quotes():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    rows = []
    quote_id = 1

    for block in soup.select(".quote"):
        quote = clean_text(block.select_one(".text").get_text())
        author = clean_text(block.select_one(".author").get_text())
        tags = block.select(".tags a.tag")
        tags_clean = "|".join(clean_text(tag.get_text()) for tag in tags)

        rows.append({
            "id": quote_id,
            "quote": quote,
            "author": author,
            "tags": tags_clean
        })
        quote_id += 1

    return pd.DataFrame(rows)


def main():
    df = scrape_quotes()

    df.to_csv(
        "quotes_clean.csv",
        index=False,
        sep=";",                 # compatible con Excel LATAM
        encoding="utf-8-sig",    # evita â€œ AndrÃ© etc.
        quoting=1                # QUOTE_ALL → evita filas rotas
    )

    print("✔ CSV generado correctamente: quotes_clean.csv")


if __name__ == "__main__":
    main()
