"""
Tipo String

Em pyhton um dado é considerado do tipo string sempre que:

-Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
-Estiver entre aspas duplas ->''uma string'', ''234'', ''a'', ''True'', ''42.3''
-Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
#-Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""
"""
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie' \n é para pular linha
print(nome)
print(type(nome))

#nome = ""Angelina
#Jolie"""
#print(nome)
#print(type(nome))
##tres aspas duplas no inicio """Angelina e na outra linha """ Jolie
# também faz pular linha

"""
print(nome.lower()) -> minusculo
print(nome.upper()) -> maiusculo
print(nome.split()) -> transforma em uma lista de strings

print(nome[0:4]) #Slice de strings

print(nome[5:15]) #Slice de strings

print(nome[14],nome[13]) -> printa a ultima e a penultima letra

#[  0,     1]
#['Geek', 'University']
print(nome.split()[0]) -> transforma string composta em string separada

print(nome.split()[1])

"""
#[ 0,  1,  2,  3]
#['G','e','e','k', '', 'U','n','i','v','e','r']

nome = 'Geek University'

print(nome[::-1]) #-> comece do primeiro elemento, vá ate o ultimo elemento e inverta

print(nome.replace('G', 'P')) #substitui aonde tem G por P

print(type(nome))

teste = 'ana'
print(teste)

print(teste[::-1]) #palíndromo


