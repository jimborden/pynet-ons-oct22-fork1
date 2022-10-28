# Read in the “aruba_show_ap_database.txt” file.

# Process the data such that all of the header and footer information is excluded.

# In other words, only print out the tabular data from the file. Your output should look as follows:
from rich import print

f = open("aruba_show_ap_database.txt")
data = f.read()
f.close()

# print(data)

data_lines = data.splitlines()
header = True
footer = False
# specifying dictionary
my_ds = {}
for line in data.splitlines():
    # We are adding two to make sure there are no false positives
    # We can also match if its lower
    if header:
        if "name" in line.lower() and "standby ip" in line.lower():
            header = False
        continue
    elif "----------" in line:
        continue
    elif "Flags:" in line:
        footer = True
        continue
    elif footer:
        continue
    elif "Total APs" in line:
        continue
    elif line.strip() == "":
        continue

    fields = line.split()
    ap_name = fields[0]
    ap_ip_address = fields[3]
    ap_status = fields[4]

    # print(ap_name)
    # print(ap_ip_address)
    # print(ap_status)
    # put a break because we only want to look at the first line
    # break
    my_ds[ap_name] = ap_status

print()
print(my_ds)
print()
