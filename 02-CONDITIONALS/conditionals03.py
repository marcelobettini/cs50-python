x = round(float(input("What's x? ")),2)
print(x)
y = round(float(input("What's y? ")),2)
print(y)
if x > y:
    result = f'{x} is greater than {y}'
elif x < y:
    result = f'{x} is smaller than {y}'
else:
    result = f'{x} and {y} are equals'

print(result)