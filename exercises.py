'''Aqui estão alguns exercícios sobre variáveis simples, tipos primitivos e concatenação:

1. **Variáveis Simples**  
   - Crie uma variável para armazenar o nome de uma pessoa e outra para a idade dela. Como você faria para exibir essas informações juntas?'''
nome = "Ana"
idade = 26
print(f"Sou {nome} e eu tenho {26} anos!")
print("Copilot, não fode não krl.")




'''2. **Tipos Primitivos**  
   - Qual é o tipo primitivo de uma variável que armazena o valor `True`?  
   - Como você pode verificar o tipo de uma variável em Python?'''

ana = True
print(f"A variável {ana} é do tipo:", type(ana), "Boolean")

# 3.Concatenação
nome = "Ana"
sobrenome = "Ramos"
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo)

#Tentando concatenar string com número (gera erro)
#print("Idade: " + 25)  # Isso gera TypeError
print("Idade: " + str(26))  # Correto

# 4. Entrada de Dados
'''numero = input("Digite um número: ")  # Recebe como string

#Para converter para inteiro:

numero_int = int(numero)'''

#Somando strings de números
a = "5"
b = "10"
print("Soma de strings:", a + b)  # Resultado: "510"
#Strings são valores de texto, portanto, não há soma :)

#5.Manipulação de Strings
frase = "Python é incrível"
print("Primeira palavra:", frase.split()[0])  # "Python"
print("Maiúsculo:", "python".upper())  # "PYTHON"
#split() -- função para separar palavras !


#6.Operações com Variáveis
x = 7
y = 2
print("Soma:", x + y)
print("Subtração:", x - y)
print("Multiplicação:", x * y)
print("Divisão:", x / y)  #Resultado da divisão
print("Divisão inteira:", x // y)  # Resultado do resto da divisão

# 7. Interpolação de Strings
nome = "Ana"
idade = 25
print(f"Meu nome é {nome} e eu tenho {idade} anos")  #f-string

# Diferença entre f-string e + 
print("Com +:", "Meu nome é " + nome + " e eu tenho " + str(idade) + " anos")