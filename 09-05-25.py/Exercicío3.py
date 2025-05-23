#Algoritmo para calcular  o Faturamento mensal de uma empresa para saber se ela teve lucros:

linha = '-' * 63 #Breve fprmatação na saída de terminal
faturamento = int(input("Insira o faturamento mensal: ")) #Pedindo valores de faturamento
custo = int(input('Insira o custo mensal: ')) #Pedindo valores de custos
print('\n' + linha)
print(f'O lucro mensal foi de R$ {faturamento - custo:.2f}')
print(linha)
#Comparação (MENOR) Verifica se a váriavel faturamento é menor que a variável custo.
if faturamento > custo :
    print('\n' + linha)
    print('Sua empresa está tendo lucros. ')
    print(linha)
else: 
    print('Sua empresa está tendo prejuízo. ')

    