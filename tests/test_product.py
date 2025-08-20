import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


def test_add_same_class():
    s1 = Smartphone("Samsung", "Galaxy", 1000.0, 3, 90.0, "S23", 256, "Серый")
    s2 = Smartphone("Iphone", "15", 2000.0, 2, 95.0, "15", 512, "Черный")

    # стоимость: 1000*3 + 2000*2 = 3000 + 4000 = 7000
    result = s1 + s2
    assert result == 7000.0


def test_add_different_classes_raises():
    s = Smartphone("Samsung", "Galaxy", 1000.0, 3, 90.0, "S23", 256, "Серый")
    l = LawnGrass("Газон", "Трава", 500.0, 10, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        result = s + l


def test_product_str():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    expected = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product) == expected
