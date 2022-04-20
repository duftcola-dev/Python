# using resolvers with arguments
import datetime
from ariadne import gql, load_schema_from_path,QueryType,make_executable_schema,ObjectType
from ariadne.asgi import GraphQL

type_defs = """
    type Query {
        holidays(year: Int): [String]!
    }
"""

query = ObjectType("Query")
#spected query 
# {	
#   	holidays(year:2022)
# }

@query.field("holidays")
def resolve_holidays(*_,year=None)->list: #holidays(year: Int): [String]! spects a list
    date = datetime.datetime.now()
    if year is not None:
        return [str(date.year)]
    return ["No dates available"]

schema = make_executable_schema(type_defs, query)

app = GraphQL(schema,debug=True)