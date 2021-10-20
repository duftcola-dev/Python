from email.mime import text
import os

from .src.IMail import MetaMail
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .src.HtmlBlueprints import GetTemplate


#Author : Robin Viera 
# Date : 20/10/2021
# Descripion : General purpose mailing service . It requires a gmail account available to work properly that
# grants access to external apps (check google documentation) and the password to such account.
# It also requires  a port and an smtp client (check readme file). It can use plain text and html templates though 
# these html templates are kinda tedious to use since using internal <style><style> gives problems and there is no way to
# add an external css file

# Last update : None
# version 1.0
# tested : No



class MailService(MetaMail):

    __instance = None

    def __init__(self, port: int, server_host: str, server_login: str) -> None:

        self.credentials = {}
        self.credentials["port"] = port
        self.credentials["server_host"] = server_host
        self.credentials["server_login"] = server_login

        if MailService.__instance != None:
            raise Exception(
                "Mailing service instance can only be implemented once")

        MailService.__instance = self




    @staticmethod
    def GetInstance():

        if MailService.__instance == None:
            MailService(000, "smtp.gmail.com",
                        "some@gmail.com")

        return MailService.__instance





    def CreateMessage(self, sender: str, receiver: str,subject:str, message: str = "",template:str="formal") -> dict:

        if message == "":
            message = "TEST"

        if type(sender) is not str or type(receiver) is not str:
            print("Failed to create message format. Parameters : sender ,receiver and message must be strings(str)")
            return False

        message_base = MIMEMultipart("alternative")
        message_base["From"] = sender
        message_base["To"] = receiver
        message_base["Subject"] = subject
        
        #add plain text option
        plain_text=MIMEText(message,"plain")

        #get html blueprint from HtmlBlueprints
        html_text=GetTemplate()
        html_text=html_text.format(message)
        html_text=MIMEText(html_text,"html")

        #add options (plaint text and html) to message 
        message_base.attach(plain_text)
        message_base.attach(html_text)

        return message_base





    def SendMessage(self,message: dict,password) -> bool:

        if type(message) is not MIMEMultipart:
            print("Wrong message format . Format must be MIMEMultipart class type")
            return False

        self.__CreateSecureSMTPConnection(self.credentials,message,password)




    def __CreateSecureSMTPConnection(self, credentials: dict, message: dict,password:str) -> smtplib.SMTP_SSL:

        if type(credentials["port"]) is not int:
            return False

        if type(password) is not str and type(credentials["server_host"]) is not str and type(credentials["server_login"]) is not str:
            return False

        if credentials["server_login"].find("@") == -1:

            print("To log into the server an email address is required")
            return False

        context = ssl.create_default_context()

        try:

            server = smtplib.SMTP_SSL(credentials["server_host"], credentials["port"], context=context)
            server.login(credentials["server_login"], password)
            server.sendmail(message["From"],message["To"], message.as_string())

        except smtplib.SMTPHeloError:

            print("Server didnt respond properly")

        except smtplib.SMTPAuthenticationError as err:

            print(f"Server wrong user or password : {err}")

        except Exception as err:

            print(f"Unknown error . Cannot stablish secure connection : {err}")




    def StartDebbugingServer(self, url: str = "localhost", port: int = 1025):

        command = f"python3 -m smtpd -c DebuggingServer -n {url}:{port}"
        print(f"Server online {url}:{port}")
        os.system(command)
