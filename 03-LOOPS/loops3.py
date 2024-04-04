# first version
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break
# for _ in range(n):
#     print("Miau!!")

# second version
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("Miau!!")

# last version

def main():
    number = getNumber()
    miau(number)

def getNumber():    
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def miau(n):
    for _ in range(n):
        print("Miau!!")

main()