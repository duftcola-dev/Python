import redis
from Redis_Driver.utils.commands import Commands
from Redis_Driver.utils.client import Client
from Redis_Driver.utils.users import Users
class Driver:

    __instance=None

    def __init__(self) -> None:
        self.__r=None
        if self.__instance is not None:
            raise Exception("Driver can only be instanciated once")
        Driver.__instance=self


    def connect(self,host:str="localhost",port:int=6379,password:str=None,db:int=0)->bool:
        self.__r=redis.Redis(host=host,port=port,password=password,db=db)
        if not self.__r.ping():
            print("Redis connect : Connection to database failed")
        self.commands=Commands(self.__r)
        self.client=Client(self.__r)
        self.users=Users(self.__r)
        return self.__r.ping()


    def close(self)->bool:
        if self.__r == None:
            print("Redis driver : No connection has been stablished with redis")
            return True
        result=self.__r.quit()
        if result:
            self.commands.close()
            self.client.close()
            self.users.close()
            self.__r=None
            return True
        return False


    @staticmethod
    def get_instance():
        if Driver.__instance is None:
            Driver()
        return Driver.__instance
