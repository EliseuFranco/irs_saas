from exceptions.field_not_valid_exception import FieldNotValidError
import re


def not_null(value, field="campo"):
    if value is None or value == '':
        raise FieldNotValidError (f'{field} não pode ser nulo ou vazio')
    return value

def email(value):
    re.search("^[A-Za-z0-9]+([_-.])+@[a-zA-Z0-9.-]+\\.[A-Za-z]{2,}$", value)
    # ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

