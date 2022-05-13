from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):

    def test_init(self):
        car = Vehicle(50.0, 301.0)
        self.assertEqual(50.0, car.fuel)
        self.assertEqual(50.0, car.capacity)
        self.assertEqual(301.0, car.horse_power)
        self.assertEqual(car.DEFAULT_FUEL_CONSUMPTION, car.fuel_consumption)

    def test_drive_happy_case(self):
        car = Vehicle(50.0, 301.0)
        car.drive(5)
        self.assertEqual(43.75, car.fuel)

    def test_drive_not_enough_fuel_raises(self):
        car = Vehicle(1.0, 301.0)
        with self.assertRaises(Exception) as ex:
            car.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_happy_case(self):
        car = Vehicle(50.0, 301.0)
        car.drive(20)
        car.refuel(20)
        self.assertEqual(45.0, car.fuel)

    def test_refuel_too_much_fuel_raises(self):
        car = Vehicle(50.0, 301.0)
        with self.assertRaises(Exception) as ex:
            car.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string_method(self):
        car = Vehicle(50.0, 301.0)
        self.assertEqual("The vehicle has 301.0 horse power with 50.0 fuel left and 1.25 fuel consumption", car.__str__())
