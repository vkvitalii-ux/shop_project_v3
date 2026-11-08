from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_print_mixin(capsys):
    Product(
        name="Product",
        description="Product",
        price=30000,
        quantity=3
    )
    message = capsys.readouterr()
    expected = "Product('Product', 'Product', 30000, 3)"
    assert message.out.strip() == expected

    Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    message = capsys.readouterr()
    expected = (
        "Smartphone('Samsung Galaxy S23 Ultra', "
        "'256GB, Серый цвет, 200MP камера', "
        "180000.0, 5)"
    )
    assert message.out.strip() == expected

    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    message = capsys.readouterr()
    expected = (
        "LawnGrass('Газонная трава', "
        "'Элитная трава для газона', "
        "500.0, 20)"
    )
    assert message.out.strip() == expected
