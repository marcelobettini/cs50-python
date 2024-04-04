# dict

studentsDictionary= {
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    "Harry": "Gryffindor",
}

for key in studentsDictionary:
    print(key, studentsDictionary[key], sep=' - ')

# list of dictionaries and None for null values

    studentsList = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
        {"name":"Draco","house":"Slytherin","patronus":None},
        {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell Terrier"},
    ]

for student in studentsList:
    print(student["name"], student["house"], student["patronus"], sep=" - ")
