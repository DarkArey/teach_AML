import pytest
from src.dec2bin import dec2bin


def test_pos():
    assert dec2bin(33, 8) == '00100001'


def test_neg():
    assert dec2bin(-33, 8) == '11011111'


def test_zero():
    assert dec2bin(0, 10) == '0000000000'


def test_neg_zero():
    assert dec2bin(0, 10) == '0000000000'


def test_bin_dig_true():
    assert dec2bin(31, 6) == '011111'


def test_bin_dig_false():
    with pytest.raises(ValueError, match='The specified bin_dig is less than the required number to represent the x'):
        dec2bin(31, 5)


if __name__ == '__main__':
    pytest.main()
