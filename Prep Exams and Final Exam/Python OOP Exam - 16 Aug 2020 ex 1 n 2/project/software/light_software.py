
from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        #Make sure that int floors down to lowest int.
        super().__init__(name, "Light", int(capacity_consumption + (capacity_consumption*0.50)), int(memory_consumption - (memory_consumption*0.50)))

