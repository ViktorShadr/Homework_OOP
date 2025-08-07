def test_category_init(category_1):
    assert category_1.name == 'фрукт'
    assert category_1.description == 'сладости'
    assert category_1.products == ['банан', 'апельсин', 'яблоко']