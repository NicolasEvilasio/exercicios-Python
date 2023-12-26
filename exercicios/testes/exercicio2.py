'''
Exercício 2: Em alguns lugares é comum lembrar um número do telefone associando seus dígitos a letras. 
Dessa maneira, a expressão MY LOVE significa 69 5683. 
Claro que existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra ou uma frase, e os dígitos 1 e 0 não estão associados a nenhuma letra.

Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado na tabela abaixo. 
Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.

Letras  ->  Número
ABC     ->  2
DEF     ->  3
GHI     ->  4
JKL     ->  5
MNO     ->  6
PQRS    ->  7
TUV     ->  8
WXYZ    ->  9

Exemplo de entrada:
1-HOME-SWEET-HOME
MY-MISERABLE-JOB}

Saídas correspondentes:
1-4663-79338-4663
69-647372253-562

Verifique casos como entrada maior que 30 caracteres, vazia e com caracteres inválidos.

'''
import re

def string_to_phone_number(string: str):
    if len(string) == 0 or len(string) > 30:
        raise(ValueError)
    elif not bool(re.compile(r'^[A-Z0-9-]*$').match(string)):
        raise(ValueError)

    dict_letters = {
        'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9
    }

    numero_final = ''.join(str(dict_letters.get(letra, letra)) for letra in string)

    return numero_final