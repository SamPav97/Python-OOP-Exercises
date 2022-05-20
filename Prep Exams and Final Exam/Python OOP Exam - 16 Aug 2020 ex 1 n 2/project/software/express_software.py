
from project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        #Make sure that int floors down to lowest int.
        super().__init__(name, "Express", capacity_consumption, int(memory_consumption*2))
