
def test_validate_false():
    assert validate('hello') == False

def test_validate_false_numbers():
    assert validate('255.255') == False

def test_validate_truthy_numbers():
    assert validate('255.100.100.100') == True

def test_validate_falsey_first():
    assert validate('512.512.512.512') == False

def test_validate_falsey():
    assert validate('-1') == False

def test_validate_first_byte():
    assert validate('50.') == False

def test_validate_other_bytes():
    assert validate('50.260.250.300') == False
