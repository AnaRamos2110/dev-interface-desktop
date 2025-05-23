'''
Nesta segunda parte deste tema, vamos retomar com mais Exercícios práticos voltado a
Estruturas de Repetição, seguindo os padrões da linguagem Python, trazendo casos de
estudos reais, que podem ser aplicados em ambiente de produção, analise o código a seguir:
'''

#Exemplo 1

#Variavel i armazena dados do metodo enumerate
'''
funcionarios = [ 'Maria Silva', 'José Inácio', 'Fernando Rodrigues', 'Luiz Santos']
for i, lista_funcionarios in enumerate(funcionarios):
    print('{} -> é o índíce do funcionário: {}' .format(i, lista_funcionarios))
'''

#Exemplo 2
'''
Seguindo com os exercício, analise o código a seguir, referente a um sistema de
verificação de metas de vendas, criado com outra lógica, utilizando o FOR e Listas na
linguagem Python, vejamos:
'''
'''
meta = 10000
valor_vendas = [
    ['João Paulo', 15000],
    ['Pedro Silva', 14000],
    ['Júlio Matos', 16000],
    ['Ronaldo Silveira', 9000],
]

print("O valor da meta do mês de julho é de R$",meta, '\n')
for item in valor_vendas:
    if item[1] > meta:
        print('Vendedor {} BATEU a meta, com o valor de vendas de R$ {}'.format(item[0], item[1]))
    else:
        print('\n' + 'Vendedor {} "NÃO" bateu a meta, com o valor de vendas de R$ {}'.format(item[0],item[1]))
'''

#Exemplo 3
'''
Repare no código a seguir que temos um código muito simples que encerra quando
encontra uma condição verdadeira determinada pelo While, onde precisamos de um IF
somente para fazer a comparação do valor digitado pelo usuário é verdadeiro ou falso,
porém neste programa a informação é 100% FALSA, vejamos:
'''

'''
linha = '-' * 63
while True:
    print(linha)
    valida_mundial = input("O Palmeiras tem mundial?? : Sim ou Não?? --> ")
    if valida_mundial == 'sim':
        print("Incorreto! O Palmeiras não tem mundial. DEAL WITH THIS! ")
        break
    else:
        print('\n' + 'Correto! O Palmeiras não tem Mundial :)) ' + '\n')
'''
#Exemplo 4
'''
Antes do último código, vamos aprender como fazer uma calculadora com o While,
utilizando alguns outros métodos auxiliares, incluindo condicionais (IF, ELSE), analise o
código a seguir e sua lógica.
'''

#Calculadora utilizando while, função (def), IF, Try. Except e Continue:

#Função para efetuar a soma de dois valores
def adicao(x, y):
    return x+y

#Função para efetuar a subtração de dois valores.
def subtracao(x, y):
    return x - y

#Função para efetuar a multiplicação de dois valores:
def multiplicacao(x, y):
    return x * y

#Função para efetuar a divisão de dois valores:
def divisao (x, y):
    return x // y

linha = '-' * 63
print(linha + '\n' + "Selecione UMA das operações: " + '\n')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão ')
print(linha + '\n')

while True:
    #Verifica se o INPUT é verdadeiro ou falso
    calculo = input('Insira uma das opções: 1 2 3 ou 4: ')


#Oçoes para escolha do usuário:
if calculo in ('1', '2', '3', '4'):
    try:
        num1= int(input("Insira o primeiro número: "))
        num2= int(input("Insira o segundo número: "))
    except ValueError:
        print('\n' + '--O valor inserido é INVÁLIDO--'+ '\n') 
        continue


if calculo == '1':
    print(num1, '+', num2, '=> O resultado do cálculo é:', adicao(num1, num2))
elif calculo == '2':
    print(num1, '-', num2, '=> O resultado do cálculo é:', subtracao(num1, num2))
elif calculo == '3':
    print(num1, 'x', num2, '=> O resultado do cálculo é:', multiplicacao(num1, num2))
elif calculo == '4':
    print(num1, '%',num2, '=> O resultado do cálculo é:', divisao(num1, num2))

#Interrompe o loop do While se a resposta for não
novo_calculo = input('Deseja efetuar mais algum cálculo? (sim/não): ')
if novo_calculo == 'não':
    break

else:
    print('\n' + '|--ERRO--| --Opção INVÁLIDA--' + '\n')