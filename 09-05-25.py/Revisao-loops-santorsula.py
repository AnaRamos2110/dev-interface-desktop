'''Seguindo com os exercicíos, analise o código a seguir, referente a um sistema de verificação de metas de vendas, criando com outra lógica, utilizando o FOR e Listas na linguagem Python, vejamos:'''

#Exemplo1
'''meta = 10000
valor_vendas = [
    ['João Paulo', 15000],
    ['Pedro Silva', 14000],
    ['Júlio Matos', 16000],
    ['Ronaldo Silveira', 9000],
]
print('O valor da meta do mês de julho é de R$', meta,'\n')
for item in valor_vendas:
    if item[1] > meta:
        print('Vendedor {} BATEU a meta, com o valor de vendas de R$ {}' .format(item[0],item[1]))
    else:
        print('\n' + 'Vendedor {} "NÃO" bateu a meta, com o valor de vendas de R$ {}' .format(item[0],item[1]))'''

#Exemplo2
'''O código do próximo exercício, é referente a um sistema de verificação de metas de
vendas, porém criado de outra forma, com auxilio do método “enumerate”,(OBS- O enumerate é uma função muito útil no Python que permite iterar sobre uma lista (ou qualquer outro iterável) e obter tanto o índice quanto o valor de cada item. Isso pode ser especialmente útil quando você precisa de ambos os elementos durante a iteração.) no mesmo foi
é utilizado outra lógica, utilizando o FOR e Listas na linguagem Python, vejamos:'''

'''
produtos = ['PC Desktop', 'Notebook', 'Monitor', 'Placa de vídeo', 'SSD 500GB', 'HD SATA 1TB']
vendas_2019 = [1000, 2000, 3000, 4000, 6000, 3000]
vendas_2020 = [1300, 2150, 3500, 4600, 6700, 3900]

for i, lista_produtos in enumerate(produtos):
    if vendas_2020[i] > vendas_2019[i]: #Verifica o crescimento em 2020
        crescimento = (vendas_2020[i] / vendas_2019[i]) -1
        #F-string > Format
        print(' {} Vendeu {} unidades em 2019, e em 2020 vendeu {} unidades. Crescimento: {:.0%}' .format(lista_produtos, vendas_2019[i], vendas_2020[i], crescimento))
'''
#Neste código temos 3 listas que são percorridas pelo FOR com auxilio do método "enumerate". Repare que temos um if fazendo a verificação de condição de duas listas inteiras, por um cálculo de divisão e impressão do resultado do código, com as vendas do ano de 2019 e 2020 de cada item da lista.

#Exemplo 3
#Variável i armazena dados do método enumarate

'''funcionarios = ['Maria Silva', 'José Inácio', 'Fernando Rodrigues', 'Luiz Santos']
for i, lista_funcionarios in enumerate (funcionarios):
    print(' {} -> é o índice do funcionário: {}' .format(i, lista_funcionarios))'''

#A variável i armazena dados no FOR, o método enumerate, é utilizado para numerar as ID'S dos usuários.


#Exemplo 4
'''
Vamos analisar o próximo código,que é uma rotina muito utilizada no dia a dia do desenvolvedor, que é um FOR dentro de outro FOR com listas distintas, analise o código a seguir e confira seu resultado:
'''


'''
estoque = [
[1000,2000,3000,4000,5000,6000],
[1100,2100,3100,4100,5100,6100],
[1200,2200,3200,4200,5200,6200],
[1300,2300,3300,4300,5300,6300],
]



fabricas = ['LexCorp', 'Wayne enterprise', 'Star solutions', 'Siberian Foundation', 'IDRA Arms']
estoque_minimo = 7000
for i in enumerate(estoque):
    #O for anterior percorre a primeira lista para verificar os valores da mesma.
    for qtd in lista:
        if qtd < estoque_minimo:
            print('As empresas com estoque abaixo de:', estoque_minimo, 'unidades, são as fáricas:',fabricas[i])
        else:
            print('As empresas com estoque acima de:', estoque_minimo, 'unidades, são as fábricas:', fabricas[i])
'''


'''
Neste próximo exemplo do FOR, podemos PARAR o loop em determinada operação do
código, analise o código a seguir e entenda a LÓGICA do programa, que é verificar o
maior valor de uma lista, ao encontrar o LOOP para de fazer as repetições, em busca do
valor que consta na variável “meta”, vejamos:
'''

#Exemplo 5- FOR com a função break que para o loop

'''
vendas = [100, 150, 1500, 2300, 120]
loja = ['Barão', 'Iguatemi', 'Centro', 'Cambuí', 'Sta. Genebra']
meta = 2100
for lista_vendas in vendas:
    if lista_vendas < meta: #Verifica se a lista_vendas é maior que a variável meta
        print(f"A loja do bairro {loja[3]}, bateu meta! ")
        break
'''

#Exemplo 6
'''
Analise o código a seguir, agora utilizando o While, repare que o código é um “Sistema de
Cadastro de Produtos” em uma lista vazia, cada item a ser inserido, será adicionado em
uma lista automaticamente.

O programa somente vai parar, quando pressionar ENTER duas vezes, vejamos o
programa no próximo slide e seu resultado.
'''
'''
lista_produtos = input('Insira o produto para cadastro e pressione ENTER para encerrar o sistema.' '\n' + ': ')
insere_lista = []

#Exemplo da estrutura while
while lista_produtos != '':
    insere_lista.append(lista_produtos)
    lista_produtos = input('Insira um NOVO produto para cadastro: ')
print(f"Cadastro efetuado com sucesso! Os produtos cadastrados foram: {', '.join(insere_lista)}")
'''

#Exemplo 7
'''
Vamos analisar mais um exemplo com o While e repare que o produto é adicionado com
sua quantidade, seguindo a mesma lógica do código anterior, porém temos um problema
nestes dois códigos, é o famoso erro de programa que ocorre durante algum lago de
repetição (While ou Loop), vejamos:
'''

'''
produtos = [ 
    ['Maçã', 5],
    ['Banana', 15],
    ['Goiaba', 25],
    ['Manga', 35]
]
produtos = [] #Lista vazia para receber iterações 

while True: #Loop para inserir vários produtos gerando laço de repetição: 
    produto = input('Insira o produto: ')
    if not produto:
        break
    qtd = int(input('Qual é a quantidade de produtos: '))
    produtos.append([produto, qtd])
    print('Os produtos e quantidade cadastrados foram: ' ,produtos)
'''

#Exemplo 8 
'''
Analise o código a seguir com o While, onde o mesmo percorre uma lista, encontra o
índice que é passada para o IF chegar o índice correto, para poder fazer a impressão do
dia da semana desejado e “para” o código, vejamos:
'''

'''
semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
i = 0
while semana:
    if i== 3:
        print('\n' + '--Um dia antes do famoso SEXTOU é:' , semana[i])
        break
    i += 1 #Contador de 0 até 3
'''

