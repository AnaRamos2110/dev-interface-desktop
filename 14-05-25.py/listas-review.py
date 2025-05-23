'''
 Introdução a Listas no Python
Uma "Lista" bom exemplo de uma lista é o poder de ter inúmeros valores em uma ÚNICA
variável, entendendo essa técnica, seu código vai ficar mais rápido, organizado e a
aplicação vai ficar mais robusta, vejamos um exemplo do módulo de "Lista", mas antes
vejamos como seria um pequeno programa com o módulo print para imprimir os seguintes
valores dentro de várias variáveis:

Nome:
Idade:
Altura:
Cidade:
Estado:
País:
'''
#Criação de muitas variáveis que pode ser feita com apenas uma lista para exibir as mesmas informações
'''
nome = 'Ana'
idade = 26
altura = 1.63
cidade = "Cps"
uf = 'SP'
pais = 'Brasil'
print( nome, '\n', idade, '\n', 'altura', '\n', cidade, '\n', uf, '\n', pais )
'''
#Exemplo 1: Criando uma lista para simplificar as variáveis
'''
lista = ['Nome: Ana', 'Idade, 26', 'Altura: 1,63', 'Cidade: Campinas', 'UF: SP', 'País: Brasil']
print( lista [0])
print( lista [1])
print( lista [2])
print( lista [3])
print( lista [4])
print( lista [5])
'''

#Beleza, aqui é sem FOR mas eu queria deixar formatadinho, e enfileirado porque sinceramente eu detesto ver como isso fica no backend... 
#Facilidade maior em trazer dados, variáveis são de grande ajuda, porém, há um certo ponto do código em que ele precisa de melhores automações.



#Exemplo 2 -- Imprimindo um índice só
#No próximo exemplo, a gente pede um índice só da lista na função print()

'''print(lista[3])'''

#OBS, vou deixa o código como comentado mas a função de print chama  o índice da lista de cima
#-- Aparece no console: Cidade: Campinas--

#Exemplo 3 -- Imprimindo vários índices de uma vez
'''print(lista [0:4])''' #Para imprimir uma sequência de índices! (obs: Essa eu não lembraca :'D  )

#Exemplo 4-- Imaginamos um programa que necessite fazer a verificação automática de índices, 
#imaginamos a situação de 5 mil itens em uma lista, seria uma tarefa complicada para a busca manual com o método "index", variavel.index('o que procuro'), auxilia na busca do índice.

#Verificação automática de índices utilizando o método index
'''
msg0 = 'O índice do item é:'
msg1 = 'E o índice da lista é:'
msg2 = 'A quantidade do produto é: '
#Variáveis para deixar o código formatado

produtos = ['Celular', 'Computador', 'Monitor', 'Placa de vídeo', 'Processador']
estoque = [100, 200, 300, 400, 1000]

indice = produtos.index('Processador') #PS: para utilizar o index, tem que saber o nome do produto que você está buscando
print('\n' + msg0, indice, msg1, produtos[indice], msg2, estoque[indice]) #Concatenando 
'''

#Exemplo 5 
'''
produto = input('\n' + 'Insira o nome de um equipamento eletrônico: ') #Pede pro usuário inserir o nome de algum produto que já tem no estoque, mas não registra um produto novo
produtos = ['Celular', 'Computador', 'Monitor', 'Placa de vídeo','Processador'] #produtos que já estão na lista 
estoque = [100, 200, 300, 400, 1000] #quantidade dos produtos de estoque

#Verificação automática de produtos na lista
if produto in produtos:
    indice = produtos.index(produto)
    qtd_estoque = estoque[indice]
    print('\n' + 'A quantidade do produto: {} em estoque é {} unidades.' .format(produto, qtd_estoque))

else:
    print('\n' + '--ATENÇÃO--  O produto {} NÃO existe no estoque :c ' .format(produto))
'''


'''
Os índices de uma lista também podem receber métodos no Python, vamos conhecer os
“PRINCIPAIS” e verificar sua sintaxe e seu funcionamento de cada método, sendo eles:

Adicionar item da lista→ lista.append(item)
Remover item da lista→ lista.pop(indice) ou lista.remove(item)
'''

#Exemplo 6- Usando a função append()

'''
adiciona_mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8'] #Lista atual
print('\n' + 'Os modelos da lista atual, são' , adiciona_mobile, '\n') #Mostrando lista atual
adiciona_mobile.append('MOTO G9') #Adicionando item ao último item da lista
print('O celular', adiciona_mobile[3], 'foi adicionado no estoque com sucesso.')
print('\n' + 'A lista de produtos atualizado é: ', adiciona_mobile) #Item adicionado
'''
#obs sobre o remove(): Se você não declarar o item de lista a ser removido, ele retira o último item da lista.

#Exemplo 7- Agora vamos tentar remover um produto
'''
remove_mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8'] #Lista atual
print('\n' + 'Os modelos da lista atual, são' , remove_mobile, '\n') #Mostrando lista atual
remove_mobile.remove('MOTO G8')
print('O celular MOTO G8 foi removido no estoque com sucesso.')
print('\n' + 'A lista de produtos atualizado é: ',remove_mobile) #lista com o item retirado 
'''
#Exemplo 8 - 
 
#Usando a função pop() para remover um item, diferente do remove, para excluir algum índice da lista você chama direto pelo índice mesmo.
'''
pop_mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8'] #Lista atual
print('\n' + 'Os modelos da lista atual, são' , pop_mobile, '\n')
item_removido = pop_mobile.pop(2) #Chama o índice dentro dos parênteses da função.
print('O celular do modelo {}' .format(item_removido) + ', foi removido no estoque com sucesso.')
print('\n' + 'A lista de produtos atualizado é: ',pop_mobile) #lista com o item retirado 
'''

#Exemplo 9- Tratando o item a ser removido com if

'''
remove_mobile2 = ['MOTO G6', 'MOTO G7', 'MOTO G8']
item_removido2 = [2] #Índice a ser removido

if remove_mobile2 in item_removido2: #SE o moto g9 na lista existir, ele remove
    remove_mobile2.remove('MOTO G9')
else:
    print('\n' + 'O produto MOTO G9, não consta no estoque.') #Senão, imprima que o produto não existe no estoque.

print('\n' + 'Os modelos da lista atual, são:' ,remove_mobile2, '\n')
'''