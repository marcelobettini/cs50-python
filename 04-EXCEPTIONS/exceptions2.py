# catch error on entering other than a number and cycle while NaN
while True:
    try:
        x = int(input("What's the number? "))
    except ValueError:
        print("You've entered not an integer...")
    else:
       break

print(f'x is {x}')

# this is also ok, if first sentence in the try fails, flox control will jump to the except block and break won't be executed, so I'll stay in the while loop.

# while True:
#     try:
#         x = int(input("What's the number? "))
#         break
#     except ValueError:
#         print("You've entered not a number...")

