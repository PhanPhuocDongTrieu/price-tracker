from price_tracker.analysis.statistics import summarize
from price_tracker.analysis.trend import trend


def test_summarize():
    r = summarize([100, 80, 120])
    assert r["min"] == 80 and r["max"] == 120


def test_trend():
    assert trend([100, 90]) == "giảm"
    assert trend([90, 100]) == "tăng"
