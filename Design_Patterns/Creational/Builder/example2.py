
class User:
    def __init__(self,name) -> None:
        self.name = name


class UserBuilder:

    def __init__(self,name) -> None:
        self.user = User(name)

    def set_tel(self,arg):
        self.user.telephone = arg
        return self

    def set_address(self,arg):
        self.user.address = arg
        return self

    def set_location(self,arg):
        self.user.location = arg
        return self

    def set_cash(self,arg):
        self.user.cash = arg
        return self

    def build(self):
        return self.user
    
# ++++ the main difference between builder and factory is that 
# factory produces predefined object while in builder we try 
# to customiza the object we are creating
user_builder = UserBuilder("Frank").set_address("lonfres 27").set_location("Barcelona")
user = user_builder.build()
# as you see user only has the params we want and doesnt have those we are not interested in
print(user.name)
print(user.address)
print(user.location)

#or 
print(vars(user))

#or 
print(user.__dict__)
    