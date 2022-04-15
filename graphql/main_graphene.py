import decimal
from graphene import ObjectType ,Decimal,String,Schema,List,Field



class Simple_Example(ObjectType):

    #defining schema fields
    id = String()
    name = String()
    surname = String()
    all = String()
    number = Decimal()

    def resolve_id(root,info):
        return "10" 
    def resolve_name(root,info):
        return "Robin"
    def resolve_surname(root,info):
        return "Viera"
    def resolve_all(root,info):
        return f" 10 Robin Viera"
    def resolve_number(root,info):
        return decimal.Decimal("10")


#creating schema 
schema = Schema(query=Simple_Example)

#send query
query = '{ id }'
query1 = '{ name }'
query2 = '{ surname }'
query3 = """{
    id 
    name 
    surname
}"""
query4 = '{ all }'
query5 = '{ number }' 

#excute calls to schema
result = schema.execute(query)
print(result.data)
result = schema.execute(query1)
print(result.data)
result = schema.execute(query2)
print(result.data)
result = schema.execute(query3)
print(result.data)
result = schema.execute(query4)
print(result.data)
result = schema.execute(query5)
print(result.data)


class Simple_Example_with_Inputs(ObjectType):

    #defining schema
    id = String(value=String())
    name = String(value=String())
    number = Decimal(value=Decimal())
    sum = Decimal(value=Decimal())


    def resolve_id(root,info,value):
        return value + " id arg"

    def resolve_name(root,info,value):
        return value + " user_name"
    
    def resolve_number(root,info,value):
        return decimal.Decimal(value)

    def resolve_sum(root,info,value):
        return value + decimal.Decimal("10")


schema = Schema(Simple_Example_with_Inputs)

query_with_arg = '{ id(value: "10") }'
query_with_arg1 = '{ name(value: "Robin") }'
query_with_arg2 = '{ number(value: "234") }'
query_with_arg3 = '{ sum(value: "22") }'
query_with_arg4= """
    {
        id(value: "10")
        name(value: "Robin")
        number(value: "234")
        sum(value: "22")
    }

"""

result = schema.execute(query_with_arg)
print(result.data)
result = schema.execute(query_with_arg1)
print(result.data)
result = schema.execute(query_with_arg2)
print(result.data)
result = schema.execute(query_with_arg3)
print(result.data)
result = schema.execute(query_with_arg4)
print(result.data)


class Items_List(ObjectType):

    items = List(String)


    def resolve_items(root,info):

        return ["item1","item2","item3"]

schema  = Schema(Items_List)

query = '{ items }'
result = schema.execute(query)
print(result.data)


class Person(ObjectType):
    name = String()
    surname = String()
    lastname = String()

class Ocupation(ObjectType):
    job = String()


class Complex_Types(ObjectType):
    person = Field(Person)
    occupation = Field(Ocupation)

    def resolve_person(root,info):
        return  {
            "name":"Robin",
            "surname":"Viera",
            "lastname":"Acosta"
        }
    
    def resolve_occupation(root,info):
        return {
            "job":"programmer"
        }

complex_object_query ="""
    {
        person { name surname lastname}
        occupation { job }
    }
"""
schema = Schema(Complex_Types)
result = schema.execute(complex_object_query)
print(result.data)


# Mutation are an object type that defines an input