def test_product_init(product_1):
    assert product_1.name == 'апельсин'
    assert product_1.description == 'свежий и очень вкусный'
    assert product_1.price == 10.2
    assert product_1.quantity == 5


