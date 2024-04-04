def main():
    print(f'x is {get_int()}')
# a function with no side effect (print) but with a value return

# 1
# def get_int():
#     while True:
#         try:
#             x = int(input("What's the number? "))
#             break
#         except ValueError:
#             print("You've entered not an integer...")
#     return x
# 2
# def get_int():
#     while True:
#         try:
#             x = int(input("What's the number? "))
#             return x
#         except ValueError:
#             print("You've entered not an integer...")

# 3
# def get_int():
#     while True:
#         try:
#             return int(input("What's the number? "))
#         except ValueError:
#             print("You've entered not an integer...")
# 4 (pass, catch the exception without printing an error message)
def get_int():
    while True:
        try:
            return int(input("What's the number? "))
        except ValueError:
            pass

main()

