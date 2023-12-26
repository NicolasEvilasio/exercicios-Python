'''
Exercício 3 Faça uma função que valide um e-mail, lançando uma exceção quando o valor for inválido. Endereços de e-mail válidos devem seguir as seguintes regras:

Devem seguir o formato nomeusuario@nomewebsite.extensao;
O nome de usuário deve conter somente letras, dígitos, traços e underscores (_);
O nome de usuário deve iniciar com uma letra;
O nome do website deve conter somente letras e dígitos;
O tamanho máximo da extensão é de 3 caracteres.

🦜 As funções isalpha, isdigit e isnumeric podem ser utilizadas para verificar se uma letra ou palavra são compostas de somente caracteres ou dígitos. 

Exemplo: "1".isalpha() -> False , "a".isalpha() -> True, "123".isnumeric() -> True.
'''
from exercicio3 import validate_email
import pytest


def test_validate_email_invalid_email_format():
    with pytest.raises(ValueError):
        validate_email('username@email')

def test_validate_email_only_letters():
    assert validate_email('email@email.com')

def test_validate_email_letters_and_digits():
    assert validate_email('email1990@email.com')

def test_validate_email_letters_and_underscores():
    assert validate_email('my_email@email.com')

def test_validate_email_letters_and_dashes():
    assert validate_email('my-email@email.com')

def test_validate_email_letters_digits_and_dashes():
    assert validate_email('email-1990@email.com')

def test_validate_email_letters_digits_dashes_and_underscores():
    assert validate_email('e-mail_1990@email.com')

def test_validate_email_username_not_contains_special_char():
    with pytest.raises(ValueError):
        validate_email('user*name@email.com')

def test_validate_email_username_starts_with_letter():
    with pytest.raises(ValueError):
        validate_email('2username@email.com')

def test_validate_email_website_contains_only_letters_or_digits():
    with pytest.raises(ValueError):
        validate_email('username@my_email.com')

def test_validate_email_extension_is_bigger_than_maximux_size():
    with pytest.raises(ValueError):
        validate_email('email@email.comm')

def test_validate_email_extension_with_2_char_should_pass():
    assert validate_email('email@email.co')