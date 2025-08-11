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
				product.price = max(product.price, product_data["price"])
				return product

		# Создание нового товара
		new_product = cls(**product_data)
		existing_products.append(new_product)
		return new_product


	@property
	def price(self):
		return self._price


	@price.setter
	def price(self, new_price):
		if new_price <= 0:
			print('Цена не должна быть нулевая или отрицательная')
		else:
			self._price = new_price

