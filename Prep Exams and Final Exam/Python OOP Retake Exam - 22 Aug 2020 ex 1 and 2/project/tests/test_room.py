from unittest import TestCase, main

from project.everland import Everland
from project.rooms.young_couple import YoungCouple


class TestRoom(TestCase):

    def test_init(self):
        room = YoungCouple("Pavlevchevi", 1000, 300)
        self.assertEqual("Pavlevchevi", room.family_name)
        self.assertEqual(1300, room.budget)
        self.assertEqual(2, room.members_count)
        self.assertEqual([], room.children)
        self.assertEqual(0, room.expenses)

    def test_init_negative_exp_raises(self):
        room = YoungCouple("Pavlevchevi", 1000, 300)
        with self.assertRaises(ValueError) as ex:
            room.expenses = -10
        self.assertEqual("Expenses cannot be negative", str(ex.exception))


if __name__ == "__main__":
    main()
