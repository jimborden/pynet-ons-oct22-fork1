from getpass import getpass
import requests
import rich

SSL_VERIFY = False
host = "10.5.235.5"


def auth(session, host, api_port=4343):
    username = input("Enter a username:")
    PASSWORD = getpass("Enter Aruba Controller Password:")
    creds = f"username={username}&password={PASSWORD}"

    login_url = f"https://{host}:{api_port}/v1/api/login"
    response = session.post(login_url, data=creds, verify=SSL_VERIFY)
