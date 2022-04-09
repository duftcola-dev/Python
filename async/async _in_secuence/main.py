import asyncio
from typing import Any, Awaitable

async def run_in_secuence(*functions : Awaitable[Any])->None:

    for function in functions:
        await function

async def run_in_parallel(*functions : Awaitable[Any])->None:

    await asyncio.gather(*functions)


class Device:

    def __init__(self,device_name:str) -> None:
        self.device_name = device_name

    async def Connect(self):
        print(f"Connectin device {self.device_name}")
        await asyncio.sleep(1)
        print(f"Device {self.device_name} connected")


    async def Switch_on_device(self):
        print(f"Switching device {self.device_name} ON")
        await asyncio.sleep(1)
        print("device ON")

    async def Switch_on_off(self):
        print(f"Switching device {self.device_name} ON")
        await asyncio.sleep(1)
        print("device ON")
    
    async def Disconnect(self):
        print(f"Disconnect device {self.device_name}")
        await asyncio.sleep(1)
        print(f"Device {self.device_name} disconnected")

async def main():

    device1 = Device("smarttoilet")
    device2 = Device("smartTv")
    device3 = Device("smartkitchen")



    await run_in_parallel( # running all 3 task i parallel
        run_in_secuence( # each task runs in async in secuence
                device1.Connect(),
                device1.Switch_on_device(),
                device1.Switch_on_off(),
                device1.Disconnect(),
                run_in_secuence( # you can create nested hyerarchies of secuence and parallel procesesss
                    device1.Connect(),
                    device1.Switch_on_device(),
                    device1.Switch_on_off(),
                    device1.Disconnect()
                    )
                ),
        run_in_secuence(
                device2.Connect(),
                device2.Switch_on_device(),
                device2.Switch_on_off(),
                device2.Disconnect()
                ),
        run_in_secuence(
                device3.Connect(),
                device3.Switch_on_device(),
                device3.Switch_on_off(),
                device3.Disconnect()
                )
    )
if __name__ == "__main__":

    asyncio.run(main())