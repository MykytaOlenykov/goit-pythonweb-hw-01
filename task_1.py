import logging

from abc import ABC, abstractmethod


logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):

    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make: str, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str):
        pass


class USVehicleFactory(VehicleFactory):

    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):

    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


class Car(Vehicle):

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


class Motorcycle(Vehicle):

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("BMW", "R1250GS")
vehicle2.start_engine()
