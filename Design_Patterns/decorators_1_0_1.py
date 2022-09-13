# inner functions 
from typing import Tuple


def parent():
    print("Parent function")
    def child():
        print("Child function")
    child()

#-----------------------------------------------

#Inner function with argument 
def parent1(arg):
    print("Parent function")
    def child(arg):
        print(f"Child function : {arg}")
    child(arg)

#---------------------------------------------------

#Parent function returning inner function
def parent2():
    print("Parent function")
    def child():
        print(f"Returning child function")
    return child

#-------------------------------------------------------

#Inner function with wrapper 
#The wrapper is returned as a variable the executes a function
def parent3(func):
    def wrapper():
        func()
    return wrapper

#----------------------------------------------------------

# sintactic sugar
def add_name(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper

#-------------------------------------------------------------
        

# Inner function
parent()
# Inner function with arg
parent1("Robin")
# Parent function returning inner function
child=parent2()
child()
# Inner function with wrapper 
def OuterFuction():
    print("Hi!")

result=parent3(OuterFuction)
result()
# parent3(OuterFuction)() # This is also works

@add_name
def SayName(name,surname):
    print(f"hello {name} {surname}")

SayName("Robin","Viera")


#---------------------------------------------

# function with args
def filter_name(func):
    def wrapper(*args,**kwargs):
        if args[0] != "Robin":
            return func(None,**kwargs)
        else:
            return func(*args,**kwargs)
    return wrapper

@filter_name
def reverse(string)->str:
    if string is None:
        return None
    temp:list=[]
    for char in string:
        temp.insert(0,char)
    return "".join(temp)

result=reverse("Robin")
print(result)


# decorator with args + function with args
def filter_name2(name):
    def super_wrapper(func):
        def wrapper(*args,**kwargs):
            if args[0] != name:
                return func(None,**kwargs)
            else:
                return func(*args,**kwargs)
        return wrapper
    return super_wrapper

@filter_name2("Robi")
def reverse(string)->str:
    if string is None:
        return None
    temp:list=[]
    for char in string:
        temp.insert(0,char)
    return "".join(temp)

result=reverse("Robin")
print(result)


# decorator with n arguments + function with n arguments 
def filter_name3(*d_args,**d_kargs):
    def super_wrapper(func):
        def wrapper(*args,**kwargs):
            temp=[]
            for a in d_args:
                if not isinstance(a,str):
                    temp.append(str(a))
                else:
                    temp.append(a)
                   
            temp=tuple(temp)
            if temp:
                return func(*temp,**kwargs)
            else:
                func(*args,**kwargs)
            return func(*args,**kwargs)

        return wrapper 
    return super_wrapper

@filter_name3("payload",12)
def endpoint(payload,token):
    return payload+token


result = endpoint("payload","token")
print(result)
    






        
