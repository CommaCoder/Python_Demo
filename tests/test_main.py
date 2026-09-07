from src.python_demo.utils.helper import say_hello

def test_say_hello():
    result=say_hello("Python")
    assert result =="Hello,Python"