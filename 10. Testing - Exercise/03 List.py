class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)




from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_is_initialized_correctly_without_data(self):
        #arrange, act
        ints = IntegerList()
        #assert
        self.assertEqual([], ints._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_data(self):
        # arrange, act
        ints = IntegerList("asd", 5.2)
        #assert
        self.assertEqual([], ints._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_and_right_data(self):
        # arrange, act
        ints = IntegerList(3, "asd", 5.2)
        #assert
        self.assertEqual([3], ints._IntegerList__data)

    def test_get_data(self):
        ints = IntegerList(3, "asd", 5.2)
        self.assertEqual([3], ints._IntegerList__data)

        res = ints.get_data()
        self.assertEqual([3], res)

    def test_if_correct_el_added(self):
        #arrange
        ints = IntegerList(1, 2)
        #act
        ints.add(3)
        #assert
        self.assertEqual([1, 2, 3], ints._IntegerList__data)

    def test_if_el_added_not_int_raises(self):
        #arrange
        ints = IntegerList(1, 2)
        #act, assert
        with self.assertRaises(ValueError) as ex:
            ints.add(3.2)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_removing_correct_index(self):
        #arrange
        ints = IntegerList(1, 2, 3)
        #act
        ints.remove_index(1)
        #assert
        self.assertEqual([1, 3], ints.get_data())

    def test_removing_index_out_of_range(self):
        #arrange
        ints = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            ints.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_valid_value_and_valid_ind(self):
        #arrange
        ints = IntegerList(1, 2, 3)
        #act
        ints.insert(2, 4)
        #assert
        self.assertEqual([1, 2, 4, 3], ints.get_data())

    def test_insert_with_invalid_value_raises(self):
        #arrange
        ints = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError) as ex:
            ints.insert(2, 4.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_with_invalid_ind_raises(self):
        #arrange
        ints = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            ints.insert(5, 4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_biggest(self):
        ints = IntegerList(1, 3, 2)
        #act
        res = ints.get_biggest()
        #assert
        self.assertEqual(3, res)

    def test_get_index(self):
        ints = IntegerList(1, 3, 2)
        #act
        res = ints.get_index(2)
        #assert
        self.assertEqual(2, res)


if __name__ == "__main__":
    main()
