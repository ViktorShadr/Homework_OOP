import json

from src.category import Category
from src.product import Product
from src.utils import create_product, read_json


def test_read_json(tmp_path):
    """Тест успешного чтения валидного JSON файла"""
    # Создаем временный файл с тестовыми данными
    test_data = {"products": ["яблоко", "банан"], "price": 10.5}
    file = tmp_path / "test_products.json"
    file.write_text(json.dumps(test_data))
    # Вызываем функцию и проверяем результат
    result = read_json(str(file))
    assert result == test_data


def test_create_product_returns_categories(example_data):
    categories = create_product(example_data)

    # Проверка, что возвращен список
    assert isinstance(categories, list)
    assert all(isinstance(c, Category) for c in categories)

    # Проверка количества категорий
    assert len(categories) == len(example_data)

    # Проверка, что продукты внутри — это объекты Product
    for cat, original in zip(categories, example_data):
        assert all(isinstance(p, Product) for p in cat._products)
        assert len(cat._products) == len(original["products"])


def test_create_product_data_integrity(example_data):
    categories = create_product(example_data)

    # Сверяем данные первой категории
    first_category = categories[0]
    assert first_category.name == "Смартфоны"
    assert first_category.description.startswith("Смартфоны, как средство")
    assert first_category._products[0].name == "Samsung Galaxy C23 Ultra"
    assert first_category._products[0].price == 180000.0
    assert first_category._products[0].quantity == 5
