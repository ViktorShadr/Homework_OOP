import pytest

from src.product import Product


@pytest.mark.parametrize(
    "category_index, product_index",
    [
        (0, 0),  # Samsung Galaxy C23 Ultra
        (0, 1),  # Iphone 15
        (0, 2),  # Xiaomi Redmi Note 11
        (1, 0),  # 55" QLED 4K
    ],
)
def test_product_init_from_example_data(example_data, category_index, product_index):
    product_data = example_data[category_index]["products"][product_index]

    product = Product(**product_data)

    assert isinstance(product, Product)
    assert product.name == product_data["name"]
    assert product.description == product_data["description"]
    assert product.price == product_data["price"]
    assert product.quantity == product_data["quantity"]


def test_new_product_creates_new():
    existing = []
    data = {"name": "iPhone 15", "price": 1000, "description": "256GB", "quantity": 5}
    product = Product.new_product(data, existing)
    assert product in existing
    assert product.name == "iPhone 15"
    assert product.quantity == 5
    assert product.price == 1000


def test_new_product_updates_existing():
    existing = [Product("iPhone 15", "256GB", 900, 3)]
    data = {"name": "iPhone 15", "price": 1000, "description": "256GB", "quantity": 2}  # выше старой цены
    product = Product.new_product(data, existing)
    assert len(existing) == 1  # не создали новый
    assert product.quantity == 5  # 3 + 2
    assert product.price == 1000  # обновили до максимальной


def test_new_product_missing_field():
    existing = []
    data = {
        "name": "iPhone 15",
        "price": 1000,
        "quantity": 5,
        # description пропущен
    }
    with pytest.raises(ValueError) as excinfo:
        Product.new_product(data, existing)
    assert "Отсутствует обязательное поле: description" in str(excinfo.value)


def test_new_product_with_none_existing_products():
    data = {"name": "Galaxy S21", "price": 800, "description": "128GB", "quantity": 4}
    product = Product.new_product(data, existing_products=None)

    # Проверяем, что продукт создан и добавлен в новый список
    assert product.name == "Galaxy S21"
    assert product.price == 800
    assert product.quantity == 4


def test_price_setter():
    product = Product("LG", "Smartphone", 15000, 5)  # создаём продукт с ценой 1500

    # Попытка установить отрицательную цену — должна проигнорироваться (цена не изменится)
    product.price = -50
    assert product.price == 15000  # цена осталась прежней

    # Попытка установить цену 0 — тоже должна игнорироваться
    product.price = 0
    assert product.price == 15000

    # Установка положительной цены — должна примениться
    product.price = 150
    assert product.price == 150


def test_price_setter_print(capsys):
    product = Product("LG", "Smartphone", 15000, 5)  # создаём продукт с ценой 1500

    # Попытка установить отрицательную цену — должно вывести предупреждение
    product.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 15000  # цена не поменялась

    # Попытка установить 0 — тоже предупреждение
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 15000  # цена не поменялась

    # Установка положительной цены — предупреждения нет
    product.price = 200
    captured = capsys.readouterr()
    assert captured.out == ""
    assert product.price == 200
