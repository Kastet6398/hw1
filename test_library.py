import pytest

import library

numbers = [library.generate_random_number() for number in range(1_000)]


@pytest.mark.parametrize('number', numbers)
def test_generate_random_number(number: int):
    assert 0 <= number <= 1_000
