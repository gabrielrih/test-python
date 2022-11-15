from model.devices import Device
from util.generator import generate_unique_id
from data.devices import devices


# It creates a fake device
def create_device(device: Device):
    if not device.id:
        device.id = generate_unique_id()
    print(device.dict())

# Gets a single device from a fake list
def get_device(device_id: str):
    return devices[device_id]

# Returns all devices from a fake list
def get_all_devices():
    return devices