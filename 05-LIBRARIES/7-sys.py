import sys
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# else:
#     fullName=''
#     for name in sys.argv:
#         fullName += f'{name} '
#     print("hello, my name is", fullName)

# solved problem of first argument with a slice of argv to get a subset of data
# 1 for index 1 and no number to go to the end of the list 
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    fullName=''
    for name in sys.argv[1:]:
        fullName += f'{name} '
    print("hello, my name is", fullName)