class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed



from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_make_with_valid_data(self):
        car = Car("make", "model", 7, 10)
        self.assertEqual("make", car.make)
        self.assertEqual("model", car.model)
        self.assertEqual(7, car.fuel_consumption)
        self.assertEqual(10, car.fuel_capacity)

    def test_make_with_invalid_make_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car("", "model", 7, 10)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_with_invalid_model_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car("Make", "", 7, 10)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_make_with_invalid_consumption_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car("Make", "Model", -1, 10)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_make_with_invalid_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Make", "Model", 7, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_refuel_when_it_dont_lead_to_over_capacity(self):
        car = Car("Make", "Model", 7, 10)
        car.refuel(2)
        self.assertEqual(2, car.fuel_amount)

    def test_refuel_when_it_leads_to_over_capacity(self):
        car = Car("Make", "Model", 7, 10)
        car.refuel(11)
        self.assertEqual(10, car.fuel_amount)

    def test_refuel_when_amount_to_be_fueled_is_smaller_than_zero_raises(self):
        car = Car("Make", "Model", 7, 10)
        with self.assertRaises(Exception) as ex:
            car.refuel(-3)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_when_amount_to_be_fueled_is_zero_raises(self):
        car = Car("Make", "Model", 7, 10)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_when_fuel_amount_correct(self):
        car = Car("Make", "Model", 7, 10)
        car.fuel_amount = 8
        self.assertEqual(8, car.fuel_amount)

    def test_when_fuel_amount_smaller_than_zero_raises(self):
        car = Car("Make", "Model", 7, 10)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_drive_with_correct_data(self):
        car = Car("Make", "Model", 7, 50)
        #maybe check what happens if u have amount bigger than capacity
        car.fuel_amount = 45
        car.drive(40)
        self.assertEqual(45-2.8, car.fuel_amount)

    def test_drive_with_too_big_distance_raises(self):
        car = Car("Make", "Model", 20, 50)
        car.fuel_amount = 45
        with self.assertRaises(Exception) as ex:
            car.drive(4000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
