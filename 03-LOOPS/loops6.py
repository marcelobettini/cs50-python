def main():
    print_grid_enhanced("🗳️",10)

def print_column(height):
    for _ in range(height):
        print("#")
def print_row(width):   
        print("?" * width)
def print_row_enhanced(char,width):   
        print(char * width)

def print_grid(size):
     # For each row in grid
     for i in range(size):
          # For each brick in row
        for j in range(size):
            print("#", end="")
        print()

def print_grid_enhanced(char, size):
     for _ in range(size):
        print_row_enhanced(char,size)
     
             
main()