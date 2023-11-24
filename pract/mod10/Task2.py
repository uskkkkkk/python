import re
import doctest
def validate_date(date):
    """
    >>> validate_date("25.08-1002")
    False

    >>> validate_date("декабря 19, 1838")
    False

    >>> validate_date("8.20.1973")
    False

    >>> validate_date("Jun 7, -1563")
    False

    >>> validate_date("31 февраля 2023")
    False

    >>> validate_date("31 июня 2015")
    False

    >>> validate_date("20 января 1806")
    True

    >>> validate_date("1924, July 25")
    True

    >>> validate_date("29/09/1635")
    True

    >>> validate_date("3.1.1506")
    True
        
    """
    pattern = r"^(?:(?:0?\d|[12]\d|3[01])([\.\/-])(?:(?<!3[01][\.\/-])0?2|(?<!31[\.\/-])0?[469]|0?[^2469]|12)\1\d{4}|\d{4}([\.\/-])(?:0?2(?![\.\/-]3[01])|0?[469](?!31[\.\/-])|0?[^2469]|12)\2(?:0?\d|[12]\d|3[01])|(?:[0-2]\d|3[01]) (?:января|(?<!3[01] )февраля|марта|(?<!31 )(?:апреля|июня|сентября|ноября)|мая|июля|августа|октября|декабря) \d{4}|(?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]), \d{4}|\d{4}, (?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]))$"
    return bool(re.match(pattern, date))

doctest.testmod(verbose=True)


