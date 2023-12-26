'''
Exercício 1: Escreva um programa que retorne uma lista com os valores numéricos de 1 a N, mas com as seguintes exceções:

Números divisíveis por 3 deve aparecer como “Fizz” ao invés do número;

Números divisíveis por 5 devem aparecer como “Buzz” ao invés do número;

Números divisíveis por 3 e 5 devem aparecer como “FizzBuzz” ao invés do número.

Exemplo: 3 -> [1, 2, "Fizz"].
'''

def lista_num(limite: int):
    lista = []
    for i in range(1, limite + 1):
        if i % 3 == 0 and i % 5 == 0:
            lista.append('FizzBuzz')
        elif i % 3 == 0:
            lista.append('Fizz')        
        elif i % 5 == 0:
            lista.append('Buzz')
        else:
            lista.append(i)
    return lista

lista_num(15)