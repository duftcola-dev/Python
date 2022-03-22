# Singleton pattern . The Singleton patter is a creational pattern
# The goal of the singleton patter is to create a class which instance can only
# instantiate once.
# This is usefull when it comes to parts of your app that should only
# be located in one place like for example a database driver.


class Singleton:

    __instance=None

    def __init__(self) -> None:
        
        if self.__instance != None:
            raise Exception("<class instance name here> can only be instanciated once")

        Singleton.__instance=self


    @staticmethod
    def GetInstance():

        if Singleton.__instance == None:
            Singleton()

        return Singleton.__instance


# Lets test the pattern

instance1=Singleton() # no error should happend

instance12=Singleton() # error happends since the class Singleton already was instanciated once