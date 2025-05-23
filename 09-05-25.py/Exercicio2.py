'''Com as estruturas de condições, temos INÚMERAS possibilidades de fazer o mesmo
programa de VÁRIAS formas, vejamos mais um exemplo com o uso do IF.

O programa deve capturar o código do produto inserido pelo usuário, analisando se o
código do produto está em CAIXA ALTA ou em caixa baixa, identificar se o código do
produto corresponde a sua categoria e retornar o nome da categoria do produto, analise o
código a seguir.'''

#Exercicio #2: Crie um algoritmo com a função "in" que verifica se EXISTE ou Não, algum  determinado conteúdo em alguma STRING, exemplo:
#Será criado um algoritmo para receber um código do usuário para verificar se a bebida é alcoólica ou não.

cod_bebida_com_alcool = 'BCA001' #Definindo código base
cod_bebida_sem_alcool = 'BSA001'
linha = '-' * 63

print('\n' + linha)
bebida = input("Insira o código da bebida em LETRA MAIÚSCULA: ") #Solicitando entrada de dados do produto para a analise
if 'BCA' in bebida:
    print('\n' + linha)
    print('Este código é referente à bebida Alcoólica e o código do produto é: ', cod_bebida_com_alcool)
    print(linha)

else:
    print('\n' + linha)
    print('Este código é referente a bebida SEM  álcool e o código do produto é: ', cod_bebida_sem_alcool)
    print(linha)