from ariadne import gql, load_schema_from_path,QueryType,make_executable_schema,ObjectType,MutationType
from ariadne.asgi import GraphQL

type_defs = """
    type Query {
        isAuthenticated: Boolean!
    }

    type Mutation {
        login(username: String!, password: String!): Boolean!
        logout: Boolean!
        user_data(username:String!):UserData
        custom_user(input:custom_type!):custom_payload
    }
    
    type UserData{
        username: String!
        email: String!
        tel: Int!
        date: Int! 
    }
    
    input custom_type{
        user: String!
        id: String!
    }
    type custom_payload{
        result: Boolean!
    }
"""

# create mutations :
# mutations are eant to be functions that write or edit data in our database
# the idea is that the write privilege is reserved for mutations
# and the read privilege is reseved for queries

query = ObjectType("Query")

#two ways of binding mutations

# 1)
mutation = MutationType() # or ObjectType("Mutation")

@mutation.field("login")
def resolve_login(_, info, username=None, password=None):
    request = info.context["request"]
    if username is not None and password is not None:
        #tipically here we would validate the user in our database
        return True
    return False

@mutation.field("user_data")
def resolve_userdata(_,info,username = None):
    if username is not None:
        return {
            "username":"Robin",
            "email":"robinviera@homtail.com",
            "tel": 60010231,
            "date":20020312
            }

@mutation.field("custom_user")
def resolve_user(_,info,input):
    if input["user"] is not None and input["id"] is not None:
        return {
            "result":True
        }

def resolve_logout(_, info):
    request = info.context["request"]
    return True

# 2) 
mutation.set_field("logout", resolve_logout)

# example spected query schema :
# mutation {
#   login(username:"Robin",password:"Robin123")
# 	logout
#   user_data(username:"Robin"){
#     username
#     email
#     tel
#     date
#   }
# 	custom_user(input:{user:"Andy",id:"1234"}){
#     result
#   }
# }


schema = make_executable_schema(type_defs,query,mutation)
app = GraphQL(schema,debug=True)


    