import pytest

import library

numbers = [library.generate_random_number() for number in range(1_000)]
password_data = [
    ('Hello_world123', True),
    ('Hello, world!', False),
    ('Hello, world123', False),
    ('Hello,_world', False),
    ('hello,_world123', False),
    ('HELLO,_WORLD123', False),
    ('Привіт,_світе123', False),
]


@pytest.mark.parametrize('number', numbers)
def test_generate_random_number(number: int):
    assert 0 <= number <= 1_000


@pytest.mark.parametrize('password, result', password_data)
def test_check_password_valid(password: str, result: bool):
    assert library.check_password_valid(password) == result
