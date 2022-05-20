from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):

    def setUp(self) -> None:
        self.factory = PaintFactory("Boqdjinica", 500)

    def test_init(self):
        factory = PaintFactory("Boqdjinica", 500)
        self.assertEqual("Boqdjinica", factory.name)
        self.assertEqual(500, factory.capacity)
        self.assertEqual({}, factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], factory.valid_ingredients)
        self.assertEqual({}, factory.products)

    def test_can_add(self):
        s = self.factory.can_add(50)
        self.assertEqual(True, s)
        s = self.factory.can_add(600)
        self.assertEqual(False, s)

    def test_add_ingridient_happy(self):
        self.factory.add_ingredient("blue", 70)
        self.assertEqual({"blue": 70}, self.factory.ingredients)

    def test_add_ingridient_when_already_have_happy(self):
        self.factory.add_ingredient("blue", 70)
        self.assertEqual({"blue": 70}, self.factory.ingredients)
        self.factory.add_ingredient("blue", 70)
        self.assertEqual({"blue": 140}, self.factory.ingredients)

    def test_ingridient_but_no_space_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("blue", 700)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_ingridient_but_not_allowed_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("kur", 50)
        self.assertEqual(f"Ingredient of type kur not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingr_happy(self):
        self.factory.add_ingredient("blue", 70)
        self.factory.remove_ingredient("blue", 40)
        self.assertEqual({"blue": 30}, self.factory.ingredients)
        self.factory.remove_ingredient("blue", 30)

    def test_remove_too_much_raises(self):
        self.factory.add_ingredient("blue", 70)
        self.factory.remove_ingredient("blue", 40)
        self.assertEqual({"blue": 30}, self.factory.ingredients)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("blue", 40)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_wrong_ingr_raises(self):
        self.factory.add_ingredient("blue", 70)
        self.factory.remove_ingredient("blue", 40)
        self.assertEqual({"blue": 30}, self.factory.ingredients)
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("kor", 40)
            #Below weird it wants single quotes
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_repr(self):
        self.factory.add_ingredient("blue", 70)
        x = self.factory.__repr__()
        self.assertEqual(f"Factory name: Boqdjinica with capacity 500.\nblue: 70\n", x)