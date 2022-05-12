class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WokerTests(TestCase):
    def test_worker_is_initialized_correctly(self):
        worker = Worker("Sam", 100, 10)
        self.assertEqual("Sammm", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_increased_after_rest(self):
        #arrange
        worker = Worker("test", 100, 10)

        self.assertEqual(10, worker.energy)
        #act
        worker.rest()

        #assert
        self.assertEqual(11, worker.energy)

    def test_worker_work_with_zero_energy_raises(self):
        #arrange
        worker = Worker("Sam", 100, 0)
        #act
        worker.work()

        #assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_with_neg_energy_raises(self):
        worker = Worker("Test", 100, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy", str(ex.exception))

    def test_worker_is_payed_after_working(self):
        worker = Worker("Sam", 100, 10)
        worker.work()
        self.assertEqual(100, worker.money)
        worker.work()
        self.assertEqual(200, worker.money)

    def test_energy_is_decreased_after_working(self):
        #arrange
        worker = Worker("Sam", 100, 10)
        #act
        self.assertEqual(10, worker.energy)
        worker.work()
        #assert
        self.assertEqual(self.assertEqual(9, worker.energy))

    def test_get_info(self):
        #arrange
        worker = Worker("Sam", 100, 10)
        result = worker.get_info()
        expected =  "Sam has saved 0 money"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()




