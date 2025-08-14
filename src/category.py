class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):

        self.name = name
        self.description = description
        self._products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, new_product):
        self._products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        return "".join(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n" for p in self._products)
