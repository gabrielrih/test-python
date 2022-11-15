import uuid

from resources.device import Device
from resources.device_type import DeviceType
from resources.atlas.mongo import Mongo
from resources.util.generator import generate_unique_id

DATABASE_NAME = 'testing'

# Create a test device
sensor_one = Device(
    id = generate_unique_id(),
    name='bathroom_light',
    type=DeviceType.LIGTH.value,a
    hardware_version='0.0.1',
    software_version='1.0.0')

print(sensor_one.__dict__)

# Save it on Mongo database
mongo = Mongo()
mongo.open_connection()
mongo.insert_a_document(DATABASE_NAME, 'devices', sensor_one.__dict__)