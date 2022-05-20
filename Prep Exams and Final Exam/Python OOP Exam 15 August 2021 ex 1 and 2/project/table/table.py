from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total = 0
        for food in self.food_orders:
            total += food.price
        for drink in self.drink_orders:
            total += drink.price
        return total

    def clear(self):
        self.drink_orders.clear()
        self.food_orders.clear()
        #I missed the thing below
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        #I had forgotten this
        if self.is_reserved:
            return None
        #Self name should work
        res = f"Table: {self.table_number}\n"
        res += f"Type: {self.__class__.__name__}\n"
        res += f"Capacity: {self.capacity}"
        return res
