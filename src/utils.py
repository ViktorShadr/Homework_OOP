import json

from src.category import Category
from src.product import Product


def read_json(path: str):
    """Функция чтения файла json"""
    with open(path, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return data


def create_product(data: dict):
    """Функция наполнения объектов класса"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
