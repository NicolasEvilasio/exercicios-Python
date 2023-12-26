from exercicio1 import lista_num
import pytest


# Must returns 'Fizz' when a number is divisible by 3 
def test_lista_num_when_num_is_divisible_by_3():
    assert 'Fizz' in lista_num(9)

# Must returns 'Fizz' when a number is divisible by 5 
def test_lista_num_when_num_is_divisible_by_5():
    assert 'Buzz' in lista_num(9)

# Must returns 'FizzBuzz' when a number is divisible by 3 and 5 
def test_lista_num_when_num_is_divisible_by_3_and_5():
    assert 'Buzz' in lista_num(15)

# Must not returns 'Fizz' or 'Buzz' when the numbers are not divisible by 3 and 5 
def test_lista_num_when_num_are_not_divisible_by_3_and_5():
    assert not ['Fizz', 'Buzz', 'FizzBuzz'] in lista_num(2)

def test_lista_num_when_input_is_a_string():
    with pytest.raises(TypeError):
        lista_num('teste')
        