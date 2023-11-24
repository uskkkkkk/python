import re
import doctest
def is_valid_password(password):
    """
    Функция для проверки, является ли входная строка корректным паролем

    >>> is_valid_password("пароль")
    False

    >>> is_valid_password("12345678")
    False

    >>> is_valid_password("abcdefgh")
    False

    >>> is_valid_password("ABC123&*$")
    False

    >>> is_valid_password("123@#ABC!.,?")
    False

    >>> is_valid_password("lOngPa$$W0Rd")
    False

    >>> is_valid_password("Password")
    False

    >>> is_valid_password("rtG&3FG#Tr^e")
    True

    >>> is_valid_password("a^A1@*@1Aa")
    True

    >>> is_valid_password("oF^a1D@y5%e6")
    True
    
    """
    pattern = r'^(?=[A-Za-z\d^$%@#&*]{8,})(?=(?:.*[a-z].*){2,})(?=(?:.*[1-9].*)+)(?=[^,.!?]*$).*([\^$%@#&*]).*(?!\1)([\^$%@#&*]).*(?!\1)(?!\2)([\^$%@#&*]).*$'
    return bool(re.match(pattern, password))

doctest.testmod(verbose=True)
