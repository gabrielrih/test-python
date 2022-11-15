from fastapi import FastAPI, HTTPException

from model.devices import Device
import functions.devices

app = FastAPI()

@app.post("/devices", status_code=201)
def create_device(device: Device):
    functions.devices.create_device(device)
    return device

@app.get("/devices")
#def get_all_devices(skip: int = 0, limit: int = 10):
def get_all_devices():
    return functions.devices.get_all_devices()

@app.get("/devices/{device_id}", response_model=Device)
def get_one_device(device_id: str):
    try:
        return functions.devices.get_device(device_id)
    except:
        raise HTTPException(status_code=404, detail=f"Device id '{device_id}' was not found")
    