from core.scraper.base import BaseScraper
from core.storage.database import CSVStorage
from bs4 import BeautifulSoup
import pandas as pd
import html

class QuotesScraper(BaseScraper):
    def __init__(self):
        super().__init__(name="QuotesScraperService")
        self.base_url = "https://quotes.toscrape.com"
        self.storage = CSVStorage()

    def clean_text(self, text: str) -> str:
        if not text: return ""
        text = html.unescape(text)
        return " ".join(text.split()).strip()

    def parse(self, html_content: str):
        soup = BeautifulSoup(html_content, "lxml")
        rows = []
        for block in soup.select(".quote"):
            rows.append({
                "quote": self.clean_text(block.select_one(".text").get_text()),
                "author": self.clean_text(block.select_one(".author").get_text()),
                "tags": "|".join(self.clean_text(tag.get_text()) for tag in block.select(".tags a.tag"))
            })
        return rows

    def run(self):
        self.logger.info("Starting Quotes Scraper Job")
        response = self.fetch(self.base_url)
        
        if response:
            data = self.parse(response.text)
            df = pd.DataFrame(data)
            self.storage.save(df, "data/quotes_enterprise.csv")
            self.logger.info(f"Job completed. Extracted {len(data)} quotes.")
        else:
            self.logger.error("Failed to fetch initial page.")

if __name__ == "__main__":
    scraper = QuotesScraper()
    scraper.run()
