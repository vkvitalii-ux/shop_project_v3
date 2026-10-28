class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.__quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.__quantity} шт."


    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            self.__price = new_price

    @property
    def quantity(self):
        return self.__quantity
