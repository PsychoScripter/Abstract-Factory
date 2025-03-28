from abc import ABC, abstractmethod

# Abstract Products
class Car(ABC):
    @abstractmethod
    def get_detail(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class SUV(Car):
    pass

class Coupe(Car):
    pass

# Concrete Products
class BmwSUV(SUV):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_detail(self):
        return f"BMW SUV - Model: {self.model}"

    def get_price(self):
        return f"${self.price}"

class BmwCoupe(Coupe):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_detail(self):
        return f"BMW Coupe - Model: {self.model}"

    def get_price(self):
        return f"${self.price}"

class BenzSUV(SUV):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_detail(self):
        return f"Mercedes SUV - Model: {self.model}"

    def get_price(self):
        return f"${self.price}"

class BenzCoupe(Coupe):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_detail(self):
        return f"Mercedes Coupe - Model: {self.model}"

    def get_price(self):
        return f"${self.price}"

# Abstract Factory
class CarFactory(ABC):
    @abstractmethod
    def create_suv(self):
        pass

    @abstractmethod
    def create_coupe(self):
        pass

# Concrete Factories
class BmwFactory(CarFactory):
    def create_suv(self, model, price):
        return BmwSUV(model, price)

    def create_coupe(self, model, price):
        return BmwCoupe(model, price)

class BenzFactory(CarFactory):
    def create_suv(self, model, price):
        return BenzSUV(model, price)

    def create_coupe(self, model, price):
        return BenzCoupe(model, price)

# Client Code
if __name__ == '__main__':
    bmw_factory = BmwFactory()
    benz_factory = BenzFactory()

    cars = [
        bmw_factory.create_suv("X5", 70000),
        bmw_factory.create_coupe("M4", 80000),
        benz_factory.create_suv("GLE", 75000),
        benz_factory.create_coupe("C-Class", 60000),
    ]

    for car in cars:
        print(car.get_detail(), "| Price:", car.get_price())