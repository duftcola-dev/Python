#Adapter design pattern.
# The adapter desing pattern  allows two or more instances with interfaces or incomplatible
# data to work together

# we have a class that handles integers
class Intergers:

    def ReturnInterger(self)->int:

        return 12345

# has you can see the class strings only admits string therefore we need
# an adapter for the tow of them to work together
class Strings:

    def PrintString(self,data:str):

        if type(data) is not str:
            raise Exception("This class only allows string!")
        print(data)

#The adapter uses python hability for multiple inheritance to warp the 
# two incomplatible classes  
class Adapter(Intergers,Strings):

    def __init__(self) -> None:
        super().__init__()

    def ConvertToString(self):

        value=self.ReturnInterger()
        value = str(value)
        self.PrintString(value)

new_adapter=Adapter()
new_adapter.ConvertToString()