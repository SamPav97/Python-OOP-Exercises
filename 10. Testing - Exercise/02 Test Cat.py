class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry.')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):

    def test_check_if_cat_gained_weight_after_eating(self):
        #arrange
        cat = Cat("Sam")
        self.assertEqual(0, cat.size)
        #act
        cat.eat()
        #assert
        self.assertEqual(1, cat.size)

    def test_if_cat_is_fed_after_eating(self):
        #arrange
        cat = Cat("Sam")
        self.assertFalse(cat.fed)
        #act
        cat.eat()
        #assert
        self.assertTrue(cat.fed)

    def test_if_cat_cannot_eat_after_fed_raises(self):
        #arrange
        cat = Cat("Sam")
        #act
        cat.eat()
        #assert
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_fall_asleep_if_not_fed_raises(self):
        #arrange
        cat = Cat("Sam")
        #act

        #assert
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_not_sleepy_after_sleeping(self):
        #arrange
        cat = Cat("Sam")
        #act
        cat.eat()
        self.assertTrue(cat.sleepy)
        cat.sleep()
        #assert
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()
