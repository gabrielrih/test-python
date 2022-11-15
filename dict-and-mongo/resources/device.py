class Device:
    def __init__(self,
                 id: str,
                 name: str,
                 hardware_version: str,
                 software_version: str):
        self.id = id
        self.name = name
        self.hardware_version = hardware_version
        self.software_version = software_version

    def get_id(self) -> str:
        return self.id

    def set_id(self, id: str):
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_hardware_version(self) -> str:
        return self.hardware_version

    def set_hardware_version(self, hardware_version: str):
        self.hardware_version = hardware_version

    def get_software_version(self) -> str:
        return self.software_version

    def set_software_version(self, software_version: str):
        self.software_version = software_version
    