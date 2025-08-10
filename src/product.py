class Product:
	name: str
	description: str
	price: float
	quantity: int

	def __init__(self, name, description, price, quantity):
		self.name = name
		self.description = description
		self.price = price
		self.quantity = quantity

	@classmethod
	def new_product(cls, data):
		return cls(**data)

