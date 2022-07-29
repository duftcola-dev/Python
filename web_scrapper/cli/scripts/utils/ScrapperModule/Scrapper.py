from bs4 import BeautifulSoup
import click
import re
class Scrapper : 

    def __init__(self,request:object,) -> None:
        self.request= request
        self.url = ""
      


    def start(self,url:str,n:int=None):
        self.url=url
        self.n=3
        self.it=0
        self.urls=[]
        self.__scrapp(url)
        self.__show()
    

    def __scrapp(self,url:set):
      
        response = self.request.Get(url)
        soup = BeautifulSoup(response["text"],"html.parser")
        for links in soup.find_all("a"):
            link_url = links.get("href")
            if self.url in link_url:
                if self.it == self.n:
                    self.it=0
                    continue
                elif link_url not in self.urls:
                    self.urls.append(link_url)
                    self.it+=1
                    self.__scrapp(link_url)
                
       
    def __show(self):
    
        prev_count = len(re.findall("/",self.url))-2
        index_zero=prev_count
        letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letters_index = 0
        letters_index_subindex=0
        subitem=0
        subsubitem=0
        self.urls.insert(0,self.url)

        for item in self.urls:
            count =  len(re.findall("/",item))-2
            spaces = " "*count
            letter = letters[letters_index]
            string=""
            if count == prev_count:
                subitem=subitem+1
            else:
                if count == index_zero:
                    if (letters_index +1) < len(letters):
                        letters_index = letters_index+1
                        letter = letters[letters_index]
                    else:
                        letters_index = 0
                        letters_index_subindex = letters_index_subindex +1
            if letters_index_subindex > 0 :
                string=f"{spaces}---{item}-{letter}{letters_index_subindex}"
            else:
                string=f"{spaces}---{item}-{letter}"
            if count > prev_count and prev_count > index_zero:
                subsubitem=subsubitem+1
            if count < prev_count:
                subitem=0
                subsubitem=0

            string=string+"-"+str(subitem)
            string=string+"-"+str(subsubitem)
            print(string)
            prev_count=count

                
    def reset(self):
        self.url = ""
        self.urls=[]
        self.url_count=0
        self.urls_index=0
        self.urls_lenght=0
        