f = open("show_version.txt")

data = f.read()

for line in data.splitlines():
    if "Processor board ID" in line:
        fields = line.split()
        serial_number = fields[-1]
        print(serial_number)
        # f says that we are going to be embedding a variable into the string the {} tells us what variable we are going to include
        print(f"\n\nSerial Number: {serial_number}\n\n")
        # We can use different values in split command
        _, fields2 = line.split("Processor board ID")
        # _ can mean this is a junk variable  We are junking the first value in the list
        fields3 = line.split()
        _, _, _, serial_number2 = line.split()
        print(fields2)
        print(serial_number2)

f.close()
