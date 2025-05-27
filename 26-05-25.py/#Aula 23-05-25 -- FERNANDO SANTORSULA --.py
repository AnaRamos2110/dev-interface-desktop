#Aula 23-05-25 -- FERNANDO SANTORSULA -- 
'''
O que são Dicionários em Python?
Dicionários são um tipo de estrutura de dados em Python que permitem armazenar pares de chave e
valor.
Eles são similares a listas, mas ao invés de usarem índices numéricos, utilizam chaves que podem
ser strings, números, ou até tuplas.
Dicionários são muito úteis quando queremos mapear uma informação para outra, como um nome
para um número de telefone ou um produto para o seu preço. Exemplo:
'''

#EXemplo1-- 

agenda = {
    'João' : '1234-5678',
    'Maria': '1234-5678',
    'Carlos': '1234-6661'
}

#Acessar o número de telefone do João:
print(agenda['João'])

#Neste exemplo criamos um dicionário chamado agenda onde as chaves são os nomes e os valores são os números de telefone.

'''
Qual a diferença entre Dicionários e Listas no Python?
Dicionários são um tipo de estrutura de dados em Python que permitem armazenar pares de chave e valor.
Eles são similares a listas, mas ao invés de usarem índices numéricos, utilizam chaves que podem ser
strings, números, ou até tuplas.
Dicionários são muito úteis quando queremos mapear uma informação para outra, como um nome para um
número de telefone ou um produto para o seu preço. Exemplo:
'''

'''
1o Estrutura:
Listas: São coleções ordenadas de elementos que podem ser acessados por índices inteiros (0, 1, 2, ...). Uma lista
armazena os elementos em sequência.
Exemplo: lista = [10, 20, 30]
Acessa o valor pelo índice: lista[0] retorna 10
Dicionários: São coleções não ordenadas de pares chave: valor. Cada item é armazenado com uma chave
associada, que pode ser de qualquer tipo imutável (como strings, números ou tuplas);
Exemplo: dicionario = {"nome": "Fernando", "idade": 30}
Acessa o valor pela chave: dicionario["nome"] retorna "Fernando"
Curso: Técnico em Desenvolvimento de Sistemas - Semestre: 1S/2025

2o Acesso aos dados:
Listas: Os itens são acessados pelos índices numéricos.
Dicionários: Os itens são acessados pelas chaves.
3o Organização:
Listas: Mantêm a ordem de inserção dos elementos.
Dicionários (a partir do Python 3.7): Também mantêm a ordem de inserção das chaves, mas
tradicionalmente não eram ordenados.
4. Utilização:
Listas: Usadas quando você tem um grupo de itens relacionados e deseja acessá-los sequencialmente ou
por posição.
Dicionários: Usados quando você precisa armazenar pares de chave-valor e quer acessar os valores por
meio de chaves nomeadas.
Vamos analisar um exemplo PRÁTICO no próximo slide, o que fará mais sentido nesta abordagem:
'''

#Exemplo 2- Dicionários e listas python
#Isso é uma lista, ok?? 

frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas[1]) #Acessa o segundo elemento: "banana"

#Isso é um dicionário, ok??
frutas_precos = {'Maçã': 2.5, 'Banana': 1.5, 'Laranja ': 3.0}
print(f' O preço da', frutas_precos['Banana'], 'está saindo a R$ o kg') #Acessa o preço da banana
#O dicionário vai acessar os valores e não as strings. Então vamos aproveitar que a gente tem uma lista para fazer uma fase mais consisa.
print(f'O preço da {frutas[1]} está saindo pelo valor de R$:', frutas_precos['Banana'], 'o Kilo.') #Bem melhor :)

#Exemplo 3
'''
Vamos analisar vários exemplos dos dicionários na linguagem Python, após nossa compreensão,
vamos reproduzir TODOS os exemplos, fixando o aprendizado nessa FUNÇÃO nativa do Python,
vejamos:
'''
produtos = {
    'Cadeira': 150.00,
    'Mesa': 450.00,
    'Sofá': 1200.00,
}

#Para acessar o preço da cadeira
print(f" O valor da cadeira é de R$ {produtos['Cadeira']} reais.")

#Adicionar um novo produto:
produtos['Armário'] = 750.00
print(produtos)


#EXemplo 4-- Este para conferir notas de alunos
notas_alunos =  {
    'Ana': 9.5,
    'Vivi': 7.8,
    'Luan': 10.0,
    'Pedro': 10.0,
    }

#Acessar as notas da aluna Ana (eu mesma kkk)

print(notas_alunos['Ana'])



'''
Exercício 1o - Cadastro de Produtos
Crie um programa que permita cadastrar produtos em um estoque. Para cada produto, armazene o
nome, a quantidade e o preço unitário. O programa deve permitir:
● Adicionar novos produtos;
● Atualizar a quantidade de um produto existente;
● Remover produtos do estoque;
● Exibir todos os produtos cadastrados;
'''

#Exercicío 1--

estoque = {}  # Começa com um dicionário vazio

# Função para adicionar produtos
def adicionar_produto(nome, quantidade, preco):
    if nome in estoque:
        # Se o produto já estiver no estoque, aumenta a quantidade
        estoque[nome]['quantidade'] += quantidade
    else:
        # Caso contrário, adiciona o produto com quantidade e preço
        estoque[nome] = {'quantidade': quantidade, 'preço': preco}

# Função para remover produtos
def remover_produto(nome):
    if nome in estoque:
        del estoque[nome]

# Função para exibir o estoque formatado
def exibir_estoque():
    for produto, dados in estoque.items():
        preco_formatado = f"R$ {dados['preço']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f"Produto: {produto}, Quantidade: {dados['quantidade']}, Preço: {preco_formatado}")

# Teste das funções
adicionar_produto('Cadeira', 10, 120.00)
adicionar_produto('Mesa', 5, 300.00)
adicionar_produto('Cadeira', 2, 120.00)  # Atualiza a quantidade da cadeira
remover_produto('Mesa')
exibir_estoque()

'''
Exercício 2o - Agenda
Crie uma agenda usando um dicionário, onde as chaves são os nomes das pessoas e os valores são
seus números de telefone. O programa deve permitir:
● Adicionar um novo contato;
● Remover um contato;
● Buscar um contato pelo nome;
● Exibir todos os contatos.
'''

agenda = {}

def adicionar_contato(nome, telefone):
    agenda[nome] = telefone

def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]

def buscar_contato(nome):
    telefone = agenda.get(nome)
    if telefone:
        return f'O telefone encontrado foi {telefone}'
    else:
        return 'Contato não encontrado'
    
def exibir_contatos():
    for nome, telefone in agenda.items():
        print(f'Nome: {nome} \nTelefone: {telefone}')

#Testando
adicionar_contato('Ana', '1234-567')
adicionar_contato('Paulin', '4533-5432')
remover_contato('Ana')
print(buscar_contato('Paulin'))
exibir_contatos()

#Tuplas-- o que são:
'''
Tuplas no Python
Tuplas são coleções de elementos que podem armazenar múltiplos itens em uma única variável. Elas
são semelhantes às listas, mas com algumas diferenças principais:
Características das Tuplas:
Imutáveis: Uma vez criadas, as tuplas não podem ser modificadas (ou seja, você não pode
adicionar, remover ou alterar elementos).
Indexadas: Assim como listas, os elementos de uma tupla podem ser acessados usando índices.
Podem conter elementos de diferentes tipos: Tuplas podem armazenar diferentes tipos de dados,
incluindo números, strings e outras tuplas.
'''

#Exemplo 1 -- criando uma tupla

tupla = (0, 1 , 2, 'python', 3)
print(tupla)

#Acessando elementos da tupla
print(tupla[0])
print(tupla[3])

#Adicionando iterações
for elemento in tupla:
    print(elemento)

'''
Exercícios práticos de Tuplas no Python
Agora que já entendemos o funcionamento das Tuplas no Python, vamos exercitar! Vamos fazer
exercícios com mais recursos, simulando uma possível solução de software para o mundo real, vejamos:
'''

'''
Exemplo 1o - Sistema de Cadastro de Produtos
O cliente XTPO necessita de um sistema que efetue o cadastro de cada produto, para ser
armazenado em uma tupla com seu nome, preço e quantidade em estoque.
'''

#Exercicío 1
produtos = []

def adicionar_produto(nome, preco, quantidade):
    produto = (nome, preco, quantidade)
    produtos.append(produto)

def exibir_produtos():
    for produto in produtos:
        nome, preco, quantidade = produto
        print(f'Produto: {nome} \nPreço: R$ {preco:.2f} \nQuantidade: {quantidade}')

#adicionando produtos
adicionar_produto('Cadeira', 120.00, 50)
adicionar_produto('Mesa', 300.00, 20)

#Exibindo produtos cadastrados
exibir_produtos()

#Exercicío 2

#Lista para armazenar funcionários
funcionarios = []

def adicionar_funcionario(nome, cargo, salario):
    funcionario = (nome, cargo, salario)
    funcionarios.append(funcionario)

def exibir_funcionarios():
    for funcionario in funcionarios:
        nome, cargo, salario = funcionario
        print(f"Nome: {nome}  \nCargo:  {cargo}  \nSalário {salario}")

#Adicionando funcionários
adicionar_funcionario('Ana', 'dba', '???')
adicionar_funcionario('Paulin', 'frontend', '???')

#Exibindo nossa nova lista
exibir_funcionarios()

#EXercicio 3 -- tuplas
#Lista pra armazenar clientes

clientes = []

def adicionar_cliente(nome, telefone, email):
   cliente = (nome, telefone, email)
   clientes.append(cliente)

def exibir_clientes():
    for cliente in clientes:
        nome, telefone, email = cliente
        print(f"Nome: {nome}, Telefone {telefone}, Email: {email} ")

#Adicionando clientes
adicionar_cliente('Jose', '1234-6777', 'dlofgvs@gg')
adicionar_cliente('Maria', '123-545433', 'dfbdv@.com')
exibir_clientes()