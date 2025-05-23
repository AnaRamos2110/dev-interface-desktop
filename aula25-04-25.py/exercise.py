#PDF 3
#Comentários: 
# Por padrão e segundo "Guido Van Rossum" (Criado da linguagem Python e atual Engenheiro de software sênior da Microsoft), os comentários utilizam o caracter #, que é seguido por "dois" espaços!

'''Também pode ser feito com aspas simples para maiores textos aonde se realiza documentação.'''
    
"""
Se preferir, pode se usar apóstrofos, porém, lembre-se que as aspas sempre devem ser iguais. Abriu com ' fecha com ' ou, abriu com " fecha com " !! se atente nisso <3 
"""

#Sobre a função print- Imprime o resultado do nosso script.
#EX: 

model = 'T800' #Uma variável com valor de string
print("My model is:", model) #Chamando a variável com a função print

#EXEMPLO 2 

#Execute o código a seguir e repare no retorno da função PRINT()

print('\n') #-- \n tem a função de pular linha dentro do código

print('Eu estudo no SENAC!') #Imprime o texto: Eu estudo no SENAC
print('\n')

#Imprimindo conteúdo das variáveis texto e idade
texto = 'Por lei a bebida alcóolica é vendida apenas para maiores de: '
idade = 18
print(texto, idade)
('\n')

#Tipos primitivos!

#Int ou INTEGER exemplos:
print(11)
print(-11)
#
#Float -> Número que contém casa decimal em QUALQUER  linguagem de programação, exemplos:
print(1.5, 15.00)
print(float(7)) #Usando o float, o número 7 que é um inteiro ganha uma casa decimal após a função ser definida. 
#
#str or String -> É tudo que irá retornar com texto, ou seja, conjuntos de caracteres, exemplos:
print("Meu nome é Ana")

#Bool ou Boolean -> retorna Verdadeiro (True) ou falso (False), exemplos:
print(10 < 9)
print(10 > 9)
print("Eu tenho mais de 18 anos e posso beber?", 19 > 18, "Bora encher a cara!")
print("Eu tenho menos de 18 anos, posso beber?", 17 < 18, "Puts.. fica pra próxima amigão :( ")
#Fim do código 

'''Criem mais algoritmos baseados nos exercicíos, fazendo algumas modificações no código!'''
'''1- Classifique o tipo
Diga qual é o tipo primitivo dos seguintes valores:

"Olá, mundo"

42

3.14

True

"100"'''

print(type("Olá mundo!!")) #Strings
print(type(42)) #Integer
print(type(3.14)) #Float
print(type(True)) #Boolean
print(type("100")) #String

'''2-Descubra o tipo com type()
Imagine que uma variável tem o valor False. Que tipo o comando type() retornaria?'''

valor = False
print(type(valor))


'''3- Diferença entre número e texto
Qual a diferença entre 25 e "25" em Python?'''

#25 é um número inteiro quanto o "25" possui aspas sendo um valor de string

'''4-Operação inválida
O que acontece se você tentar somar o número 10 com a string "5"?'''
soma1 = 10
soma2 = "5"
print(soma1, soma2) #Haverá a junção dos dois números 10 + 5 por 5 ser uma string

'''5-Conversão de tipos
Como transformar uma string "8" em um número inteiro?'''
valores = "8"
print(int(valores))

'''6-Tipos em entrada de dados
Quando você usa input(), qual é o tipo do valor recebido? Como mudar isso?'''
#Ao inserir um input, é recebido um valor de string, para receber um valor especifíco basta informar o tipo primitivo antes da função.
#Exemplo:
seu_nome = input("Qual é seu nome??") #Aceita qualquer valor
sua_idade = int(input("Quantos anos você tem? (Apenas números!)"))
print(f"Seu nome é {seu_nome}, você tem {sua_idade} anos!")

'''7-Booleano na prática
Qual é o valor booleano de uma string vazia ""? E do número 0?'''
#Minha versão 
numero = 0 == bool
print(type(numero))

#Versão do gepeto
print(bool(""))   # Vai mostrar False
print(bool(0))    # Também mostra False


'''8-Detectando o tipo errado
O que acontece se você tentar converter "abc" em um número com int()?

abece = "abc"
print(int(abece))

Isso acontece porque "abc" não representa um número inteiro válido — o int() só aceita strings que pareçam com números, tipo "123" ou "-5".'''

'''9-Verifique o tipo do dado
Como você pode saber se uma variável é do tipo str?
R:Uma string necessita de aspas para anunciar ser um conjunto de caractéres diferente de apenas números, pois contem grafias diferentes, espaços, 
letras maiusculas e minusculas, etc. Logo não se pode declarar uma string sem aspas'''

'''10-Mistura de tipos
Dado: nome = "Ana" e idade = 20. O que acontece se você tentar fazer nome + idade?'''

nome = "Ana"
idade = 26
print(nome,('\n'), idade)