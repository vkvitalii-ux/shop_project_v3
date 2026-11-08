import pytest


def test_lawngrass_init(product_lawngrass):
    assert product_lawngrass.name == "Газонная трава"
    assert product_lawngrass.description == "Элитная трава для газона"
    assert product_lawngrass.price == 500.0
    assert product_lawngrass.quantity == 20
    assert product_lawngrass.country == "Россия"
    assert product_lawngrass.germination_period == "7 дней"
    assert product_lawngrass.color == "Зеленый"


def test_lawngrass_test_add(product_lawngrass, product_lawngrass2):
    assert product_lawngrass + product_lawngrass2 == 20000.0


def test_lawngrass_test_add_error(product_lawngrass, product_smartphone):
    with pytest.raises(TypeError):
        result = product_lawngrass + product_smartphone
