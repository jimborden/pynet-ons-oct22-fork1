from rich import print


def gen_ds(device_name, ip_addr, vendor, platform):
    return {
        "device_name": device_name,
        "ip_addr": ip_addr,
        "vendor": vendor,
        "platform": platform,
    }


# new_ds1 = {
#     "device name": "rtr1",
#     "ip_addr:": "1.1.1.2",
#     "vendor": "Cisco"
#     "platform": "IOS"
# }

new_ds1 = gen_ds("rtr1", "1.1.1.1", "Cisco", "IOS")
new_ds2 = gen_ds("rtr2", "1.1.1.2", "Cisco", "IOS")
new_ds3 = gen_ds("sw1", "1.1.1.21", "Aruba", "Aruba-CX")
new_ds4 = gen_ds("sw2", "1.1.1.22", "Aruba", "Aruba-CX")

my_list = [new_ds1, new_ds2, new_ds3, new_ds4]
print()
print("Entire Data Structure")
print(my_list)
print()

print()
print("Print out last entry")
print(my_list[-1])
print()

print()
print("Print out fields from first entry")
ds1 = my_list[0]
# be careful we have a single quotes around device name here because it would terminate the double quotes
print(f"Device Name: {my_list[0]['device_name']}")
print(f"IP ADDR: {ds1['ip_addr']}")
print()
