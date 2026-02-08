from twttr import shorten


def test_basic():
    assert shorten('Hello') == 'Hll'

def test_full():
    assert shorten('Hello, world! 120') == 'Hll, wrld! 120'