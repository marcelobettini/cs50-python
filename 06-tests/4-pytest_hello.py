from hello import hello
def test_default():
    assert hello() == "hello, world"

def test_arguments():
    assert hello("Marcelo") == "hello, Marcelo"