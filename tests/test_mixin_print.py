from src.product import Product


def test_mixin_print_repr(capsys):
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    expected = "Product('Iphone 15', '512GB, Gray space', 210000.0, 8)"
    assert repr(product) == expected

    # проверяем, что print в __init__ тоже вывел repr
    captured = capsys.readouterr()
    assert expected in captured.out