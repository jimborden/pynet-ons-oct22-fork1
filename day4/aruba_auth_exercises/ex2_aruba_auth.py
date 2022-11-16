import aruba_auth
import requests

host = "10.5.235.12"
api_port = "4343"
SSL_VERIFY = False

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = aruba_auth.auth(session, host, api_port=api_port)

print(uid_aruba)
