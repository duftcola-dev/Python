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
        item = self.__position.copy()
        data = data[0]
        item["id"]= item[0]
        item["latitud"]= item[1]
        item["longitud"]= item[2]
        item["velocidad"]= item[3]
        item["id_vehiculo"]= item[4]
        return item
   
    
    def get_collection(self,collection):
        new_collection  =[]
        for item in collection:
            new_item = self.__position.copy()
            new_item["id"]= item[0]
            new_item["latitud"]= item[1]
            new_item["longitud"]= item[2]
            new_item["velocidad"]= item[3]
            new_item["id_vehiculo"]= item[4]
            new_collection.append(new_item)
        return new_collection
 

    def clear(self):
        
        self.__position = {
            "id":"",
            "latitud":"",
            "longitud":"",
            "velocidad":"",
            "id_vehiculo":""
        }
