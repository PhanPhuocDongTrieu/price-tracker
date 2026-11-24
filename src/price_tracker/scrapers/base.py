from abc import ABC, abstractmethod
import requests


class BaseScraper(ABC):
    """Lớp cơ sở cho mọi scraper."""

    headers = {"User-Agent": "Mozilla/5.0 (PriceTracker)"}

    def fetch(self, url: str) -> str:
        resp = requests.get(url, headers=self.headers, timeout=15)
        resp.raise_for_status()
        return resp.text

    @abstractmethod
    def parse_price(self, html: str) -> float:
        """Trích xuất giá từ HTML."""

    def get_price(self, url: str) -> float:
        return self.parse_price(self.fetch(url))
