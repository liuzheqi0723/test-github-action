from controller.readItem import add_postfix

def test_postfix():
    assert add_postfix("add") == "addpostfix"