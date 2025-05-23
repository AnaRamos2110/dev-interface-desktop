# Calculadora utilizando while, função (def), IF, Try. Except e Continue:

# Função para efetuar a soma de dois valores
def adicao(x, y):
    return x + y

# Função para efetuar a subtração de dois valores.
def subtracao(x, y):
    return x - y

# Função para efetuar a multiplicação de dois valores:
def multiplicacao(x, y):
    return x * y

# Função para efetuar a divisão de dois valores:
def divisao(x, y):
    return x // y

linha = '-' * 63
print(linha + '\n' + "Selecione UMA das operações: " + '\n')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print(linha + '\n')

while True:
    # Verifica se o INPUT é verdadeiro ou falso
    calculo = input('Insira uma das opções: 1 2 3 ou 4: ')

    # Verifica se a opção é válida
    if calculo not in ('1', '2', '3', '4'):
        print('\n' + '|--ERRO--| --Opção INVÁLIDA--' + '\n')
        continue  # Volta ao início do loop

    try:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
    except ValueError:
        print('\n' + '--O valor inserido é INVÁLIDO--' + '\n')
        continue  # Volta ao início do loop

    # Executa a operação selecionada
    if calculo == '1':
        print(num1, '+', num2, '=> O resultado do cálculo é:', adicao(num1, num2))
    elif calculo == '2':
        print(num1, '-', num2, '=> O resultado do cálculo é:', subtracao(num1, num2))
    elif calculo == '3':
        print(num1, 'x', num2, '=> O resultado do cálculo é:', multiplicacao(num1, num2))
    elif calculo == '4':
        print(num1, '%', num2, '=> O resultado do cálculo é:', divisao(num1, num2))

    # Pergunta se deseja continuar
    novo_calculo = input('Deseja efetuar mais algum cálculo? (sim/não): ')
    if novo_calculo.lower() == 'não' or novo_calculo.lower() == 'n':
        break  # Sai do loop