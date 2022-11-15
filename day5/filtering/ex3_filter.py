import requests
import json
import rich
from aruba_auth import auth, get_request_filter


host = "aruba.lasthop.io"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host)

relative_url = "object/int_gig"
config_path = "/md/40Lab/VH/20:4c:03:39:5a:fc"
filter_str = ""

# Initial GET with no filter
response = get_request_filter(
    session,
    host,
    relative_url=relative_url,
    config_path=config_path,
    filter_str=filter_str,
    uid_aruba=uid_aruba,
)
print()
rich.print(response.json())
print()

# Apply the Filter
filter_str = [{"OBJECT": {"$eq": ["int_gig.slot/module/port"]}}]

# Second GET with the filter
response = get_request_filter(
    session,
    host,
    relative_url=relative_url,
    config_path=config_path,
    filter_str=filter_str,
    uid_aruba=uid_aruba,
)
print()
rich.print(response.json())
print()
