
#Builder desing pattern.
# The builder patter arises from the need when we a base class to be able
# extend its functionalities without having to create a large amount of subclasses while also
# being very flexible in the type of new functionalities that it needs to adquire.

# example  : 

# We have a class . We need to be able to generate different types of houses without having to spawn many subclases 
# for every possible variation of house. House we need an easy way to scale the base class every time we need a new type of house.

# the builder pattern allows to build complex object step by step piece by piece. This pattern doens allow to access the object
# while in contruction.

# the construction steps for differenct types of objects can be stored in director / manager class


# PROS
# ***use the builder patther when a class has a very large constructor
# ***use the builder patter for different representations of a base class
# ***allows to isolate complex code from the business logic

#CONS
# *** this pattern is only justified for large applications due that the complexity of the code increases


from __future__ import annotations
from abc import ABC,abstractmethod
from typing import Any 

from builder import Builder
from house import HouseType1



# Builder specialized in building houses

class HouseBuilder(Builder):

    def __init__(self) -> None:
        
        self.reset()

    def reset(self)->None:

        self.__product = HouseType1()


    def get_product(self)->HouseType1:

        product=self.__product
        self.reset()
        return product

    def wall(self)->None:
        
        self.__product.add("Wall")


    def door(self)->None:
        
        self.__product.add("Door")
    

    def roof(self)->None:
        
        self.__product.add("Roof")


    def floor(self) -> None:
        
        self.__product.add("Floor")


class Director:

    def __init__(self) -> None:
        
        self.__builder=None


    def get_builder(self)->Builder:

        return self.__builder


    def builder(self,builder:Builder)->None:

        self.__builder=builder


    def build_minimal_house(self):

        self.__builder.floor()


    def build_full_house(self):
        
        self.__builder.floor()
        self.__builder.wall()
        self.__builder.door()
        self.__builder.roof()



#Creation of houses

director=Director() # create a director
new_builder=HouseBuilder() # create a builder with methods to create different variations of the object house

director.builder(new_builder) # set the builder under the director
director.build_full_house()# director tells builder to make a specific type oh house

new_builder.get_product().list_parts() # check what the builder has created