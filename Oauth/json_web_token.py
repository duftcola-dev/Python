import jwt


secret = "qwerty123uhiu123iuihis87s8a"
token = {
    "data": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjAxZDViZjBlMTI1OWYxNmMwMzU4NDMxOGZjYmVlNjczYTkxMmYxM2E4ZjhhOWZmYjE1ZTk0NWZjZWE1Yjc3NzYxMjA2YWQ4MTBjNDA1MDE2YjMzZGNlM2Q0NTQ5NzRjOWEyMDc2OGVkZTg1ZTE4ZDk0NTMxZTVmNTgyYWI1Y2I2IiwiaWF0IjoxNjQ2MDgyODM3LCJleHAiOjE2NDYxNTQ4Mzd9.0NbFRauhqvqyd8ShgRb-qb6LCBYwtX7YcUEmqJ7oA6c"
}
content = jwt.decode(token["data"],secret,algorithms=["HS256"])
print(content)