class HouseType1():

    def __init__(self) -> None:
        self.parts=[]

    def add(self,part:str):
        self.parts.append(part)

    def list_parts(self)->None:
        print(self.parts)
