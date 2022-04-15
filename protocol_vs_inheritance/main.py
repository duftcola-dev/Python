from devices import Light,Speaker,Kitchen_os,SmartCooker
from device import Device
from service import IOT_Service


def get_status(device:Device):
    device.status_update()

def main():
    service = IOT_Service()

    light = Light()
    speaker = Speaker()
    kitchen = Kitchen_os()
    cooker = SmartCooker()

    
    get_status(light)
    get_status(speaker)
    get_status(kitchen)
    get_status(cooker)
    light_id = service.register_device(light)# uses inheritance with ABC
    speaker_id = service.register_device(speaker)# uses inheritance with ABC

    kitchen_id = service.register_device(kitchen)# uses protocols 
    cooker_id = service.register_device(cooker)# uses protocols 

    service.run_program(light_id,"Blink Lights")
    service.run_program(speaker_id,"Increase volume")
    service.run_program(kitchen_id,"Turn on Kitchen")
    service.run_program(cooker_id,"Turn on  Cooker")





if __name__ == "__main__":
    main()