import pandas as pd


def moving_average(prices: list[float], window: int = 7) -> list[float]:
    return pd.Series(prices, dtype=float).rolling(window, min_periods=1).mean().tolist()


def trend(prices: list[float]) -> str:
    if len(prices) < 2:
        return "không đủ dữ liệu"
    if prices[-1] > prices[0]:
        return "tăng"
    if prices[-1] < prices[0]:
        return "giảm"
    return "đi ngang"
