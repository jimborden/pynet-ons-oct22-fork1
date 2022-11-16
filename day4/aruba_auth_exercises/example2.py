import aruba_auth
import requests
import rich


session = requests.Session()
host = "10.5.235.12"
api_port = 4343

uid_aruba = aruba_auth.auth(session, host=host)
uid_aruba_qs = f"UIDARUBA={uid_aruba}"

base_url = f"https://{host}:{api_port}/v1/configuration/"

command = "show+vlan"
relative_url = f"showcommand?command={command}&{uid_aruba_qs}"
full_url = f"{base_url}{relative_url}"

response = session.get(full_url, verify=False)
data = response.json()

rich.print(type(data))
rich.print(data)
