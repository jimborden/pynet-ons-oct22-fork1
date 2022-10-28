from rich import print as rich_print

with open("show_ip_int_brief.txt") as ipinfo:
    ip_addr = ipinfo.read()

interface = {}

for line in ip_addr.splitlines():
    if "IP-Address" in line and "Interface" in line:
        continue

    fields = line.split()
    ifn = fields[0]
    ip_address = fields[1]
    protocol_status = fields[4]
    lin_status = fields[5]

    interface[ifn] = {
        "ip address": ip_address,
        "protocol status": protocol_status,
        "line_status": lin_status,
    }

rich_print(interface)
