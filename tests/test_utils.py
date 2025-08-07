import json

from src.category import Category
from src.product import Product
from src.utils import read_json, create_product


def test_read_json(tmp_path):
    """Тест успешного чтения валидного JSON файла"""
    # Создаем временный файл с тестовыми данными
    test_data = {"products": ["яблоко", "банан"], "price": 10.5}
    file = tmp_path / "test_products.json"
    file.write_text(json.dumps(test_data))
    # Вызываем функцию и проверяем результат
    result = read_json(str(file))
    assert result == test_data


def test_create_product(example_data):
    categories = create_product(example_data)

    assert isinstance(categories, list)
    assert len(categories) == 2

    # Проверка первой категории
    smartphones = categories[0]
    assert isinstance(smartphones, Category)
    assert smartphones.name == "Смартфоны"
    assert len(smartphones.products) == 3

    p1 = smartphones.products[0]
    assert isinstance(p1, Product)
    assert p1.name == "Samsung Galaxy C23 Ultra"
    assert p1.price == 180000.0
    assert p1.quantity == 5

    # Проверка второй категории
    tvs = categories[1]
    assert isinstance(tvs, Category)
    assert tvs.name == "Телевизоры"
    assert len(tvs.products) == 1

    tv = tvs.products[0]
    assert tv.name == '55" QLED 4K'
    assert tv.price == 123000.0
