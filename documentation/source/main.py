# the goal of this excercise is how to generate documentation in a proper manner

"""
Houses class
------------
Description : 
    Contains a list of houses.
    Houses can be added or pulled out of the list.
------------
Methods:
    - pop_house : Pulls a house from the list
    - add_new_house : Adds a new house to the list
------------
Exceptions:
    **No exceptions for this class
"""

class houses:
    
    def __init__(self,houses:list = None) -> None:
        self.houses = houses

    
    def pop_house(self,house)->str:
        """
        Description:
            Pulls houses form the house list one by one.
        ------------
        Returns:
            - house:str
        ------------
        Exception:
            - No Exeptions
        """
        result = None
      
        if house in self.houses:
            for i in enumerate(self.houses):
                if house == i[1]:
                    result = self.houses.pop(i[0])
                    return result
        else:
            return False
    
    def add_new_house(self,house):
        """
        Description:
            Adds a new house to the house list
        -----------
        Returns :
            - None
        -----------
        Exception:
            - No Exceptions
        """
        self.houses.append(house)
    

real_state  = houses(["house1","house2","house3","house4","house5"])
real_state.add_new_house("houes6")
house = real_state.pop_house("house1")
print(house)