""""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, verdadeiro ou falso

True-> Verdadeiro
Flase-> falso

Obs.: Sempre com a inicial maiuscula

#errado -> true, false

#certo -> True, False
"""

ativo = False
print(ativo)


"""
Operações básicas
"""

#Negação (not)
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso.
Se for falso o resultado será verdadeiro. Ou seja, sempre o contrario.
"""
print(not ativo)

# Ou (or):
"""
É uma operação binaria, ou sejan, depende de dois valores. Ou um ou outro deve ser verdadeiro

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
logado = False
print(ativo or logado)

# E (and)
"""
Também é uma operação binaria, ou seja, depende de dois valores. Ambos os 
valores devem ser verdadeiros

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""