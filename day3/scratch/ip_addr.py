def split_ip(ip_addr, message, network):
    print(message)
    print(f"Network is {network}")
    octets = ip_addr.split(".")
    return octets


# whatever my function returns, stuff it into the my_octets variable
my_octets = split_ip(
    ip_addr="1.1.1.9", message="We are splitting an IP address", network="192.168.1"
)
print(my_octets)
# can put positional arguments first and then named arguments
my_octets2 = split_ip("1.1.1.9", "We are splitting an IP address", network="192.168.1")
