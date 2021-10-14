
import threading
import datetime
import sys

from .src.Logs import Logs
from .src._CheckType import CheckType


@CheckType
def GetLogInstance(log_file_path=""):

    logs=Logs(log_file=log_file_path)

    return logs


@CheckType
def LogMessage(message:str):

    x=datetime.datetime.now()
    Year=str(x.year)
    Month=str(x.month)
    Day=str(x.day)
    Hour=str(x.hour)
    Minute=str(x.minute)
    Second=str(x.second)
    
    message=Day+"|"+Month+"|"+Year+" - "+Hour+":"+Minute+":"+Second+" | "+message+"\n"

    sys.stdout.write(message)


