from ariadne import gql, load_schema_from_path,QueryType,make_executable_schema,ObjectType
from ariadne.asgi import GraphQL
# load schema from file...
schema_data = load_schema_from_path("ariadne_schema.graphql")
type_defs = gql(schema_data)


query = ObjectType("Query")
# query sent in uvicorn  :  { status }
# simple request with no passing arg
@query.field("status")
def resolve_app_status(_):
    return "OK:1"


schema = make_executable_schema(type_defs,query)
app = GraphQL(schema,debug=True)