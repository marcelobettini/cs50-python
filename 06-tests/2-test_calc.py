from calc import square
def main():
    test_square()

# first version
# def test_square():
#     if square(2) != 4:
#         print("Fail: 2 squared was not 4")
#     if square(3) != 9:
#         print("Fail: 3 squared was not 9")

# assert is best than if and more testing specific, though not very user friendly when prompting test failures    
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9

# more user friendly, but became long again
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("Fail: 2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("Fail: 3 squared was not 9")

if __name__ == '__main__':
    main()