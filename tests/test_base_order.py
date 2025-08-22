import pytest
from src.base_order import BaseOrder


def test_base_order_is_abstract():
    # напрямую создать нельзя
    with pytest.raises(TypeError):
        BaseOrder("test", "desc")


def test_base_order_inheritance():
    class DummyOrder(BaseOrder):
        def __str__(self):
            return f"DummyOrder: {self.name}, {self.description}"

    order = DummyOrder("Test order", "Just for test")

    assert order.name == "Test order"
    assert order.description == "Just for test"
    assert str(order) == "DummyOrder: Test order, Just for test"
