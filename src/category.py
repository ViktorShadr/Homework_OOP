from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):

        self.name = name
        self.description = description
        self._products = [
            p if isinstance(p, Product) else Product(**p)
            for p in (products or [])
        ]

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, new_product):
        self._products.append(new_product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку с товарами в формате для теста"""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self._products
        )

    @property
    def products_list(self) -> list:
        """Возвращает список объектов Product"""
        return self._products


    def __str__(self):
        return (
            "".join(f"{self.name}, количество продуктов: "
            f"{sum(product.quantity for product in self._products)} шт.\n")
        )




