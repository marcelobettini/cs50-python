# parity: a number is even or odd
def main():
    number = int(input("Enter number to check it's parity: "))
    if isEven(number):
        print(f'Number {number} is even')
    else:
        print(f'Number {number} is odd')

def isEven(n):
    return n % 2 == 0
# return True if n % 2 == 0 else False

main()