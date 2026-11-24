def should_alert(current_price: float, target_price: float | None) -> bool:
    return target_price is not None and current_price <= target_price


def send_alert(product_name: str, price: float) -> None:
    # TODO: gửi qua Email / Telegram
    print(f"[CẢNH BÁO] {product_name} giảm còn {price:,.0f}đ")
