def display_output(msg1, msg2):
    print()
    print("#" * 60)
    print(f"msg1: {msg1}")
    print("-" * 60)
    print(f"msg2: {msg2}")
    print("#" * 60)
    print()


display_output("Message1", "Message2")
display_output("Hello", "Something")
# this doesn't have to be in order you can change it to named arguments
display_output(msg2="Hello", msg1="Something")
