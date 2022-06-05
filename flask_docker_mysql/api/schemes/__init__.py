from . position import position
from .vehicles import vehicle

class schemes:

    def __init__(self) -> None:
        pass

    def create_vehicle_scheme(self):
        new_vehicle = vehicle()
        return new_vehicle

    def create_position_scheme(self):
        new_position = position()
        return new_position
        
schemes_factory = schemes()