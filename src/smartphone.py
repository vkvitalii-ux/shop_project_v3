from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        return (self.price * self.quantity) + (other.price * other.quantity)


if __name__ == "__main__":
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    print(smartphone.name)
    print(smartphone.description)
    print(smartphone.price)
    print(smartphone.quantity)

    print(smartphone.efficiency)
    print(smartphone.model)
    print(smartphone.memory)
    print(smartphone.color)

    smartphone2 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    print(smartphone + smartphone2)
