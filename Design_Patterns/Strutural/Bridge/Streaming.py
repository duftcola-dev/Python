import abc 
import uuid

class Protocol(abc.ABC):

    def __init__(self,device) -> None:
        super().__init__()
        self.device = device

    @abc.abstractmethod
    def stop_stream(self):
        pass
    @abc.abstractmethod
    def start_stream(self):
        pass
    @abc.abstractmethod
    def fill_buffer(self):
        pass


class Youtube(Protocol):

    service_name= "Youtube"

    def __init__(self, device) -> None:
        super().__init__(device)
        self.device = device

    def start_stream(self):
        id = uuid.uuid4()
        print(f"{self.service_name} has started -->{id}")
        return id

    def stop_stream(self):
        print(f"{self.service_name} has stoped -->{id}")

    def fill_buffer(self):
        print("Filling buffer : ")
        x=0
        for i in range(100):
            x+=i
        print(f"{x}%\n")

class Discord(Protocol):

    service_name = "Discord"

    def __init__(self, device) -> None:
        super().__init__(device)
        self.device = device

    def start_stream(self):
        id = uuid.uuid4()
        return f"{self.service_name} has started -->{id}"
        return id

    def stop_stream(self):
        return f"{self.service_name} has stoped -->{id}"

    def fill_buffer(self):
        print("Filling buffer : ")
        x=0
        for i in range(100):
            x+=i
        print(f"{x}%\n")
