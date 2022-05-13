from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def test_init(self):
        mammal = Mammal("name", "mammal_type", "sound")
        self.assertEqual("name", mammal.name)
        self.assertEqual("mammal_type", mammal.type)
        self.assertEqual("sound", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound(self):
        mammal = Mammal("name", "mammal_type", "sound")
        x = mammal.make_sound()
        self.assertEqual("name makes sound", x)

    def test_get_kingdom(self):
        mammal = Mammal("name", "mammal_type", "sound")
        x = mammal.get_kingdom()
        self.assertEqual("animals", x)

    def test_get_info(self):
        mammal = Mammal("name", "mammal_type", "sound")
        x = mammal.info()
        self.assertEqual("name is of type mammal_type", x)

