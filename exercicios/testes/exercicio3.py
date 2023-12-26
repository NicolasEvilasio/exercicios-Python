'''
🦜 As funções isalpha, isdigit e isnumeric podem ser utilizadas para verificar se uma letra ou palavra são compostas de somente caracteres ou dígitos. 

Exemplo: "1".isalpha() -> False , "a".isalpha() -> True, "123".isnumeric() -> True.
'''
import re


def validate_email(email: str):
    try:
        username = email[:email.index('@')]
        website = email[email.index('@') + 1: email.index('.')]
        extension = email[email.index(r'.') + 1:]
    except ValueError:
        raise ValueError("Invalid e-mail format")

    if not bool(re.compile(r'^[a-z0-9-_]*$').match(username)):
        raise ValueError('Invalid username format')
    elif username[0].isdigit():
        raise ValueError("Username must start with a letter")
    elif not bool(re.compile(r'^[a-z0-9]*$').match(website)):
        raise ValueError('Invalid website format')
    elif len(extension) > 3 or bool(re.compile(r'\.').match(extension)):
        raise ValueError('The extension must be 1 to 3 characters')
    
    return True

