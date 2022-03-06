from .templates import template

class position(template):

    def __init__(self) -> None:
        super().__init__()
        self.__position = {
            "id":"",
            "latitud":"",
            "longitud":"",
            "velocidad":"",
            "id_vehiculo":""
        }
    

    def get_item(self):
        self.clear()
        pass
    
    def get_collection(self):
        self.collection = []
        self.clear()
        pass
    

    def clear(self):
        
        self.__position = {
            "id":"",
            "latitud":"",
            "longitud":"",
            "velocidad":"",
            "id_vehiculo":""
        }
