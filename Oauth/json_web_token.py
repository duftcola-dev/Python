import jwt


secret = "qwerty123uhiu123iuihis87s8a"
token = {
    "data": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjI4NzM0MTVjNmU4OTc2ODU2MTEyMjljOGZiN2RlNDkyZDhkODJiYTQ1ZWRkY2QzODE2YTRkZDRjOTBkOGMwYzBlMWRmMThiZTkyM2U3OGJlMWRiZjExMjhlOGIwMmIzMjYwM2ZhMjcwYWY1MWJmMTg4ZDE0NzgwMzkyZDhkYmMxIiwiaWF0IjoxNjQ2MjU0NTA1LCJleHAiOjE2NDYzMjY1MDV9.Dgih-aS-YdT3cREs-XfIQ7pIg5rr-AoyfmwUtuwkkL4"
}
content = jwt.decode(token["data"],secret,algorithms=["HS256"])
print(content)