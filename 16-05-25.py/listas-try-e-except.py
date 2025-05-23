'''
REVISÃO de Listas
No código a seguir, temos os seguintes índices positivos, que começam em 0 e vão até 9. Exemplo: lista[0]
retorna 'a', lista[9] retorna 'j'.
Em seguida temos os índices negativos, que começam em -1 e vão até -10 (ou seja, de -1 até -len(lista)).
Exemplo: lista[-1] retorna 'j', lista[-10] retorna 'a'.
Dessa forma, o código demonstra como acessar os mesmos elementos tanto por meio de índices positivos quanto
negativos:
'''
#Exemplo 1-  uma lista com índices POSITIVOS e NEGATIVOS
#Lista com elementos de 'a' - 'j':
'''
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#Exibindo os índices positivos e os valores correspondentes
print('Indices positivos:')
for i in range(len(lista)):
    print(f'Índice {i}: {lista[i]}')

#Exibindo os índices negativos e os valores correspondentes
print('\nÍndices negativos:')
for i in range(-1, -len(lista) -1, -1):  
    #Índices negativos começam de -1 até -len(lista)
    print(f'Indice {i}: {lista[i]}')
'''


#Exemplo 2- CAIXA ALTA 
'''
CURIOSIDADE 1o
Digamos que iremos precisar que a impressão do código saia com todos os caracteres em CAIXA ALTA, devido
uma particularidade do sistema, como resolver? Simples, temos o método do Pythton chamado Captilize que faz a
conversão de textos de caixa baixa em CAIXA ALTA, exemplo:
'''

 
#Lista de elementos de a-j
'''
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#Alterando os caracteres para CAIXA ALTA com método CAPITALIZE 
conversor_texto = [letra.capitalize() for letra in lista]

#Exibindo os índices positivos e os valores correspondentes
print('Índices positivos:')
for i in range(len(conversor_texto)):
    print(f'Índice {i}: {conversor_texto[i]}')

#Exibindo os índices negativos e os valores correspondentes
print('\nÍndices negativos:')
for i in range(-1, -len(conversor_texto)-1, -1):
    print(f'Índice {i}: {conversor_texto[i]}')
'''

#Exemplo 3- caixa baixa
'''
CURIOSIDADE 2o
Digamos que iremos precisar que a impressão do código saia com todos os caracteres em caixa baixa, devido uma
particularidade do sistema, como resolver? Simples, temos o método do Pythton chamado Lower que faz a
conversão de textos de CAIXA ALTA em caixa baixa, exemplo:
'''
#Exemplos de uma lista
lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#Transformando todos os elementos para minúsculas (mesmo que já estejam)
conversor_texto = [letra.lower() for letra in lista]

#Exibindo os índices positivos e os valores correspondentes
print('Índices positivos: ')
for i in range(len(conversor_texto)):
    print(f'Índice {i}: {conversor_texto[i]}')

#Exibindo os índices negativos e os valores correspondentes
print('\nÍndices negativos:')
for i in range(-1, -len(conversor_texto) -1, -1):
    print(f'Índice {i}: {conversor_texto[i]}')


#Exemplo 4
'''
Métodos aplicados a Listas
Como já aprendemos na primeira parte da aula do tema de “Listas” no Python, temos a possibilidade
de incluir alguns “Métodos”, em uma determinada lista, vamos criar mais algumas situações,
envolvendo novos métodos de “Listas”, são eles:
● Try e Except
● Len
● Max e Min
'''

    #Também veremos try e Except para tratativa de erros !
'''
Estes dois métodos trabalham “juntos” com a finalidade de tratar erros que acontecem em
determinado código, e muito utilizado com o método de “Listas” na linguagem Python.
Vamos analisar o código a seguir, que pode ser aplicado nos Exercícios, e repare que o
mesmo ainda não tem os métodos Try e Except, que poderiam ajudar no tratamento do erro retornado
'''

try: #Usando o try para coisas que podem dar algum erro na interação com o usuário de acordo com os dados que ele inserir
    with open('arquivo.txt') as file_object:    
        #O Python abre o arquivo e garante que ele será fechado corretamente, mesmo que ocorra um erro durante a leitura ou escrita. Pede-se que determinado arquivo seja aberto e previamento renomeado para 'file_object'
        texto = file_object.read() #Pedindo para abrir o texto 
        print(texto)
except FileNotFoundError as erro: #Se a tentativa cair no erro, ele se torna uma exceção, nós denominamos o nome da exceção como 'Erro, arquivo não encontrado' para que quando o erro aparecer, o usuário possa compreender também.
    print(f'O arquivo .TXT não foi encontrado no diretório de projetos.\n{erro}')

#Para ficar mais claro, vamos verificar outro exemplo, agora efetuando a divisão por inteiro
#(//), lembra? Vejamos:


#Exemplo 5: programa para fazer uma divisão, porém ao efetuar o cálculo, um erro é gerado e o tratamento do erro é efetuado pelos métodos: Try e Except

def divisao(x, y): #Criando uma função de divisão 
    try:
        #O valor do cálculo é a divisão INTEIRA DE 3 por 0
        resultado = x // y
    except ZeroDivisionError: #Valor PADRÃO  para tratamento de erros de divisão.
        print('Desculpe. Mas o valor não pode ser dividido por zero! :(' )
        
'''
Os valores da divisão podem estar em qualquer parte da função (def), 
assunto que vamos ver nas próximas aulas.
'''
divisao(3, 0) #Chamando a função 

#Exemplo 6- len
'''
LEN
Vamos entender melhor com um exemplo prático no código a seguir, que na prática é um
DESAFIO, vamos entender por que este código é um problema de Programação que foi
resolvido com um dois índices.
'''
#Verificando a quantidade de itens de uma lista com o método - len

qtd_titulos = ['4', '3', '2', '1']
titulos = qtd_titulos #A variável títulos recebe os valores da lista qtd_titulos

#Uma boa prática é utilizar o método len dentro do print, conforme a seguir e configura o resultado
print('\n' + 'A quantidade de titulos mundiais do Palmeiras são: {}'.format(len(titulos[0:0])), '-> Títulos mundiais.' + '\n') #Santorsula zoa o próprio time kkkkk
#Curiosidade- o [0:0] dentro dos colchetes serve para percorrer a lista assim como poderia ser [1:4], porém, como ele começa em 0 e para em 0, resulta em lista vazia entregando o resultado de 0 no final kkkk
#Apesar da brincadeira, é um problema muito complicado de resolver, onde os índices não são contados no print.

#Exemplo 7- len
'''
Vamos entender melhor ainda o código anterior, se o método Len faz a contagem de
qualquer informação dentro de uma String, então ele começa do índice zero e percorre
toda a lista, exemplo:
'''
personagens = 'Bananas de pijama '
indice = ['b', 'a', 'n', 'a', 'n', 'a']
#          0    1    2    3    4    5
#       Sequência de índices da lista
print(f'{personagens} descendo as escadas!')
print('\n' + 'A quantidade de caracteres da palavra "banana" são {}'.format(len(indice)), '-> caracteres' + '\n')

'''
Conclusão- Sendo assim travamos a contagem do método Len com seus índices [0:0], na prática é
uma função muito útil se quer retornar uma valor ZERO em uma lista de 5 mil itens por
exemplo e que fosse preciso retornar zero para alguma finalidade, conforme o exemplo da
brincadeira com o time Palmeiras, que sabemos que o retorno é ZERO.
'''


#Exemplo 8- MAX & MIN
'''
Para que serve? 
Este método é muito simples de utilizar, assim como os demais que já aprendemos, a
finalidade deste método é fazer a contagem dentro de uma lista com “String”, sendo a
quantidade MÁXIMA de caracteres e a quantidade MÍNIMA de carecteres, vamos ver
alguns exemplos, para entender melhor na prática.
'''


mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8'] #Listas de modelos de celulares e suas quantidades
qtd = [100, 200, 300]

vendas = list(zip(mobile, qtd)) #Associa as listas de modelos e quantidades, criando uma lista de tuplas. ps: Não podemos juntar uma lista de strings com integers a não ser que você crie uma tupla para unifica-lás.
venda_minima = 150 #Estabeleci uma meta também 

#E também um laço de iteração para percorrer a lista.
print("Modelos com estoque em relação à venda mínima:")

for modelo, quantidade in vendas: #Percorre a quantidade de vendas.
    if quantidade < venda_minima:
        print(f'Modelo: {modelo}, Quantidade: {quantidade} - Abaixo da venda miníma :( .')
    elif quantidade == venda_minima:
        print(f'Modelo: {modelo}, Quantidade: {quantidade} - Corresponde a quantidade miníma de vendas.')
    else:
        print(f'Modelo: {modelo}, Quantidade: {quantidade} - Ultrapassou a meta mensal, parabéns!.')

# Encontrando o modelo com a maior e a menor quantidade
modelo_max = max(vendas, key=lambda x: x[1])  # Maior quantidade
modelo_min = min(vendas, key=lambda x: x[1])  # Menor quantidade

print(f'\nModelo com maior quantidade em estoque: {modelo_max[0]} - {modelo_max[1]} unidades')
print(f'Modelo com menor quantidade em estoque: {modelo_min[0]} - {modelo_min[1]} unidades')

#Exemplo 9 - MAX & MIN
'''
Max e Min
Uma forma muito utilizada é o TRATAMENTO de valores MÁXIMO e MÍNIMO com o uso
de condições, onde a tomada de decisões é mais ÚTIL em alguns estudos de caso em
algum determinado programa, utilizando o método muito utilizado de LISTAS, vejamos um
exemplo na PRÁTICA, muito útil e muito utilizado no DIA A DIA.
'''
