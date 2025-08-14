from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product


def test_category_iterator_simple(example_data):
    category = Category(example_data[0]["name"], example_data[0]["description"], example_data[0]["products"])

    iterator = CategoryIterator(category)

    # Проверяем, что итератор возвращает объекты Product
    for product in iterator:
        assert isinstance(product, Product)

    # Проверяем, что количество товаров совпадает с исходным списком
    assert len(list(CategoryIterator(category))) == len(example_data[0]["products"])


def test_category_iterator_repr(example_data):
    # Создаем категорию
    category = Category(example_data[0]["name"], example_data[0]["description"], example_data[0]["products"])

    # Создаем итератор
    iterator = CategoryIterator(category)

    # Вызываем __repr__
    repr_str = repr(iterator)

    # Проверяем, что строка начинается с имени класса
    assert repr_str.startswith("CategoryIterator(")

    # Проверяем, что в строке присутствует имя первого продукта
    first_product_name = example_data[0]["products"][0]["name"]
    assert first_product_name in repr_str

    # Проверяем, что результат — это строка
    assert isinstance(repr_str, str)
