message = input("What's your name? ").strip().upper()

def sayHello(a):
    print("Hello",a,"\ngreat to see ya here!")


# override print param end with a single space and no Carriage Return
# (default is CR)
# We can also override sep param
# and we can use escape character \ to print double quotes without changing
# the outer quotes to single...

def sayHelloNoCR(a):
    print('Hello', end=' ')
    print(a)
    print("here we change \"separator\": Hello".capitalize(),a,sep="-> ")


sayHello(message)

sayHelloNoCR(message)
name = "Eduardo"
# tell Python this is a "formated" string
print(f"hi {name} with an initial f and curly braces for variable")
ttl = "     París era una fiesta   "
print(ttl.strip().title())

# split a string
fullName = "Marcelo Bettini"
first, last = fullName.split(" ")
print(f"Your name is {first}")
print(f"Your surname is {last}")