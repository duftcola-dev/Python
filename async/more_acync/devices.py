from message import MessageType
import asyncio

class Light:

    def __init__(self) -> None:
        pass

    async def connect(self):
        print("Connecting Light")
        await asyncio.sleep(1)
        print("Light connected")
    
    async def disconnect(self):
        print("Deisconnecting light")
        await asyncio.sleep(1)
        print("Light disconnected")

    async def send_message(self,message_type:MessageType,data:str):
        print(f"Light : {message_type.name} with data {data}")
        await asyncio.sleep(1)
        print("Data : sent")

class SmartSpeaker:

    def __init__(self) -> None:
        pass

    async def connect(self):
        print("Connecting SmartSpeaker")
        await asyncio.sleep(2)
        print("SmartSpeaker Connected")
    
    async def disconnect(self):
        print("Deisconnecting SmartSpeaker")
        await asyncio.sleep(1)
        print("SmartSpeaker disconnected")

    async def send_message(self,message_type:MessageType,data:str):
        print(f"SmartSpeaker : {message_type.name} with data {data}")
        await asyncio.sleep(1)
        print("Data : sent")

class SmartToiledt:

    def __init__(self) -> None:
        pass

    async def connect(self):
        print("Connecting SmartToiledt")
        await asyncio.sleep(2)
        print("SmartToiledt Connnected")
    
    async def disconnect(self):
        print("Deisconnecting SmartToiledt")
        await asyncio.sleep(1)
        print("SmartToiledt disconnected")

    async def send_message(self,message_type:MessageType,data:str=""):
        print(f"SmartToiledt : {message_type.name} with data {data}")
        await asyncio.sleep(1)
        print("Data : sent")