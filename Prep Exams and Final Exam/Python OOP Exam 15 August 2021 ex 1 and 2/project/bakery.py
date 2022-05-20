from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            x = Bread(name, price)
            self.food_menu.append(x)

        elif food_type == "Cake":
            x = Cake(name, price)
            self.food_menu.append(x)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            x = Tea(name, portion, brand)
            self.drinks_menu.append(x)

        elif drink_type == "Water":
            x = Water(name, portion, brand)
            self.drinks_menu.append(x)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            x = InsideTable(table_number, capacity)
            self.tables_repository.append(x)

        elif table_type == "OutsideTable":
            x = OutsideTable(table_number, capacity)
            self.tables_repository.append(x)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.is_reserved = True
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def find_table(self, num):
        for table in self.tables_repository:
            if table.table_number == num:
                return table
        return False

    def order_food(self, table_number: int, *args):
        if not self.find_table(table_number):
            return f"Could not find table {table_number}"
        x = self.find_table(table_number)
        not_in_menu = []
        in_menu = [x.name for x in self.food_menu]
        for food in args:
            if food in in_menu:
                for obj in self.food_menu:
                    if obj.name == food:
                        x.food_orders.append(obj)
            else:
                not_in_menu.append(food)

        res = f"Table {table_number} ordered:\n"
        for food in x.food_orders:
            res += repr(food) + "\n"
        res += f"{self.name} does not have in the menu:\n"
        for food in not_in_menu:
            res += food + "\n"
        return res.strip()

    def order_drink(self, table_number: int, *args):
        if not self.find_table(table_number):
            return f"Could not find table {table_number}"
        x = self.find_table(table_number)
        not_in_menu_drink = []
        in_menu_drink = [x.name for x in self.drinks_menu]
        for drink in args:
            if drink in in_menu_drink:
                for obj in self.drinks_menu:
                    if obj.name == drink:
                        x.drink_orders.append(obj)
            else:
                not_in_menu_drink.append(drink)

        res = f"Table {table_number} ordered:\n"
        for drink in x.drink_orders:
            res += repr(drink) + "\n"
        res += f"{self.name} does not have in the menu:\n"
        for drink in not_in_menu_drink:
            res += drink + "\n"
        return res.strip()

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                table.clear()
                res = f"Table: {table_number}\n"
                res += f"Bill: {bill:.2f}"
                self.total_income += bill
                return res

    def get_free_tables_info(self):
        res = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                res += table.free_table_info() + "\n"
        return res.strip()

    def get_total_income(self):
        for table in self.tables_repository:
            self.leave_table(table.table_number)
        return f"Total income: {self.total_income:.2f}lv"


# from unittest import TestCase
#
# class BakeryTest(TestCase):
#
#     def test_reserve_table(self):
#         bake = Bakery("Bakeru")
#         bake.add_table("InsideTable", 50, 7)
#         bake.add_food("Cake", "gradska", 2.40)
#         bake.add_food("Cake", "selska", 2.00)
#         bake.add_drink("Water", "hubava", 200, "devin")
#         bake.order_drink(50, "hubava")
#         s = bake.leave_table(50)
#         self.assertEqual("Table 50 has been reserved for 5 people", s)