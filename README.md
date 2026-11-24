# Price Tracker — Hệ thống theo dõi và phân tích giá sản phẩm

Hệ thống thu thập giá sản phẩm từ các trang thương mại điện tử, lưu lịch sử giá,
phân tích xu hướng và gửi cảnh báo khi giá giảm.

## Tính năng
- Thu thập giá tự động (scraper cho từng trang)
- Lưu lịch sử giá vào cơ sở dữ liệu (SQLite / PostgreSQL)
- Phân tích: giá thấp nhất/cao nhất, trung bình, xu hướng, biến động
- Cảnh báo giảm giá qua Email / Telegram
- REST API (FastAPI) và Dashboard (Streamlit)

## Cấu trúc thư mục
```
price-tracker/
├── config/                  # Cấu hình (danh sách sản phẩm)
├── data/
│   ├── raw/                 # Dữ liệu thô sau khi thu thập
│   └── processed/           # Dữ liệu đã làm sạch
├── docs/                    # Tài liệu
├── notebooks/               # Jupyter notebook phân tích
├── scripts/                 # Script chạy định kỳ
├── src/price_tracker/
│   ├── scrapers/            # Thu thập giá từ các trang
│   ├── database/            # Model và kết nối CSDL
│   ├── analysis/            # Thống kê, xu hướng giá
│   ├── alerts/              # Gửi cảnh báo
│   ├── api/                 # REST API (FastAPI)
│   ├── dashboard/           # Giao diện (Streamlit)
│   ├── utils/               # Tiện ích, logger
│   ├── config.py
│   └── main.py              # Điểm chạy chính
├── tests/                   # Unit test
├── .env.example
├── requirements.txt
└── README.md
```

## Cài đặt
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env
```

## Chạy
```bash
set PYTHONPATH=src
python -m price_tracker.main                         # thu thập giá 1 lần
python scripts/run_scheduler.py                      # thu thập định kỳ
uvicorn price_tracker.api.app:app --reload           # chạy API
streamlit run src/price_tracker/dashboard/app.py     # chạy dashboard
pytest                                               # chạy test
```
