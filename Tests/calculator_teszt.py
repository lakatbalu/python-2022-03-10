from calculator import add 

def test_add():
    result = add(5,10)
    assert result == 15

def test_add_with_negative_numbers():
    result = add(-1,-2)
    assert result == -3