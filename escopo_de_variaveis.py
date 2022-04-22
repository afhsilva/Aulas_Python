"""
Escopo de variáveis
limitação de algo /                    / não vem antes e não acontece depois
está dentro do espaço limitado

Dois casos de escopo:
1-Variaveis globais;
    - variavesi globais são reconhecidas, ou seja, seu espcopo compreende todo o programa.

2-variáveis locais;
    - variáveis locais são reconhecidas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar varáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica, isso significa que ao declararmos
uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;
(int - tipo da variavel) (numero - nome da variavel) (42 - valor da variavel)

Exemplo em java:
int numero = 42;



"""
numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 42
#novo = 0

if numero > 10:
    novo = numero+10 # a variavel 'novo' está declarada localmente dentro do bloco do if. Portanto é local
    print(novo)

print(novo)