from device import Device

# inheritance from abstract class Device
class Light(Device):

    def __init__(self) -> None:
        super().__init__()

    def connect(self) -> None:
        print("Connectin lights")
    
    def disconnect(self) -> None:
        print("Disconnecting lights")

    def send_message(self, message: str) -> None:
        print(f"Lights  : {message}") 

    def status_update(self) -> None:
        return "Lights status : OK"


class Speaker(Device):

    def __init__(self) -> None:
        super().__init__()

    def connect(self) -> None:
        print("Connectin speaker")
    
    def disconnect(self) -> None:
        print("Disconnecting speaker")

    def send_message(self, message: str) -> None:
        print(f"Speaker  : {message}") 

    def status_update(self) -> None:
        return "Speaker status : OK"



# protocol Aplliance
# notice we never specify these 2 classes inherits from protocol.
# the interpreted can already tell that by the structure they share
class Kitchen_os:

    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        print("Connectin KitchenOS")
    
    def disconnect(self) -> None:
        print("Disconnecting KitchenOS")

    def status_update(self) -> None:
        return "KitchenOS status : OK"
    
    def send_message(self, message: str) -> None:
        print(f"KitchenOS  : {message}") 

class SmartCooker:

    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        print("Connectin SmartCooker")
    
    def disconnect(self) -> None:
        print("Disconnecting SmartCooker")

    def status_update(self) -> None:
        return "SmartCooker status : OK"
    
    def send_message(self, message: str) -> None:
        print(f"SmartCooker  : {message}") 