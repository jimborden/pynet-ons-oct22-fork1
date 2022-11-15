class NetworkDevice:
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        # you don't need to pass variables, you can set it as static
        self.vendor = "Aruba"

    def print_ip(self, message):
        print(f"My IP Address: {self.ip_addr}")
        print(message)


rtr1 = NetworkDevice("1.1.1.1", username="admin", password="whatever")
rtr2 = NetworkDevice("1.1.1.2", username="admin", password="whatever")
rtr3 = NetworkDevice("1.1.1.3", username="admin", password="whatever")
rtr4 = NetworkDevice("1.1.1.4", username="admin", password="whatever")

print(f"IP ADDR: {rtr4.ip_addr}")
print(f"USERNAME: {rtr4.username}")
print(f"PASSWORD: {rtr4.password}")
print(rtr4.vendor)

rtr1.print_ip(message="Hello World")
