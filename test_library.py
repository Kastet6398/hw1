import pytest

import library

password_data = [
    ('Hello_world123', True),
    ('Hello, world!', False),
    ('Hello, world123', False),
    ('Hello,_world', False),
    ('hello,_world123', False),
    ('HELLO,_WORLD123', False),
    ('Привіт,_світе123', False),
]


@pytest.mark.parametrize('password, result', password_data)
def test_check_password_valid(password: str, result: bool):
    assert library.check_password_valid(password) == result
