import os
def main():  
    clear_screen()

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')

# Call the function to clear the screen if the file clear.py is executed
# via cli instead of using it as an imported package in other module.
# Python assigns __name__ the name "__main__" when executed via the container file
if __name__ == "__main__":
    main()
