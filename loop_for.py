"""
Loop for

Loop -> estrutura de repetição.
For -> uma dessas estruturas

C ou Java:

for (int i = 0; i < limitador; i faça a execução)
for (int i = 0; i < 10; i++)
{
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3 , 5 , 7 , 9]
- Range
    numeros = range(1, 10)

    range(valor_inicial, valor_final)

Obs: o valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não


#Exemplo de for 1 [Iterando em uma string]
for letra in nome:
    print(letra)

#Exemplo de for 2 [Iterando sobre uma lista]
for numero in lista:
    print(numero)

#Exemplo de for 3 [Iterando sobre um range]

for numero in range(1, 10):
    print(numero)

"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em uma lista


"""
Enumerate -> prea cada sequencia do interavel ele agrega um indice
 (0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')
 
 for i, v in enumerate(nome): #Para i -> de indice, v-> de valor
    print(nome[i])
    
    for indice, letra in enumerate(nome):
    print(letra)
    
    for _, letra in enumerate(nome):
     print(letra)
    
    Obs: quando não precisamos de um valor podemos descartá-lo com um underline(_)
   
   for valor in enumerate(nome):
    print(valor)  #esse comando imprime o valor do indice e a posição da letra da varialvel
    
    for valor in enumerate(nome):
    print(valor[0])  #traz somente os indices
    
    for valor in enumerate(nome):
    print(valor[1])  # traz somente as letras
    
    qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd+1):
    print(f'imprimindo{n}')
    
    
    qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
    print(f'A soma é {soma}')
    
    
    nome = 'Geek University'
for letra in nome:
    print(letra, end='') #esse comando imprime a frase sem pular linha
    
    Tabela de emojis unicode
    https://apps.timwhitlock.info/emoji/tables/unicode
    
    
    
#Original: U+1F60D  -> substituir o + para tres zeros
#Modificado: U0001F60D

for _ in range (3):
    for num in range (1,15):
        print('\U0001F60D' * num)
    
"""

