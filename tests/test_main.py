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


def test_product_init(first_product):
    assert first_product.name == "Product"


def test_category_products_property_print(first_product, second_category):
    print(second_category.products)


def test_category_products_property(first_product, second_category):
    assert second_category.products == (
        f"{first_product.name}, {first_product.price} руб. "
        f"Остаток: {first_product.quantity} шт.\n"
    )


def test_product_price_setter(first_product):
    """Тестируем режим доступа (геттер и сеттер) для цены продукта"""
    # 1. Проверяем успешное изменение через сеттер
    first_product.price = 50000.0
    assert first_product.price == 50000.0

    # 2. Проверяем защиту сеттера от некорректных данных (цена <= 0)
    first_product.price = -100
    assert first_product.price == 50000.0  # Цена не должна была измениться


def test_category_add_product(first_product, second_category):
    """Тестируем режим доступа к продуктам категории через метод add_product"""
    # Считаем, сколько товаров в строке изначально (из фикстуры там 1 товар)
    # Наш геттер возвращает строку, проверяем, что в ней есть имя первого продукта
    assert first_product.name in second_category.products

    # Создаем еще один продукт для проверки добавления
    new_prod = Product("Xiaomi", "Budget phone", 20000.0, 5)

    # Добавляем продукт в категорию через публичный метод
    second_category.add_product(new_prod)

    # Проверяем через геттер, что новый продукт успешно добавился в скрытый список
    assert "Xiaomi" in second_category.products


def test_product_str(first_product):
    assert str(first_product) == "Product, 30000 руб. Остаток: 3 шт."


def test_category_str(second_category):
    assert str(second_category) == "Category, количество продуктов: 3 шт."


def test_product_add(first_product):
    second_category = Product(
        "Samsung Galaxy", "Смартфон", 20000.0, 2
    )
    assert first_product + second_category == 130000.0


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


def test_category_add_product_error(second_category):
    """Тест: Проверка, что в категорию нельзя добавить объект, не являющийся продуктом"""
    with pytest.raises(TypeError):
        second_category.add_product("Просто строка вместо продукта")
