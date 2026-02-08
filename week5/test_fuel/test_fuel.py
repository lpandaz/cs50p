from fuel import convert, gauge
import pytest


def test_convert_basic():
    assert convert('3/4') == 75

def test_gauge_basic():
    assert gauge(75) == '75%'

def test_gauge_full():
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'

def test_gauge_empty():
    assert gauge(1) == 'E'

def test_convert_error():
    with pytest.raises(ValueError):
        convert('red/4')

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert('5/0')

def test_convert_negative():
    with pytest.raises(ValueError):
        convert('-3/2')

