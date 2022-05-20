from project.software.software import Software


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.capacity_used = capacity
        self.memory = memory
        self.memory_used = memory
        self.software_components = []

    def install(self, software: Software):
        if software.capacity_consumption <= self.capacity_used and software.memory_consumption <= self.memory_used:
            self.software_components.append(software)
            self.capacity_used -= software.capacity_consumption
            self.memory_used -= software.memory_consumption
            return True
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def mmry_used(self):
        total = 0
        for software in self.software_components:
            total += software.memory_consumption
        return total

    def cap_used(self):
        total = 0
        for software in self.software_components:
            total += software.capacity_consumption
        return total

