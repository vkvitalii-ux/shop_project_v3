import pytest

from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


@pytest.fixture
def first_product():
    return Product(
        name="Product",
        description="Product",
        price=30000,
        quantity=3
    )


@pytest.fixture
def category(first_product):
    return Category(
        name="Category",
        description="Category",
        products=[first_product]
    )


@pytest.fixture
def second_category(first_product):
    return Category(
        name="Category",
        description="Category",
        products=[first_product]
    )


@pytest.fixture()
def product_smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture()
def product_smartphone2():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture()
def product_lawngrass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture()
def product_lawngrass2():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
