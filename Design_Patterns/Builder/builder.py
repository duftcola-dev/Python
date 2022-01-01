from abc import ABC,abstractmethod

class Builder(ABC):

    @property
    @abstractmethod
    def get_product(self)->None:
        pass

    @abstractmethod
    def wall(self)->None:
        pass

    @abstractmethod
    def door(self)->None:
        pass
    
    @abstractmethod
    def roof(self)->None:
        pass

    def floor(self)->None:
        pass