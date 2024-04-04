import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    fullName=""
    for i in range((len((sys.argv))-1)):
        fullName += f'{sys.argv[i+1]} '
    print("hello, my name is", fullName)