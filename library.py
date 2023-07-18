import random
import string


def generate_random_number() -> int:
    result = random.randint(0, 1_000)
    return result


def check_password_valid(password: str) -> bool:
    contains_lowercase_letter = contains_uppercase_letter = contains_special_character = contains_number = False
    for character in password:
        if not character.isascii() or character.isspace():
            return False
        if character.islower():
            contains_lowercase_letter = True
        elif character.isupper():
            contains_uppercase_letter = True
        elif character in string.punctuation:
            contains_special_character = True
        elif character.isdecimal():
            contains_number = True
    return contains_lowercase_letter and contains_uppercase_letter and contains_special_character and contains_number
