import unittest
from services.quotes_scraper import QuotesScraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = QuotesScraper()

    def test_clean_text(self):
        dirty = "  Hello &ldquo;World&rdquo; \n "
        clean = self.scraper.clean_text(dirty)
        self.assertEqual(clean, 'Hello "World"')

    def test_parse_quotes(self):
        sample_html = '<div class="quote"><span class="text">Test Quote</span><small class="author">Author</small><div class="tags"><a class="tag">tag1</a></div></div>'
        results = self.scraper.parse(sample_html)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['author'], 'Author')

if __name__ == "__main__":
    unittest.main()
