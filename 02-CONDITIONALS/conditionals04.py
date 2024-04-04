import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
       os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')

# Call the function to clear the screen
clear_screen()


score = int(input("Enter score (min 0 - max 100): "))
if score <0 or score >100:
    print("Error, score must be a positive number between 0 and 100")
elif score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# concise and cleaner implicit AND, flipping first condition

if score < 0 or score > 100:
    print("Error, score must be a positive number between 0 and 100")
elif 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# better, just checking lower bound
if score < 0 or score > 100:
    print("Error, score must be a positive number between 0 and 100")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    