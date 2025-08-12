class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        """
        Создает новый товар или обновляет существующий
        """
        if existing_products is None:
            existing_products = []

        # Проверка обязательных полей
        required_fields = ["name", "description", "price", "quantity"]
        for field in required_fields:
            if field not in product_data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")

        # Проверка дубликатов
        for product in existing_products:
            if product.name.lower() == product_data["name"].lower():
                product.quantity += product_data["quantity"]
                # Обновляем цену, если она больше текущей
                if product_data["price"] > product.price:
                    product.price = product_data["price"]
                return product

        # Создание нового товара
        new_product = cls(**product_data)
        existing_products.append(new_product)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price > self.__price:
            self.__price = new_price  # повышение — без вопросов
        elif new_price < self.__price:
            user_input = input("Вы точно хотите снизить цену?(y/n)").lower()
            if user_input == "y":
                self.__price = new_price




