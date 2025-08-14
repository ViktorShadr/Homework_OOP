import pytest

from src.product import Product


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
    data = {"name": "iPhone 15", "price": 1000, "description": "256GB", "quantity": 2}
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
    assert product.name == "Galaxy S21"
    assert product.price == 800
    assert product.quantity == 4


def test_price_setter_increase():
    product = Product("LG", "Smartphone", 15000, 5)
    product.price = 20000  # увеличение без вопросов
    assert product.price == 20000


def test_price_setter_negative_or_zero(capsys):
    product = Product("LG", "Smartphone", 15000, 5)

    product.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 15000

    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 15000


def test_price_setter_lower_price_with_confirm(monkeypatch):
    product = Product("Sony", "TV", 5000, 3)

    # Симулируем ввод "y"
    monkeypatch.setattr("builtins.input", lambda _: "y")

    product.price = 4000
    assert product.price == 4000


def test_price_setter_lower_price_with_decline(monkeypatch):
    product = Product("Sony", "TV", 5000, 3)

    # Симулируем ввод "n"
    monkeypatch.setattr("builtins.input", lambda _: "n")

    product.price = 4000
    assert product.price == 5000
