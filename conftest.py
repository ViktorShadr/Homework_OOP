import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return (
        Product(
            name='апельсин',
            description='свежий и очень вкусный',
            price=10.2,
            quantity=5
        )
    )

@pytest.fixture
def product_2():
    return (
        Product(
            name='яблоко',
            description='зеленое',
            price=15.0,
            quantity=10
        )
    )


@pytest.fixture
def category_1():
    return (
        Category(
            name='фрукт',
            description='сладости',
            products=['банан', 'апельсин', 'яблоко']
        )
    )





