from abc import ABC, abstractmethod
from typing import Protocol

# Device is an abstract class (an interface used for inheritance)
# abtract base class inheritance works by typing inheritance
# this means we explicitly say a class inherits form Device ...
class Device(ABC):

    @abstractmethod
    def connect(self)->None:
        pass

    @abstractmethod
    def disconnect(self)->None:
        pass

    @abstractmethod
    def send_message(self,message:str)->None:
        pass

    @abstractmethod
    def status_update(self)->None:
        pass

# On the other hand Protocols work by structural inheritance. This means subclasses of protocol
# dont need to specify they inherit from protocol. Instead , they share the same structure :
# the same methods and atributes, and that is how the compiler tells a class inherits from protocol

# PROS
# a big advantage of protocols is that the same protocol can be defined multyple times accros files in
# the same app

#CONS
# with protocols you loose the type checking that comes with abstract classes since protols dont check 
# for type but for structure . 
# You also cannot add new functionalities for the subclasses from the base class
class Aplliance(Protocol):
   
    def connect(self)->None:
        ...

    def disconnect(self)->None:
        ...

    def status_update(self)->None:
        ...

    def send_message(self,message:str)->None:
        ...