# a. Read the file "show_version.txt" (in the current directory). Remember the VS Code file
# location issue.

# b. Read in the contents of the file using the readlines() method. This will create a list.

# c. Print the length of the list. This will give you the number of lines in that file.

# d. Print out lines number 1 and 35 respectively. Which indices are these?

# e. Split line number1 into fields using a comma as the field separator. One of these fields
# should be OS Version. Print this to standard output.

with open("show_version.txt") as show_version:
    file_output = read(show_version)
