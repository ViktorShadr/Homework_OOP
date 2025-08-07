from src.category import Category


def test_category_init(category_1):
    assert category_1.name == "фрукт"
    assert category_1.description == "сладости"
    assert category_1.products == ["банан", "апельсин", "яблоко"]


def test_category_counters(category_1):
    Category.category_count = 0
    Category.product_count = 0

    cat = Category(name="овощи", description="полезно", products=["морковь", "помидор"])
    assert Category.category_count == 1
    assert Category.product_count == 2

    cat2 = Category(name="напитки", description="жидкости", products=[])
    assert Category.category_count == 2
    assert Category.product_count == 2  # продуктов не добавилось


def test_product_count_accumulation(category_1):
    initial_cat_count = Category.category_count
    initial_prod_count = Category.product_count

    cat = Category(name="сухофрукты", description="вкусняшки", products=["изюм", "курага"])
    assert Category.category_count == initial_cat_count + 1
    assert Category.product_count == initial_prod_count + 2
