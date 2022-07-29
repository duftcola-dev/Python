from scripts.utils.RequestModule.Request import Request 
from scripts.utils.ScrapperModule.Scrapper import Scrapper
from scripts.utils import r
from bs4 import BeautifulSoup
import pytest
import re

@pytest.fixture 
def request_module():
    return r.GetInstance()
    

def test_request_module(request_module:Request):
    url = "https://realpython.github.io/fake-jobs/"
    response = request_module.Get(url)
    assert response != False


def test_soup(request_module:Request):
    url = "https://realpython.github.io/fake-jobs/"
    response = request_module.Get(url)
    soup = BeautifulSoup(response["text"],"html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))
    assert len(links) > 0
    assert isinstance(links[0],str) == True


def test_scrapper(request_module:Request):
    url = "https://realpython.github.io/fake-jobs/"
    s =  Scrapper(request_module)
    s.start(url)
    assert len(s.urls) > 0 

