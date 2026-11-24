from bs4 import BeautifulSoup
from .base import BaseScraper


class ExampleScraper(BaseScraper):
    """Scraper mẫu — sửa CSS selector theo trang thật."""

    def parse_price(self, html: str) -> float:
        soup = BeautifulSoup(html, "lxml")
        tag = soup.select_one(".price")
        text = tag.get_text() if tag else ""
        return float("".join(c for c in text if c.isdigit()) or 0)
