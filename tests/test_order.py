from src.order import Order
from src.product import Product


def test_order_creation():
    # создаём товар
    product = Product(name="Ноутбук", description="Игровой", price=50000, quantity=10)

    # создаём заказ на 2 штуки
    order = Order(product, 2)

    # проверяем, что заказ содержит правильные данные
    assert order.product == product
    assert order.quantity == 2
    assert order.total_price == 100000  # 50000 * 2
    assert order.name == "Ноутбук"
    assert "Заказ: Ноутбук, 2 шт. Итог: 100000 руб." in str(order)