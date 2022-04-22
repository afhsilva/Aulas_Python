"""
PEP8 - PYTHON ENHANCEMENT PROPOSAL
São propostas de melhoria para a linguagem python

The Zen of Python
import this

A ideia da PEP8 é que possamos escrever códigos python de forma
Pythônica, ou seja, visualmente agradavel.

[1] - utiliza Camel case para nomes de classes -> forma correta é iniciar com letra maiuscula,
 sem nome composto ou underline;
 [2] - utilize nomes em minusculo, separados por underline para funções (def) ou variaveis;
def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

 [3] - utilize 4 espaços para identação! (se o tab estiver confugurado para 4 espaços tb funciona)
 if 'a' in 'banana':
    print('tem')

 [4] - linhas em branco
 - Separar funções e definições de classes com duas linhas em branco;
 - Métodos dentro de uma classe devem ser separados com uma unica linha em branco;

 [5] - Imports
 -Imports devem ser sempre feitos em linhas separadas;

 #import errado
 import sys, os

 #import certo
 import sys
 import os

 #Não há problemas em utilizar:
 from types import StringType, ListType

 # Caso tenha muitos imports de um mesmo pacote recomenda-se fazer:

 from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

#Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstring e
#antes de constantes ou variaveis globais

[6] - Espaços em expressões e instruções
#Não faça
funcao( algo[ 1 ]), { outro: 2 } )

#Faça
funcao(algo[1], {outro: 2})

#Não faça
algo (1)

#Faça
algo(1)

#Não faça:
dict ['chave'] = lista [indice]

# Faça
dict['chave'] = lista[indice]

#não faça
x             =1
y             =3
variavel_longa=5

#faça
x = 1
y = 3
variavel_longa = 5

[7] Termine sempre uma instrução com uma nova linha (uma linha em branco)
"""
import this


class Calculadora:
    pass


class CalculadoraCientifica:
    pass



def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

if 'a' in 'banana':
    print('tem')
