def main():
    height = int(input('Height: '))
    pyramid(height)

def pyramid(n):    
    for i in range(n):
        # first print is for debugging before counter + 1
        # print(i, end=" -> ")
        print('#' * (i + 1))

if __name__ == "__main__":
    main()

# set breakpoint in last line and start altering step into and step over. Step over for lines 2 and 6, because input and for loop are already implemented and we don't want to inspect them internally but execute them. Step into for our own functions. On the left eventually we'll see variables values: height, then n, then i:0