from project.movie import Movie
from unittest import TestCase, main


class MovieTest(TestCase):
    def setUp(self) -> None:
        movie = Movie("Sam", 2020, 4.5)

    def test_init_happy(self):
        movie = Movie("Sam", 2020, 4.5)
        self.assertEqual("Sam", movie.name)
        self.assertEqual(2020, movie.year)
        self.assertEqual(4.5, movie.rating)
        self.assertEqual([], movie.actors)

    def test_init_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            Movie("", 2020, 4.5)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_init_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            Movie("saaa", 1000, 4.5)
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_happy(self):
        movie = Movie("Sam", 2020, 4.5)
        movie.add_actor("antonio")
        self.assertEqual(["antonio"], movie.actors)

    def test_add_actor_returns(self):
        movie = Movie("Sam", 2020, 4.5)
        movie.add_actor("antonio")
        self.assertEqual(["antonio"], movie.actors)
        x = movie.add_actor("antonio")
        self.assertEqual("antonio is already added in the list of actors!", x)

    def test_gt(self):
        movie1 = Movie("Sam", 2020, 4.5)
        movie2 = Movie("kur", 2019, 5)
        x = movie1 > movie2
        self.assertEqual('"kur" is better than "Sam"', x)

    def test_gt_2(self):
        movie1 = Movie("Sam", 2020, 4.5)
        movie2 = Movie("kur", 2019, 5)
        x = movie1 < movie2
        self.assertEqual('"kur" is better than "Sam"', x)

    def test_repr(self):
        movie1 = Movie("Sam", 2020, 4.5)
        x = repr(movie1)
        self.assertEqual(f"Name: Sam\nYear of Release: 2020\nRating: 4.50\nCast: ", x)

    def test_repr_2(self):
        movie1 = Movie("Sam", 2020, 4.5)
        movie1.add_actor("antonio")
        x = repr(movie1)
        self.assertEqual(f"Name: Sam\nYear of Release: 2020\nRating: 4.50\nCast: antonio", x)