from src.base_order import BaseOrder
from src.product import Product


class Order(BaseOrder):

    def __init__(self, product: Product, quantity: int):
        super().__init__(product.name, f"Заказ {quantity} шт. товара {product.name}")
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итог: {self.total_price} руб."
