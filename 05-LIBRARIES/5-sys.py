# argument vector -> all values user typed at CLI
from sys import argv
fullName=''
if len(argv)>1:
    for i in range((len((argv))-1)):
        fullName += f'{argv[i+1]} '
    print("hello, my name is", fullName)
else:
    print("Enter your name after file name")

# we must pass the argument to de cli when executing the file
# python3 5-sys.py Marcelo