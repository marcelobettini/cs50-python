def compareTwoNumbers(n1,n2):
    
    if isEqual(n1,n2):
        return f'Numbers {n1} and {n2} are equals'
    else:
        return f'Numbers {n1} and {n2} are not equals'
def isEqual(n1, n2):
    return n1 == n2

x = input("What's x? ")
y = input("What's y? ")
print(compareTwoNumbers(x,y))