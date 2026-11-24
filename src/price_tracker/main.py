from .database.db import init_db
from .utils.logger import get_logger

log = get_logger(__name__)


def run():
    init_db()
    log.info("Bắt đầu thu thập giá...")
    # TODO: đọc config/products.yaml, gọi scraper, lưu PriceHistory, kiểm tra cảnh báo


if __name__ == "__main__":
    run()
