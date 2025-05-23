'''Para entendermos melhor esta estrutura do IF/ELIF, vamos analisar o código a seguir, 
onde o intuito do mesmo, é verificar se a meta de vendas foi atingida ou não, repare que é 
utilizado o IF, ELIF e ELSE, em toda rotina do programa, vejamos:
'''
print('')
linha = '-' * 63 #Pré formatação para backend do código
print(linha + '\n')

meta = 40.000 #Pedindo um valor de meta
equipe = input("Digite sua equipe: ") #Selecionando sua equipe. 
vendas = float(input("Digite o valor vendido: ")) #Dandp entrada no valor das vendas mensais.


while True:
    equipe = input("Qual o nome da sua equipe?")
    consultas += 1

    if vendas < meta:  #SE a venda for menor que meta, a equipe não vai ter sucesso
        print(f"A equipe {equipe} não bateu a meta pois vendeu apenas R$ {vendas}")
     

    elif vendas >= meta:
        print(f"A equipe {equipe} bateu a meta! ")
 

    elif vendas > (meta * 2):
        bonus1 = 0.03 * vendas
        print(f"A equipe {equipe} bateu a meta vendendo {vendas} e obtendo um bônus de R$ {bonus1:.3f}  ")
   

    elif vendas > (meta * 3):
        bonus = 0.07 * vendas
        print(f"A equipe {equipe} atingiu a meta vendendo R${vendas} e obteve um bônus de {bonus:.3f}")
  


