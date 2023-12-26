from exercicio2 import string_to_phone_number
import pytest
from unittest.mock import mock_open, patch

# Verifique casos como entrada maior que 30 caracteres, vazia e com caracteres inválidos.

def test_abc_should_be_converted_in_2():
    assert string_to_phone_number("ABC") == "222"


def test_def_should_be_converted_in_3():
    assert string_to_phone_number("DEF") == "333"


def test_ghi_should_be_converted_in_4():
    assert string_to_phone_number("GHI") == "444"


def test_jkl_should_be_converted_in_5():
    assert string_to_phone_number("JKL") == "555"


def test_mno_should_be_converted_in_6():
    assert string_to_phone_number("MNO") == "666"


def test_pqrs_should_be_converted_in_7():
    assert string_to_phone_number("PQRS") == "7777"


def test_tuv_should_be_converted_in_8():
    assert string_to_phone_number("TUV") == "888"


def test_wxyz_should_be_converted_in_9():
    assert string_to_phone_number("WXYZ") == "9999"


def test_dash_zero_one_should_be_kept():
    assert string_to_phone_number("0-1") == "0-1"


def test_expression_should_be_at_least_one_char():
    with pytest.raises(ValueError):
        string_to_phone_number("")


def test_expression_maximum_are_thirty_chars():
    long_expression = (
        "1111111111"  # 10 chars
        "1111111111"
        "1111111111"
        "1"
    )
    with pytest.raises(ValueError):
        string_to_phone_number(long_expression)


def test_expression_with_invalid_chars():
    with pytest.raises(ValueError):
        string_to_phone_number("I-****-MY_JOB")