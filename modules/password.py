from os import urandom
from random import choice

char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
             'nums': '0123456789',
             'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'special': '^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
            }


def generate_pass(length=21):
    """Function to generate a password"""

    password = []

    while len(password) < length:
        key = choice([char_set["small"],char_set["big"],char_set["special"],char_set["nums"]])
        a_char = urandom(1)
        n = choice(key)
        if n in key:
            if check_prev_char(password, n):
                continue
            else:
                password.append(n)
    return ''.join(password)


def check_prev_char(password, current_char_set):
    """Function to ensure that there are no consecutive 
    UPPERCASE/lowercase/numbers/special-characters."""

    index = len(password)
    if index == 0:
        return False
    else:
        prev_char = password[index - 1]
        if prev_char in current_char_set:
            return True
        else:
            return False

if __name__ == '__main__':
    print (generate_pass())