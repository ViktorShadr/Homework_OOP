import pytest

from src.base_product import BaseProduct


def test_base_product_cannot_be_instantiated():
    """Нельзя создать объект BaseProduct напрямую"""
    with pytest.raises(TypeError):
        BaseProduct()


def test_inheritance_and_new_product():
    """Проверяем, что наследник обязан реализовать new_product"""

    class DummyProduct(BaseProduct):
        def __init__(self, name, price):
            self.name = name
            self.price = price

        @classmethod
        def new_product(cls, name, price):
            return cls(name, price)

    # создаём через new_product
    product = DummyProduct.new_product("Test product", 1000)

    assert isinstance(product, DummyProduct)
    assert product.name == "Test product"
    assert product.price == 1000
