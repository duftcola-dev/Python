# binding resolvers with araidne
from ariadne import gql, load_schema_from_path,QueryType,make_executable_schema,ObjectType
from ariadne.asgi import GraphQL

type_defs = """ 
    type Query {
        hello: String!
        name : String!
        user: User
    }

    type User {
        username: String!
    }
"""

query = ObjectType("Query")
user = ObjectType("User")

#query sent

# {	
#   	hello
#   	name
#   	user { username }

# }

@query.field("hello")
def resolve_hello(*_):
    return "hello world"

@query.field("name")
def resolve_name(*_):
    return "duftcola"

# the field user is necessary to acess the type User
@query.field("user")
def resolver_user(*_):
    return  "weuewdhjhf"

@user.field("username")
def resolve_username(*_):
    return "Robin"


schema = make_executable_schema(type_defs, query,user)

app = GraphQL(schema,debug=True)
    