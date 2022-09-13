import pytest

TEST_DICT = {a: a ** 2 for a in range(1, 5)}


def test_value_is_int():
    for value in TEST_DICT.values():
        assert isinstance(value, int)


@pytest.mark.parametrize("test_dicts", [(dict(a=1, b=2)),
                                        dict(a=0, b=0),
                                        dict(a=-1, b=-2)])
def test_equals_values(test_dicts):
    assert test_dicts['a'] * 2 == test_dicts['b']


@pytest.mark.parametrize("key", [-1, 0, 5])
def test_exist_keys(key):
    try:
        assert TEST_DICT[key] == key ** 2
    except KeyError:
        print(f"\nKey {key} is not exist in dict")
