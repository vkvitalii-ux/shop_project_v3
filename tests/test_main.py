import pytest
from src.category import Category

from src.product import Product


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


def test_category_add_product_error(second_category):
    """Тест: Проверка, что в категорию нельзя добавить объект, не являющийся продуктом"""
    with pytest.raises(TypeError):
        second_category.add_product("Просто строка вместо продукта")


def test_product_init_zero_quantity_raises_value_error():
    """Тест Выбрасывания ValueError при нулевом или количеством"""
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Описание", 1000.0, 0)


def test_category_middle_price_empty():
    """Тест подсчета средней цены для пустой категории."""
    empty_cat = Category("Пустая категория", "Здесь нет товаров", [])
    assert empty_cat.middle_price() == 0


def test_category_middle_price(second_category):
    """Тест: Корректный подсчет средней цены товаров в категории"""
    assert second_category.middle_price() == 30000.0
