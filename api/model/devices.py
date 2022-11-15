from pydantic import BaseModel

class Device(BaseModel):
    id: str | None = None
    name: str
    hardware_version: str
    software_version: str
