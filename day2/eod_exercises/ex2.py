from rich import print

with open("show_vlan.txt") as vlan_file:
    vlan_data = vlan_file.read()

my_ds = {}
for line in vlan_data.splitlines():
    if "Name" in line or "--------------------------------" in line:
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_status = fields[2]
    # this is a list slice
    ports = fields[3:]

    my_ds[vlan_id] = {}
    my_ds[vlan_id]["vlan_name"] = vlan_name
    my_ds[vlan_id]["vlan_status"] = vlan_status
    my_ds[vlan_id]["ports"] = ports

    # can also do
    # my_ds[vlan_id] = {
    # "vlan_name": vlan_name,
    # "vlan_status": vlan_name,
    # "ports": ports
    # }


print(my_ds)
