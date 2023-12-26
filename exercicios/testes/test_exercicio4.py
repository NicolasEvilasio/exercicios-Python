'''
Exercício 4 
Baseado no exercício anterior, escreva uma função que, dado uma lista de emails, deve retornar somente os emails válidos. 
Caso uma exceção ocorra, apenas a escreva na tela.

Exemplo: 
["nome@dominio.com", "errad#@dominio.com", "outro@dominio.com"] -> ["nome@dominio.com", "outro@dominio.com"].
'''

from exercicio4 import generate_valid_email_list
import pytest


def test_if_doesnt_have_emails_returns_empty_list():
    assert generate_valid_email_list([]) == []


def test_only_valid_emails():
    emails = ["username@website.com"]
    expected_emails = ["username@website.com"]
    assert generate_valid_email_list(emails) == expected_emails


def test_invalid_emails_should_be_filtered():
    emails = ["inv*alid@website.com"]
    expected_emails = []
    assert generate_valid_email_list(emails) == expected_emails


def test_valid_and_invalid_emails_returns_only_valids():
    emails = ["username@website.com", "inv*alid@website.com"]
    expected_emails = ["username@website.com"]
    assert generate_valid_email_list(emails) == expected_emails