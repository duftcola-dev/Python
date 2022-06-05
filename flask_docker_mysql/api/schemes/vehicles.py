from hashlib import new
from operator import ne
from .templates import template

class vehicle(template):

    def __init__(self) -> None:
        super().__init__()
        self.__item = {
            "id" : "",
            "matricula": "",
            "id_estado" : ""
        }


    def get_item(self,data):
        item = self.__item.copy()
        data = data[0]
        item["id"] = data[0]
        item["matricula"] = data[1]
        item["id_estado"] = data[2]
        return item
   
    
    def get_collection(self,collection):
        new_collection  =[]
        for item in collection:
            new_item = self.__item.copy()
            new_item["id"]= item[0]
            new_item["matricula"]= item[1]
            new_item["id_estado"]= item[2]
            new_collection.append(new_item)
        return new_collection
    

    def clear(self):
        
        self.__item = {
            "id" : "",
            "matricula": "",
            "id_stado" : ""
        }



