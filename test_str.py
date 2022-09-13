import string
from random import choice

import pytest

from string import ascii_letters


RANDOM_STRING = ''.join(choice(ascii_letters) for _ in range(20))


@pytest.mark.parametrize("test_string", [RANDOM_STRING, "Строка на кириллице", "12345"])
def test_is_str(test_string):
    assert type(test_string) == str


def test_is_no_digits():
    for char in RANDOM_STRING:
        assert not char.isdigit()


def test_is_no_punctuation():
    for char in RANDOM_STRING:
        assert char not in string.punctuation
