from src.utils.helper import say_hello


def test_say_hello():
    assert say_hello("Python") == "Hello, Python!"