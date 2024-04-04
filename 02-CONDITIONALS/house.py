name = input("What's your name? ").capitalize()
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco" or name == "Severus" or name == "Bellatrix":
    print("Slytherin")
elif name == "Luna":
    print("Ravenclaw")
elif name == "Cedric":
    print("Hufflepuff")

else:
    print("Who?")
