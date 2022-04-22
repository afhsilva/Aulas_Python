""""
Tipo Float

Tipo real, decimal

Casas decimais

obs.: os separadores das casas decimais na programação é o ponto e não a virgula.
#Errado
valor = 1,44

#Certo
valor = 1.44

"""
#Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)

#Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

#É POSSIVEL fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Podemos converter um float para um int
"""
Obs.: ao converter valores float para inteiros, nós perdemos precisão - ele trunca
"""
res = int(valor)
print(res)
print(type(res))

#Podemos trabalhar com numeros complexos - é representado pelo j
variavel = 5j