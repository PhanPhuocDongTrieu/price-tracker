import pandas as pd


def summarize(prices: list[float]) -> dict:
    """Thống kê cơ bản cho chuỗi giá."""
    s = pd.Series(prices, dtype=float)
    return {
        "min": s.min(),
        "max": s.max(),
        "mean": round(s.mean(), 2),
        "std": round(s.std(), 2) if len(s) > 1 else 0.0,
        "change_pct": round((s.iloc[-1] - s.iloc[0]) / s.iloc[0] * 100, 2) if len(s) > 1 else 0.0,
    }
