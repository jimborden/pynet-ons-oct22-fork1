class NetworkDevice:
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        # you don't need to pass variables, you can set it as static
        self.vendor = "Aruba"

    def print_ip(self):
        print(f"My IP Address: {self.ip_addr}")

    def print_creds(self):
        print(f"The Username is: {self.username}")
        print(f"The Password is: {self.password}")


rtr1 = NetworkDevice("1.1.1.1", username="admin", password="whatever")
rtr2 = NetworkDevice("1.1.1.2", username="admin", password="whatever")
rtr3 = NetworkDevice("1.1.1.3", username="admin", password="whatever")
rtr4 = NetworkDevice("1.1.1.4", username="admin", password="whatever")

rtr4.print_ip()
rtr4.print_creds()
