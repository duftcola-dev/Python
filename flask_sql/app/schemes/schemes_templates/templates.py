from ipaddress import collapse_addresses
from abc import ABCMeta, abstractmethod

class template():
    __metaclass__ = ABCMeta
    @classmethod
    def version(self): return "1.0"
    @abstractmethod
    def clear(self): raise NotImplementedError
    def get_item(self): raise NotImplementedError
    def get_collection(self): raise NotImplementedError


