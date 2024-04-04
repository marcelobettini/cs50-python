from email.policy import default


name = input("What's your name? ").capitalize()
match name:
    case "Harry" | "Hermione" | "Ron":
     print("Gryffindor")
    case "Draco" | "Severus" | "Bellatrix":
        print("Slytherin")
    case "Luna":
        print("Ravenclaw")
    case "Cedric":
        print("Hufflepuff")
    case _:
        print("Who?")
