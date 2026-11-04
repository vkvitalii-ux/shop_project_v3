from src.product import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        return (self.price * self.quantity) + (other.price * other.quantity)



if __name__ == "__main__":
    lawnGrass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    print(lawnGrass.name)
    print(lawnGrass.description)
    print(lawnGrass.price)
    print(lawnGrass.quantity)

    print(lawnGrass.country)
    print(lawnGrass.germination_period)
    print(lawnGrass.color)


    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    lawnGrass + product
