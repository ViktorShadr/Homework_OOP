import pytest

from src.product import Product


def test_product_init(product_1):
    assert product_1.name == "апельсин"
    assert product_1.description == "свежий и очень вкусный"
    assert product_1.price == 10.2
    assert product_1.quantity == 5


def test_new_product_creates_new():
    existing = []
    data = {
        "name": "iPhone 15",
        "price": 1000,
        "description": "256GB",
        "quantity": 5
    }
    product = Product.new_product(data, existing)
    assert product in existing
    assert product.name == "iPhone 15"
    assert product.quantity == 5
    assert product.price == 1000


def test_new_product_updates_existing():
    existing = [Product("iPhone 15", "256GB",900, 3)]
    data = {
        "name": "iPhone 15",
        "price": 1000,  # выше старой цены
        "description": "256GB",
        "quantity": 2
    }
    product = Product.new_product(data, existing)
    assert len(existing) == 1  # не создали новый
    assert product.quantity == 5  # 3 + 2
    assert product.price == 1000  # обновили до максимальной


def test_new_product_missing_field():
    existing = []
    data = {
        "name": "iPhone 15",
        "price": 1000,
        "quantity": 5
        # description пропущен
    }
    with pytest.raises(ValueError) as excinfo:
        Product.new_product(data, existing)
    assert "Отсутствует обязательное поле: description" in str(excinfo.value)
