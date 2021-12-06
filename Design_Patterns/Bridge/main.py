#Bridge design pattern .
# The bredge desin pattern devides de logic of a very big class into hierarchies of smaller classes 
# that can be developed independently.
# The bridege patter is specially usefull to deal with multiplatform apps.
from  __future__ import annotations
from abc import ABC,abstractmethod

class Abstraction:

    """The abstraction defines the control interface of the hierarchy
    """

    def __init__(self,implementation: Implementation) -> None:
        self.implementation=implementation

    def operation(self)->str:

        return (f"Abstraction : {self.implementation}")

    
class ExdendedAbstraction(Abstraction):

    def operation(self) -> str:
        return  (f"Extended abstraction : extended operation {self.implementation}")



class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self):
        pass