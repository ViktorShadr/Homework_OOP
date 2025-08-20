from src.lawn_grass import LawnGrass


def test_lawn_grass_init(lawn_grass1_data, lawn_grass2_data):
    lawn1 = LawnGrass(*lawn_grass1_data)
    lawn2 = LawnGrass(*lawn_grass2_data)

    # Проверка lawn1
    assert lawn1.name == "Газонная трава"
    assert lawn1.description == "Элитная трава для газона"
    assert lawn1.price == 500.0
    assert lawn1.quantity == 20
    assert lawn1.country == "Россия"
    assert lawn1.germination_period == "7 дней"
    assert lawn1.color == "Зеленый"

    # Проверка lawn2
    assert lawn2.name == "Газонная трава 2"
    assert lawn2.description == "Выносливая трава"
    assert lawn2.price == 450.0
    assert lawn2.quantity == 15
    assert lawn2.country == "США"
    assert lawn2.germination_period == "5 дней"
    assert lawn2.color == "Темно-зеленый"