from src.category import Category
from src.product import Product


def test_category_init(example_data):
    categories = [Category(d["name"], d["description"], [Product(**p) for p in d["products"]]) for d in example_data]
    cat = categories[0]
    assert cat.name == "Смартфоны"
    assert cat.description.startswith("Смартфоны, как средство")
    assert len(cat._products) == 3
    assert all(isinstance(p, Product) for p in cat._products)


def test_product_count_stepwise(example_data):
    Category.category_count = 0
    Category.product_count = 0

    total_categories = 0
    total_products = 0

    for category_data in example_data:
        total_categories += 1
        total_products += len(category_data["products"])

        Category(
            category_data["name"],
            category_data["description"],
            [Product(**p) for p in category_data["products"]],
        )

        assert Category.category_count == total_categories
        assert Category.product_count == total_products


def test_products(example_data):
    categories = []
    for data in example_data:
        product_objects = [Product(**prod) for prod in data["products"]]
        categories.append(Category(data["name"], data["description"], product_objects))
    # Проверка количества категорий
    assert len(categories) == 2
    # Проверка первой категории
    smartphones = categories[0]
    products_str = smartphones.products

    assert isinstance(products_str, str)
    assert "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products_str
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in products_str

    # Проверка, что список _products хранит Product
    assert all(isinstance(p, Product) for p in smartphones._products)


def test_add_product_increases_count_and_list(example_data):
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создаем категорию с одним продуктом из example_data
    cat = Category(
        example_data[0]["name"],
        example_data[0]["description"],
        [Product(**example_data[0]["products"][0])],
    )

    initial_product_count = Category.product_count
    initial_products_len = len(cat._products)  # обращаемся к внутреннему списку

    # Создаем новый продукт
    new_product = Product("Test Product", "Description", 999.0, 3)

    # Добавляем продукт через метод
    cat.add_product(new_product)

    # Проверяем, что счетчик увеличился на 1
    assert Category.product_count == initial_product_count + 1

    # Проверяем, что внутренний список продуктов увеличился на 1
    assert len(cat._products) == initial_products_len + 1

    # Можно дополнительно проверить, что последний продукт — это новый продукт
    assert cat._products[-1] == new_product
