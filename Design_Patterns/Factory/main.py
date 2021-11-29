from abc import ABCMeta,abstractstaticmethod
# Factory pattern .
# The Factory pattern work creating a factory class.
# Instead of creating objects be the new() operator we call methods of the factory class
# the return instances of other classes

# The advantage of this pattern is that the factory class works as and interface
# separating the objects of you code from the code that uses those object.
# Another advantage is the capacity of add new classes without alterating the overall structure of the code.



class DatabaseDriver:

    def __init__(self) -> None:
        pass
    
    def Print(self):

        print("<Class DatabaseDriver>")


class DatabaseField:

    def __init__(self) -> None:
        pass
    
    def Print(self):

        print("<Class DatabaseField>")



class Operators:

    def __init__(self) -> None:
        pass
    
    def Print(self):

        print("<Class operator>")



class FactoryClass:

    def __init__(self) -> None:
        self.db=None # The database driver is created once an kept in the factory to further reuse

    def CreateDatabaseDriver(self):

        self.db=DatabaseDriver()


    def CreateOperators(self):

        operator=Operators()
        return operator


    def CreateDatabaseField(self):

        dbf=DatabaseField()
        return dbf


new_factory=FactoryClass()
new_factory.CreateDatabaseDriver()

new_factory.db.Print()
print(new_factory.CreateDatabaseField())
print(new_factory.CreateOperators())