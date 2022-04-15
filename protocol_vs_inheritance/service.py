from device import Device
import uuid

class IOT_Service:

    def __init__(self) -> None:
        self.devices : dict[str,Device] = {}

    def register_device(self,device:Device)->str:
        device.connect()
        device_id = str(uuid.uuid4())   
        self.devices[device_id] = device
        return device_id

    def unregister_device(self,device_id:str)->str:   
        self.devices.get(device_id).disconnect()
        self.devices.pop(device_id)
    
    def get_device(self,device_id:str)->Device:
        return self.devices.get(device_id)

    def run_program(self,device_id:str,message:str):
        self.devices.get(device_id).send_message(message)