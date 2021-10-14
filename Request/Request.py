import requests
from requests import HTTPError
from json import JSONDecodeError
from Source.Meta_Request import IRequest



#Author : Robin Viera
#Date : 29/09/2021
#Version : 1.0
#Tested : No
#Description : Class for general purpose http requests. Singleton class arch.
#last update : 14/10/2021


class Request(IRequest):

    __instance=None

    def __init__(self) -> None:

        if Request.__instance != None:
            raise Exception("Request instance can only be implemented once!")

        self.json_response=False
        Request.__instance=self


    @staticmethod
    def GetInstance():
        if Request.__instance==None:
            Request()
        
        return Request.__instance


    def Ping(self,url:str):

        return self.__PING(url)



    def Get(self,url:str,header:dict=None,data:dict=None)->dict:

        self.__HttpMethods("GET",url,header,data)



    def Post(self,url:str,header:dict=None,data:dict=None)->dict:

        self.__HttpMethods("POST",url,header,data)



    def Put(self,url:str,header:dict=None,data:dict=None)->dict:

        self.__HttpMethods("PUT",url,header,data)




    def __HttpMethods(self,method,url,header,data):

        if self.__CheckTypes(url,data)==False:
            return False
        
        response=""
        if method =="GET":

            self.__GET(url,header=header,data=data)

        if method =="POST":
            
            self.__POST(url,header=header,data=data)

                
        if method =="PUT":

            self.__PUT(url,header=header,data=data)

        if self.json_response==False:

            return self.__FormatResponse(response)
        else:
            return self.__FormatResponseJson(response)




    def __CheckTypes(self,method:str="",url:str="",data:dict=""):


        if method=="" or method == None :#method is mandatory
            return False

        if url == "" or url== None: #url is mandatory
            return False

        if method != "GET" and (data=="" or data==None): # data is only optional for get
            return False
        else:
            if self.__CheckDictType(data)==False:# data must be a dict for POST/PUT
                return False
           
        if self.__CheckUrlType(url)==False:# url must be a string
            return False

        return True




    def __CheckDictType(self,data,datatype:type)->bool:

        if type(data) == datatype:

            return True

        return False




    def __CheckUrlType(self,data:str)->bool:

        if type(data) ==str:

            return True

        return False



    def __PING(self,url:str):
        
        result=None
        try:
            result=requests.get(url)

            if result != None:
                return True
                
        except HTTPError as httpError: 

            return False

        except Exception:

            return False




    def __GET(self,url:str,header:dict=None,data:dict=None):

        response=""
        if data==None :
                response=requests.get(url)
        else:
            if header==None:
                response=requests.get(url,params=data)
            else:
                response=requests.get(url,headers=header,params=data)

        return response




    def __POST(self,url:str,header:dict=None,data:dict=None):

        response=""
        if header==None:
            response=requests.post(url,data=data)
        else:
            response=requests.post(url,headers=header,data=data)

        return response




    def __PUT(self,url:str,header:dict=None,data:dict=None):

        response=""
        if header == None:
            response=requests.put(url,data=data)
        else:
            response=requests.put(url,headers=header,data=data)
        return response




    def __FormatResponse(response)->dict:

        try:

            result={}
            result["status"]=response.status_code
            result["url"]=response.url
            result["text"]=response.text
            result["encoding"]=response.encoding
            result["bcontent"]=response.content
            result["content"]=response.content.decode(response.encoding)

            return result

        except Exception:

            return False
        



    def __FormatResponseJson(response)->dict:

        try:
            result=""
            result=response.json()
            return result

        except requests.exceptions.JSONDecodeError:

            print("Response may be not json type")
            return False
        except Exception:

            print("Unkown error on json decoding operation")
            return False



