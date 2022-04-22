"""
Loop While

Forma geral

while expressao_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5
// num recebe 5, num é menor que cinco? False


numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# Obs: em um loop while, é importante que cuidemos do critério de parada para não causar
 um loop infinito

while numero < 10:
   print(numero)
numero = numero + 1  -- essa linha faz a condição de parada do while para não entrar em loop infinito.

# C ou Java
while(expressao){
//execucao
}

#do while (C ou Java)

do{
    //execucao
}while (expressao)
"""

#Exemplo 2
resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
