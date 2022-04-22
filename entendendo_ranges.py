"""
Ranges

-Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trablahar melhor com loops for

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatório
mas sim de maneira especificada.

Formas gerais:

#Forma1

range(valor_de_parada)

#Exemplo forma 1

for num in range(11):
    print(num)

Obs: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

#Forma 2

range(valor_de_inicio, valor_de_parada)

#Exemplo Forma 2
for num in range(4,11):
    print(num)

Obs: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo de 1 em 1)

#Forma 3

range (valor_de_inicio, valor_de_parada, passo)

#Exemplo Forma 3
for num in range(1, 10, 2) :
    print(num)  #começa em 1 vai até o dez e pula de dois em dois

Obs: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

#Forma 4 (Inversa)

range (valor_de_inicio, valor_de_parada, passo)

Obs: valor_de_parada não inclusive valor_inicio especificado pelo usuário, e passo especificado pelo usuário)

#Exemplo Forma 4
for num in range(10, -1, -1) :
    print(num)  #valor decrescente

"""
#Forma 4
for num in range(10, 0, -1) :
    print(num)