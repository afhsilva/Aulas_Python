"""
Recebendo dados do usuário

input() -> entrada, todo dado recebido via input é do tipo string

Em PythonTudo que estiver entre:
- Aspas simples;
- Aspas dulas;
- Aspas simples triplas;
- Aspas duplas triplas.

"""
#Entrada de dados
#print("Qual seu nome?")

nome = input('Qual seu nome?')

#Exemplo de print 'antigo' 2.x
#print('Seja bem-vindo(a) %s' %nome)

#Exemplo de print 'moderno' 3.x
#print('Seja bem vindo(a)', format(nome))

#Exemplo de print 'mais atual'3.7
print(f'Seja bem vindo(a) {nome}')

#print('Qual sua idade?')
#idade = input()

idade = int(input('Qual sua idade?'))

#Processamento

#Saída de dados

#Exemplo de print 'antigo' 2.x
#print ('A %s tem %s anos' %(nome,idade))

#Exemplo de print 'moderno' 3.x
#print('A{0} tem {1} anos', format(nome,idade))

#Exemplo de print 'mais atual'3.7
print(f'A {nome} tem {idade} anos')

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para ouotro

"""
#print(f'A {nome} nasceu em {2021 - int(idade)}')

print(f'A {nome} nasceu em {2021 - (idade)}')