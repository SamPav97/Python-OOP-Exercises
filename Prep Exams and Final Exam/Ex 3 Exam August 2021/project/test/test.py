from project.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.lib = Library("Tina's Lib")

    def test_init_happy_case(self):
        lib = Library("RadeTapako")
        self.assertEqual("RadeTapako", lib.name)
        self.assertEqual({}, lib.books_by_authors)
        self.assertEqual({}, lib.readers)

    def test_init_raises(self):

        with self.assertRaises(Exception) as ex:
            lib = Library("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_adds_author_when_author_not_there_and_book_not_there(self):
        self.lib.add_book("maistoro", "na vanq perdeto")
        self.assertEqual({"maistoro": ["na vanq perdeto"]}, self.lib.books_by_authors)
        self.assertEqual(["na vanq perdeto"], self.lib.books_by_authors["maistoro"])

    def test_add_book_if_author_there_but_book_not(self):
        self.lib.add_book("maistoro", "na vanq perdeto")
        self.lib.add_book("maistoro", "Shuntata")
        self.assertEqual(["na vanq perdeto", "Shuntata"], self.lib.books_by_authors["maistoro"])

    def test_add_book_when_author_there_and_book_there(self):
        self.lib.add_book("maistoro", "na vanq perdeto")
        self.lib.add_book("maistoro", "Shuntata")
        self.lib.add_book("maistoro", "Shuntata")
        self.assertEqual(["na vanq perdeto", "Shuntata"], self.lib.books_by_authors["maistoro"])

    def test_if_reader_not_there_add(self):
        self.lib.add_reader("sami")
        self.assertEqual({"sami": []}, self.lib.readers)

    def test_if_reader_there_dont_add_returns(self):
        self.lib.add_reader("sami")
        x = self.lib.add_reader("sami")
        self.assertEqual(f"sami is already registered in the {self.lib.name} library.", x)

    def test_rent_if_reader_not_in_self_reader_returns(self):
        self.lib.add_book("maistoro", "Shuntata")
        self.lib.add_reader("sami")
        x = self.lib.rent_book("horhe","maistoro", "Shuntata" )
        self.assertEqual(f"horhe is not registered in the {self.lib.name} Library.", x)

    def test_if_book_author_not_in_authors_returns(self):
        self.lib.add_book("maistoro", "Shuntata")
        self.lib.add_reader("sami")
        x = self.lib.rent_book("sami", "kole", "Shuntata")
        self.assertEqual(f"{self.lib.name} Library does not have any kole's books.", x)

    def test_if_book_not_in_author_returns(self):
        self.lib.add_book("maistoro", "Shuntata")
        self.lib.add_reader("sami")
        x = self.lib.rent_book("sami", "maistoro", "vunata")
        self.assertEqual(f"""{self.lib.name} Library does not have maistoro's "vunata".""", x)

    def test_if_book_rented_happy_case(self):
        self.lib.add_book("maistoro", "Shuntata")
        self.lib.add_reader("sami")
        self.lib.rent_book("sami", "maistoro", "Shuntata")
        self.assertEqual([{"maistoro": "Shuntata"}], self.lib.readers["sami"])
        self.assertEqual([], self.lib.books_by_authors["maistoro"])

if __name__ == "__main__":
    main()