# Lists Ex1
# a. Create a list with five strings
# b. Use append to add two strings to the list
# c. Use pop to remove the first element
# d. Find the length of the list
# e. Sort the list
# f. Loop over the list and print both the index and the value.
#   width field.

superlist = ["No", "more", "market", "interventions", "from"]

superlist.append("now")
superlist.append("on")

firstelement = superlist.pop()
print(firstelement)
list_length = len(superlist)
print(list_length)

superlist.sort()

print(superlist)

print()
for index, value in enumerate(superlist):
    print(f"{index:>3} ---- {value:>15}")
print
