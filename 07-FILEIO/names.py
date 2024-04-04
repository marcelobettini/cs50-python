names = []
for _ in range(1):
    names.append(input("What's your name? "))

# file = open("./names.txt", "a")
# for name in sorted(names):
#     file.write(f'{name} \n')
# file.close()

# no need for a specific close(), very useful to avoid problems in long codebase, prone to forget the file closing or introducing some other bug
with open("./names.txt", "a") as file:
    for name in sorted(names):
        file.write(f'{name} \n')

with open("./names.txt", "r") as file:
    for line in sorted(file, reverse=True):
        print(line.rstrip())


    #   lines = file.readlines()
    # for line in sorted(lines):
        # print(line, end='')