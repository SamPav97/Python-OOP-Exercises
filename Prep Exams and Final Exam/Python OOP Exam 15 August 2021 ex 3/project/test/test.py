from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):

    def setUp(self) -> None:
        self.shop = PetShop("magazino")

    def test_init(self):
        shop = PetShop("magazino")
        self.assertEqual("magazino", shop.name)
        self.assertEqual({}, shop.food)
        self.assertEqual([], shop.pets)

    def test_add_food_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food("vafla", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_happy_case(self):
        x = self.shop.add_food("vafla", 2.00)
        self.assertEqual(f"Successfully added 2.00 grams of vafla.", x)

    def test_add_pet_raises(self):
        self.shop.add_pet("joni")
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("joni")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_happy_case(self):
        self.shop.add_pet("joni")
        self.assertEqual(["joni"], self.shop.pets)

    def test_feed_pet_when_pet_not_in_pets_raises(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("vafla", "sami")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_when_food_not_in_food_raises(self):
        self.shop.add_pet("sami")
        x = self.shop.feed_pet("kur", "sami")
        self.assertEqual('You do not have kur', x)

    def test_if_food_lower_than_100(self):
        self.shop.add_pet("sami")
        self.shop.add_food("kur", 89)
        x = self.shop.feed_pet("kur", "sami")
        self.assertEqual("Adding food...", x)

    def test_if_food_increased(self):
        self.shop.add_pet("sami")
        self.shop.add_food("kur", 89)
        self.shop.feed_pet("kur", "sami")
        self.assertEqual(1089, self.shop.food["kur"])

    def test_feed_pet_happy_case(self):
        self.shop.add_pet("sami")
        self.shop.add_food("kur", 300)
        x = self.shop.feed_pet("kur", "sami")
        self.assertEqual("sami was successfully fed", x)
        self.assertEqual(200, self.shop.food["kur"])

    def test_rep(self):
        self.shop.add_pet("sami")
        x = self.shop.__repr__()
        self.assertEqual(f'Shop magazino:\nPets: sami', x)


if __name__ == "__main__":
    main()
