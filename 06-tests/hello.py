def main():
    name = input("What is your name? ")
    print(hello(name))

# we wouldn't test side effects, that is why the hello function does not print but returns
def hello(to="world"):
    return f'hello, {to}'

if __name__ == '__main__':
    main()