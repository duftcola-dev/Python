from message import Message,MessageType
from service import IOTService
from devices import Light,SmartSpeaker,SmartToiledt
import asyncio


async def main():

    #create service
    iot_service = IOTService()


    #create devices
    light = Light()
    speaker = SmartSpeaker()
    toilet = SmartToiledt()


    #register devices
    # this code is still executed in secuence and is not very efficient

    # light_id = await iot_service.register_device(light)
    # speaker_id = await iot_service.register_device(speaker)
    # toilet_id = await iot_service.register_device(toilet)
   
 # speed up the code by gathering tasks // gather actually runs things in paralell
 # gather itself is an async function so it needs await 
    light_id , speaker_id ,toilet_id = await  asyncio.gather(
        iot_service.register_device(light),
        iot_service.register_device(speaker),
        iot_service.register_device(toilet) 
    )

    #create program
    wake_up=[
            Message(light_id,MessageType.SWITCH_ON,""),
            Message(speaker_id,MessageType.SWITCH_ON,""),
            Message(toilet_id,MessageType.SWITCH_ON,"Lucy in the sky with diamons")
        ]

    shut_down = [
            Message(light_id,MessageType.SWITCH_OFF,""),
            Message(speaker_id,MessageType.SWITCH_OFF,""),
            Message(toilet_id,MessageType.SWITCH_OFF,"")
    ]

    # right now the code still exceutes in secuence which is not very efficient
    # await iot_service.run_program(wake_up)
    # await iot_service.run_program(shut_down)

    # speed up the code by gathering tasks // gather actually runs things in paralell
    # gather itself is an async function so it needs await 
    await asyncio.gather(
        iot_service.run_program(wake_up),
        iot_service.run_program(shut_down)
    )

if __name__ == "__main__":

    asyncio.run(main()) # run async task