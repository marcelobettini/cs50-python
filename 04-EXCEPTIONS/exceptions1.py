# catch error on entering other than a number

try:
    x = int(input("What's the number? "))
except ValueError:
    print("You've entered not an integer...")
else:
    print(f'x is {x}')
finally:
    print("This has ended, either with an integer or something else")

# finally will print always...