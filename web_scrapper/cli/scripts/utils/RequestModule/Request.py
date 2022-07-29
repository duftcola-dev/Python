import requests
import json
from typing import Optional,Tuple
from requests import HTTPError
from json import JSONDecodeError
from .Source.Meta_Request import IRequest



class Request(IRequest):

    """General purpose http module.

    Author : Robin Viera
    Date : 29/09/2021
    Version : 2.0
    Tested : no
    last update : 6/12/2021
    
    Description
    -----------

        General purpose http request module.
        The module is quite simple to use. It accepts 4 types of operations so far.
        `This module is a singleton and can only be implemented once.`

        - Get
        - Post
        - Put
        - Ping

    Ping is a GET method for testing connections urls.
    Parameres for GET are optional.

    The class accepts a configuration in the form of dict passed as optional
    parameter.Use the GetConfigurationField() to get the name of the exact field 
    in the configuration file this class requires:
    
    The class acccepts a log message instance passed as optional parameter.

    Parameters
    ----------
    
    - log : log_message_instance (optional)
        Instance of log message class.

    Raises
    ------

    - Custom exception Exception .  Error during get FullResponse.

    - JSONDecodeError . Error during json response.

    - Custom exception Exception . Unknown error during handling of json response.


    """


    __instance=None

    def __init__(self,json_response:bool = True, log:Optional[object] = None) -> None:

        if Request.__instance != None:
            raise Exception("Request instance can only be implemented once!")
    
        self.__json_response : bool=json_response
        self.__logs=log
        Request.__instance=self


    @staticmethod
    def GetInstance():
        if Request.__instance==None:
            Request()
        
        return Request.__instance


    def Ping(self,url:str):
        """Test if a connection works or an url exists. Returns False if status is 404 or request fails"""

        return self.__PING(url)


    def Get(self,url:str,header : Optional[dict] = None, query_params : Optional[dict] = None)->dict:

        response=self.__GET(url,header=header,params=query_params)
        return self.__ResponseHandler(response)


    def Post(self,url:str,data : dict, header : Optional[dict] = None)->dict:
        data = json.dumps(data)
        response=self.__POST(url,data = data, header = header)
        return self.__ResponseHandler(response)




    def __PING(self,url:str):
        
        result=None
        try:
            result=requests.get(url)

            if result != None or result.status_code != 404 :
                return True
                
        except HTTPError as httpError: 

            return False

        except Exception:

            return False




    def __GET(self,url:str,header:dict=None,params:dict=None):

        response=""
        if params==None :
                response=requests.get(url)
        else:
            if header==None:
                self.__LogMessage("info",f"request : {url} {params}")
                response=requests.get(url,params=params)
            else:
                self.__LogMessage("info",f" request : headers:{header} | uri: {url} | params : {params}")
                response=requests.get(url,headers=header,params=params)
        
        return response




    def __POST(self,url:str, data:dict = None, header:dict = None):

        response=""
        self.__LogMessage("info",f" request : headers:{header} | uri: {url} | params : {data}")
        response=requests.post(url,data = data, json = data , headers= header)

        return response




    def __ResponseHandler(self,response):

        response_content=None

        if self.__json_response==True:
            response_content=self.__GetJsonContent(response)
        else:
            response_content=self.__GetFullResponse(response)

        return response_content


    def __GetFullResponse(self,response)->dict:

        try:

            result={}
            result["status"]=response.status_code
            result["url"]=response.url
            result["text"]=response.text
            result["encoding"]=response.encoding
            result["bcontent"]=response.content
            if result["encoding"] != None:
                result["content"]=response.content.decode(response.encoding)
            else:
                result["content"]=response.content
            return result

        except Exception as err:
            self.__LogMessage("error",f"Error while formating response : {err}")
            return False
        


    def __GetJsonContent(self,response)->dict:

        try:
    
            self.__LogMessage("info",f"response : {response.status_code}")
            result=response.json()
            return result

        except JSONDecodeError:

            self.__LogMessage("error","Request module -> Response may be not json type")
            return False

        except Exception:

            self.__LogMessage("error","Request module -> Unknown error on json decoding operation")
            return False


    def __LogMessage(self,message_type,message):

        if self.__logs==None:
            print(message+"\n")
        else:
            self.__logs.LogMessage(message_type,message)



