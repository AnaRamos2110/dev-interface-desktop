#Exercicío nº(??- Corrigindo o código

'''
print('Nome', nome)
print('Sobrenome:' sobrenome)
print('Idade', idade)
print('Ano de nascimento:', ano_de_nascimento)
print('Altura', altura)

'''
#Vamos começar com uma simples correção sem funções de input, condições e iterações mais complexas! Conforme o prof for repassando os códigos eu vou acompanhando!

nome = "Ana"
sobrenome = "Ramos"
idade = 26
ano_de_nascimento = 1998
altura = 1.63 

#Criamos 5 variáveis com 3 tipos primitivos diferentes!Agora vamos exibir as informações:
print(f"Meu nome é: {nome} {sobrenome} eu tenho {idade} anos e meu ano de nascimento é em {ano_de_nascimento}.\nEu tenho {altura} de altura! ")


#Boas práticas- Evite criar variáveis com nomes que sejam vagos ou que não sejam tão intuitivos. Lembre-se que outros colegas irão consultar seu código e você irá consultar outros scripts. A comunicação precisa ser bem detalhada!
a1 = 2000
a2 = 23
print('A soma dos valores é o ano de:', a1 + a2)

valor_de_soma = 2000
valor_de_soma2 = 24
print(f"A soma dos valores é o ano de: {valor_de_soma + valor_de_soma2}")


#Operadores de comparação !! Observe o código abaixo:

nome = 'Avril Lavigne'
idade  = 17
maior_de_idade = idade >= 18
fim_do_programa = '--Sair do sistema--'

print('')
print('Nome completo:', nome, '-', 'Idade', idade)
print('Ela é maior de idade?', maior_de_idade)
print('') #Esta função com string vazia pula uma linha, o mesmo retorno do print('\n')
print(fim_do_programa)

'''Exercicío:
Processo de converter tipos de dados, por exemplo: Um sistema de PDV (Ponto de
Vendas) de um Supermercado recebe um valor tipo "String" em um campo que é para
receber um valor "Inteiro", a classe do Python, chamada type que é uma CLASSE, que faz
a conversão de dados.'''

mercadoria = input("Passe ou digite o código de barras do produto: ")

try:
    codigo = int(mercadoria)  # tenta converter para inteiro
    print(f"{codigo} foi adicionado à sua lista")
except ValueError:
    print("Erro: o código de barras deve conter apenas números.")
