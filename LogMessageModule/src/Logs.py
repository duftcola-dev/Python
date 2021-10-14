import sys
import os
import threading
import datetime
from inspect import getframeinfo,currentframe
from .interface.MetaLog import MetaLogMessage

# Author: Robin
# Description : General purpose log message class . Takes 2 string as arguments indicating the message
# and the type of message . Accepts and optional argument indicating and ABSULUTE path to a log file .txt
# The class is meant to be used as a product of a factory method.
# The logs class can be inherited but to so will disable the ability to toutpust messages to a log file
# version 2.0
# tested : yes
# last update: 11/10/2021


class Logs(MetaLogMessage):

    def __init__(self,log_file="") -> None:
        self.log_file=log_file
        pass


    def LogMessage(self,message_type,message):

       self.__LogMessage(message_type,message)
             

    
    def __LogMessage(self,message_type,message):

        self.__type=["warning","error","info"]
    
        if message_type in self.__type:
            
            date=self.__GetDate()

            self.__message=date+" | "+message_type+" | "+message+"\n"
            self.__SaveLogMessage(self.__message,message_type)

            sys.stdout.write(self.__message)




    def __SaveLogMessage(self,message,message_type):
        
        if message_type =="error" and self.log_file != "":

            try:
                file=open(self.log_file,"a")
                file.write(message)
                file.close()
            except FileExistsError:

                sys.stdout.write("ERROR , log class cannot find log file ")

            except Exception as err:

                sys.stdout.write("Log class : Unknown error"+str(err)) 



    def __GetDate(self):
        
        x=datetime.datetime.now()
        Year=str(x.year)
        Month=str(x.month)
        Day=str(x.day)
        Hour=str(x.hour)
        Minute=str(x.minute)
        Second=str(x.second)
        
        return Day+"|"+Month+"|"+Year+" - "+Hour+":"+Minute+":"+Second


