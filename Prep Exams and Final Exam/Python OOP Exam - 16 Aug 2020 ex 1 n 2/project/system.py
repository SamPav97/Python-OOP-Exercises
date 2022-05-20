from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        x = PowerHardware(name, capacity, memory)
        System._hardware.append(x)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        x = HeavyHardware(name, capacity, memory)
        System._hardware.append(x)

    @staticmethod
    def check_hardware_there(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware
        else:
            return False

    @staticmethod
    def check_software_there(software_name):
        for software in System._software:
            if software.name == software_name:
                return software
        else:
            return False

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if not System.check_hardware_there(hardware_name):
            return "Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = System.check_hardware_there(hardware_name)
        #Questionable if below works.
        if hardware.install(software):
            System._software.append(software)
        else:
            raise Exception("Software cannot be installed")

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if not System.check_hardware_there(hardware_name):
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = System.check_hardware_there(hardware_name)
        # Questionable if below works.
        if hardware.install(software):
            System._software.append(software)
        else:
            raise Exception("Software cannot be installed")

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        if System.check_hardware_there(hardware_name) and System.check_software_there(software_name):
            software = System.check_software_there(software_name)
            hardware = System.check_hardware_there(hardware_name)

            hardware.uninstall(software)
            #Does below remove it or must I run a for thru the list separately
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def get_mmry_used():
        total = 0
        for software in System._software:
            total += software.memory_consumption
        return total

    @staticmethod
    def get_mmry_available():
        total = 0
        for hardware in System._hardware:
            total += hardware.memory
        return total

    @staticmethod
    def get_capacity_used():
        total = 0
        for software in System._software:
            total += software.capacity_consumption
        return total

    @staticmethod
    def get_capacity_available():
        total = 0
        for hardware in System._hardware:
            total += hardware.capacity
        return total

    @staticmethod
    def analyze():
        res = "System Analysis\n"
        res += f"Hardware Components: {len(System._hardware)}\n"
        res += f"Software Components: {len(System._software)}\n"
        res += f"Total Operational Memory: {System.get_mmry_used()} / {System.get_mmry_available()}\n"
        res += f"Total Capacity Taken: {System.get_capacity_used()} / {System.get_capacity_available()}\n"
        return res.strip()

    @staticmethod
    def system_split():
        final = ""

        for hardware in System._hardware:
            res = ""
            res += f"Hardware Component - {hardware.name}\n"
            res += f"Express Software Components: {len([x for x in hardware.software_components if x.__class__.__name__ == 'ExpressSoftware'])}\n"
            res += f"Light Software Components: {len([x for x in hardware.software_components if x.__class__.__name__ == 'LightSoftware'])}\n"
            res += f"Memory Usage: {hardware.mmry_used()} / {hardware.memory}\n"
            res += f"Capacity Usage: {hardware.cap_used()} / {hardware.capacity}\n"
            res += f"Type: {hardware.hardware_type}\n"
            if len(System._software) == 0:
                res += f"Software Components: None\n"
            else:
                res += f"Software Components: {', '.join([x.name for x in hardware.software_components])}\n"
            final += res
        return final.strip()
