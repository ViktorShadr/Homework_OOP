from src.category import Category


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, data):
        # Ищем товар с таким же именем
        for product in Category.products:
            if product.name.lower() == data["name"].lower():
                # Суммируем количество
                product.quantity += data["quantity"]
                # Цена — максимальная
                if data["price"] > product.price:
                    product.price = data["price"]
                return product  # Возвращаем обновленный товар

        # Если не нашли — создаём новый
        new_prod = cls(**data)
        products_list.append(new_prod)
        return new_prod


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self._price = new_price

