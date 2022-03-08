import mysql.connector


class driver:

    __instance =None

    def __init__(self) -> None:

        if driver.__instance != None:
            raise Exception("class driver can only be instanciated once")
        driver.__instance = self

    def get_instance(): 
        if driver.__instance == None:
            driver()
        return driver.__instance

    def ping(self):
        access = None
        access = mysql.connector.connect(
            host="mysql_service",
            user="user",
            password="user",
            port = 3306
        )
        if access != None:
            return True
        access.close()
        return False

    def get_cursor(self,database="docker"):
        db = mysql.connector.connect(
            host="mysql_service",
            user="user",
            password="user",
            port = 3306,
            database = database
        )
        return db
    
