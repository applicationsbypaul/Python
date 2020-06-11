SHIPPING_UNDER_10 = 5.95
SHIPPING_BETWEEN_30_10 = 7.95
SHIPPING_BETWEEN_30_50 = 11.95
TAX = .06


def calculate_order(price, cash_coupon, percent_coupon):
    if 10 > price > cash_coupon:
        total = price - cash_coupon
        total = total - (total * percent_coupon)
        total = (total * (1 + TAX) + SHIPPING_UNDER_10)
        return round(total, 2)
    elif 10 > price < cash_coupon:
        total = price - (price * percent_coupon)
        total = (total * (1 + TAX) + SHIPPING_UNDER_10)
        return round(total, 2)
    elif 10 < price <= 30:
        total = price - cash_coupon
        total = total - (total * percent_coupon)
        total = (total * (1 + TAX) + SHIPPING_BETWEEN_30_10)
        return round(total, 2)
    elif 30 < price <= 50:
        total = price - cash_coupon
        total = total - (total * percent_coupon)
        total = (total * (1 + TAX) + SHIPPING_BETWEEN_30_50)
        return round(total, 2)
    else:
        total = price - cash_coupon
        total = total - (total * percent_coupon)
        total = (total * (1 + TAX))
        return round(total, 2)


if __name__ == '__main__':
    pass
