from product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = sum(
            product.quantity for product in self.__products
        )
        return (
            f"{self.name}, "
            f"количество продуктов: {total_quantity} шт."
        )

    def add_product(self, product):
        """Метод для добавления одного товара в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"

        return products_str

    @classmethod
    def new_product(cls, product_info):
        return Product(
            product_info['name'],
            product_info['description'],
            product_info['price'],
            product_info['quantity']
        )
