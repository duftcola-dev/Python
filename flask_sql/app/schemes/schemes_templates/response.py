class status:
    def __init__(self) -> None:
        self.__status = {
            "server" : "",
            "database" : ""
        }

    def get_scheme(self):
        return self.__status


class response:
    def __init__(self) -> None:
        self.header = ""
        self.status = ""
        self.data = ""
        self.__response = {
            "status":"",
            "header":"",
            "data":"",
        }
    
    def get_scheme(self):
        self.__response = {
            "status":self.status,
            "header":self.header,
            "data":self.data,
        }
        return self.__response
