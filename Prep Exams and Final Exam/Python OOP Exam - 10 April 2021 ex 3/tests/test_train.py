from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train = Train("Samis train", 100)

    def test_init(self):
        train = Train("Samis train", 100)
        self.assertEqual("Samis train", train.name)
        self.assertEqual(100, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_when_cap_full_raises(self):
        self.train.passengers = ["1"] * 100
        with self.assertRaises(ValueError) as ex:
            self.train.add("kole")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_if_passenger_exists_raises(self):
        self.train.passengers = ["Sami"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("Sami")
        self.assertEqual("Passenger Sami Exists", str(ex.exception))

    def test_add_happy_case(self):
        x = self.train.add("niki")
        self.assertEqual("niki", self.train.passengers[0])
        #Do I need 2 tests here?
        self.assertEqual("Added passenger niki", x)

    def test_remove_when_passenger_not_there_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("sami")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_happy_case(self):
        self.train.add("sami")
        x = self.train.remove("sami")
        self.assertEqual([], self.train.passengers)
        self.assertEqual("Removed sami", x)
