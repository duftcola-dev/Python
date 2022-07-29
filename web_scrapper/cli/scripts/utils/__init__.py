from .RequestModule.Request import Request
from .ScrapperModule.Scrapper import Scrapper

r = Request(json_response=False)
s = Scrapper(r.GetInstance())