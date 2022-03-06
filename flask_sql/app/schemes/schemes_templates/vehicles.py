from .templates import template

class vehicle(template):

    def __init__(self) -> None:
        super().__init__()
        self.__item = {
            "id" : "",
            "matricula": "",
            "id_stado" : ""
        }


    def get_item(self):
        self.clear()
        pass
    
    def get_collection(self):
        self.collection = []
        self.clear()
        pass
    

    def clear(self):
        
        self.__item = {
            "id" : "",
            "matricula": "",
            "id_stado" : ""
        }



