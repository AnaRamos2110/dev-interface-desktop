#Revisão py- Prof Santorsula :))
#Este exercicío revisa sobre se uma empresa obteve lucro vendendo latas de refrigerante ou se obteve prejuízo- Reforçando tabela verdade, lógica bool e condições python;

#Quantidade de coca-cola(lata) vendida = 100 unidades
#Quantidade de pepsi(lata) vendida = 50 unidades
'''----------------------------------------------------------------------------------------'''
#Valor unitário da coca-cola(lata) = R$4.50
#Valor unitário da pepsi(lata) = R$3.90
'''----------------------------------------------------------------------------------------'''
#Investimento total de produtos = R$6.000,00

qnt_coca = 100 #Sempre deixe suas variáveis intuitivas e limpas para melhor compreensão do código
qnt_pepsi = 50
valor_da_coca = 4.50
valor_da_pepsi = 3.90
investimento = 6.000
linha = '-' * 63

print('\n' + linha)
print(f"O total de vendas de latas de Coca-cola foi de: R$ {qnt_coca * valor_da_coca:,.2f}") #Faturamento de cada produto
print(f"O total de vendas de latas de Pepsi foi de: R$ {qnt_pepsi * valor_da_pepsi:,.2f}")

faturamento = (qnt_coca * valor_da_coca) + (qnt_pepsi * valor_da_pepsi) #Calculando faturamento geral

print(f"A empresa obteve um total de R${faturamento} na venda de refrigerante" '\n')
print(linha + '\n')
print(f"O faturamento das vendas de latas de refrigerante foi de R$ {investimento - faturamento:,.2f}" + '\n')

if investimento < faturamento:
    print(linha + '\n')
    print('A empresa obteve prejuízo na venda de refrigerantes. ')
    print(linha + '\n')
else:
     print(linha + '\n')
     print('A empresa obteve lucro nas vendas de refrigerante!')
     print('\n' + linha)