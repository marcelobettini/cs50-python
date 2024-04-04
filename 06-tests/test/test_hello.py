# pytest test, being in the upper directory, will run each test in this file and other test files in the test folder. If in test folder, just pytest
from hello import hello
def test_default():
    assert hello() == "hello, world"

def test_arguments():
    assert hello("Marcelo") == "hello, Marcelo"