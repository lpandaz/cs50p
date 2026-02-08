from plates import is_valid


def test_is_valid_less():
    assert is_valid('A1') == False

def test_is_valid_greater():
    assert is_valid('CS12345678') == False

def test_normal_valid():
    assert is_valid('CS50') == True

def test_normal_valid2():
    assert is_valid('cs50') == True

def test_numbers_middle():
    assert is_valid('CS50AB') == False

def test_zero():
    assert is_valid('CS0') == False

def test_nonalpha():
    assert is_valid('CS50!!') == False
