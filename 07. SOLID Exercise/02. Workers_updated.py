# from abc import ABCMeta, abstractmethod
# import time
#
# class AbstractWorker:
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def work(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Worker(AbstractWorker):
#
#     def work(self):
#         print("I'm normal worker. I'm working.")
#
#     def eat(self):
#         print("Lunch break....(5 secs)")
#         time.sleep(5)
#
# class SuperWorker(AbstractWorker):
#
#     def work(self):
#         print("I'm super worker. I work very hard!")
#
#     def eat(self):
#         print("Lunch break....(3 secs)")
#         time.sleep(3)
#
#
# class Manager:
#
#     def __init__(self):
#         self.worker = None
#
#     def set_worker(self, worker):
#         assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)
#
#         self.worker = worker
#
#     def manage(self):
#         self.worker.work()
#
#     def lunch_break(self):
#         self.worker.eat()
#
# class Robot(AbstractWorker):
#
#     def work(self):
#         print("I'm a robot. I'm working....")
#
#     def eat(self):
#         print("I don't need to eat....")
#
#
# manager = Manager()
# manager.set_worker(Worker())
# manager.manage()
# manager.lunch_break()
#
# manager.set_worker(SuperWorker())
# manager.manage()
# manager.lunch_break()
#
# manager.set_worker(Robot())
# manager.manage()
# manager.lunch_break()
#












from abc import ABC, abstractmethod
import time


class AbstractWorkable(ABC):

    @abstractmethod
    def work(self):
        pass


class AbstractEatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(AbstractWorkable, AbstractEatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorkable, AbstractEatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class ManageWork:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorkable), "`worker` must be of type {}".format(AbstractWorkable)

        self.worker = worker

    def manage(self):
        self.worker.work()


class ManageBreak:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractEatable), "`worker` must be of type {}".format(AbstractEatable)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(AbstractWorkable):

    def work(self):
        print("I'm a robot. I'm working....")


work_manager = ManageWork()
break_manager = ManageBreak()

work_manager.set_worker(Worker())
work_manager.manage()
break_manager.set_worker(Worker())
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.set_worker(SuperWorker())
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
break_manager.set_worker(Robot())
break_manager.lunch_break()
