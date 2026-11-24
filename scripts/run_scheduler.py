"""Chạy thu thập giá định kỳ."""
from apscheduler.schedulers.blocking import BlockingScheduler
from price_tracker.config import SCRAPE_INTERVAL_MINUTES
from price_tracker.main import run

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(run, "interval", minutes=SCRAPE_INTERVAL_MINUTES)
    run()
    scheduler.start()
