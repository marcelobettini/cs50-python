x = float(input("What's x? "))
y= float(input("What's y? "))
print(f'{x} + {y} = {round(x+y,2)}')

# int(x) + int(y) for integers with no decimal places
# z = round(x + y)
z = (x + y)
# comma separator every 3 digits plus 2 decimal places
print(f'{z:,.2f}')

# 2 decimal places
print(f'{z:.2f}')