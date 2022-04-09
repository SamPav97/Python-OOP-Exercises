class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int,
                 workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed = 0
        for worker in self.workers:
            needed += worker.salary
        if needed <= self.__budget:
            self.__budget -= needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        necessary_tending = 0
        for animal in self.animals:
            necessary_tending += animal.money_for_care
        if necessary_tending <= self.__budget:
            self.__budget -= necessary_tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        res = f"You have {len(self.animals)} animals\n"
        lions = [x for x in self.animals if type(x).__name__ == 'Lion']
        res += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            res += f"{lion}\n"
        tigs = [x for x in self.animals if type(x).__name__ == 'Tiger']
        res += f"----- {len(tigs)} Tigers:\n"
        for tig in tigs:
            res += f"{tig}\n"
        cheets = [x for x in self.animals if type(x).__name__ == 'Cheetah']
        res += f"----- {len(tigs)} Cheetahs:\n"
        for cheet in cheets:
            res += f"{cheet}\n"
        return res.strip()

    def workers_status(self):
        res = f"You have {len(self.workers)} workers\n"
        lions = [x for x in self.workers if type(x).__name__ == 'Keeper']
        res += f"----- {len(lions)} Keepers:\n"
        for lion in lions:
            res += f"{lion}\n"
        tigs = [x for x in self.workers if type(x).__name__ == 'Caretaker']
        res += f"----- {len(tigs)} Caretakers:\n"
        for tig in tigs:
            res += f"{tig}\n"
        cheets = [x for x in self.workers if type(x).__name__ == 'Vet']
        res += f"----- {len(cheets)} Vets:\n"
        for cheet in cheets:
            res += f"{cheet}\n"
        return res.strip()
