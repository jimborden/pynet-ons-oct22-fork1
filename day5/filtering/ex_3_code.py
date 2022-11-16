import requests
import json
import rich
from aruba_auth import auth, get_request_filter


host = "10.5.235.12"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host)

relative_url = "object/int_gig"
config_path = "/md/40Lab/VH/20:4c:03:39:5a:fc"
filter_str = ""
