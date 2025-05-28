#Olá pra você que está lendo este script. Eu pedi a IA para criar exercicíos, alguns são fáceis e outros são a niveis desafiadores que envolvem um pouco de matemática e juntar mais coisas dentro de um código do que só variáveis. Resolvi deixar em duas partes e como tenho outras atividades para resolver, irei iniciar a parte 2 em breve. Podem usar os exercicíos e ler para aprimorar lógica de programação e sintaxe de python... 



'''Soma Simples
1.Escreva um programa que peça dois números ao usuário e imprima a soma deles.'''

'''numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))
print(f"A soma dos números é: {numero1 + numero2}")'''
#Primeiro eu tinha tentado a função input só com strings comuns mas ele não reconheceu como número então eu forcei a entrada de INTEGER.


'''
2.Par ou Ímpar
Faça um programa que verifique se um número digitado é par ou ímpar.
'''
'''numeros = int(input("Insira um número para verificar se é impar ou par: "))
if numeros / 2 == 0 :
    print(f"O número `{numeros} é par")
else:
    print(f"O número {numeros} é impar")'''
#Ok, eu já fiz esse exercicío umas 3 vezes e consegui lembrar de cabeça!! Estou deverás feliz <3

'''Lista de Compras
3.Crie uma lista de compras (com 5 itens) e depois faça um loop para imprimir cada item com a frase:
"Preciso comprar: [item]'''

'''shop_list = ['Tabaco Dublin', 'Filtro mentolado OCB', 'Seda black BROS', 'Piteira Bem-bolado', 'Clipper' ] #Criando a lista de compras
for i in  range(1): #Fazendo o FOR percorrer a lista 
    print(f"Itens da tabacaria: {shop_list}") #Pedindo para imprimir '''
 
#Tive dificuldades de lembrar do range mas esqueci totalmente que só se pode colocar números dentro dele ~GENIUS~

'''Contador de Vogais
4.Escreva uma função que conte quantas vogais (a, e, i, o, u) existem em uma palavra digitada pelo usuário.'''

'''nome = input("Digite seu nome: ") #Função de input para o usuário inserir os dados

def contador_de_vogais(nome): #Criando a função com parâmetro 
    letras_vogais = ["a", "e", "i", "o", "u"] #Dentro da função contém: uma lista com as vogais disponíveis
    total_vogais = 0 #E um contador inicial
    
    for letra in nome: #Gerando iteração no nome para o loop percorrer o nome e a lista e ver compatibilidades.
        if letra.lower() in letras_vogais: #O lower para mesmo que o usuário digite tudo em maiúsculo, transforme as letras para minúsculo e compatibilize com a lista 
            total_vogais += 1 #Agora o contador gera um número a cada iteração 
    
    return total_vogais #O Return pede para voltar quantas vogais o contador da minha função encontrou e mostra para mim !

total = contador_de_vogais(nome) #Chamando a função
print(f"Seu nome tem {total} vogais!")'''

'''
5.Variáveis & Operadores Aritméticos
Crie duas variáveis (a e b) com números inteiros e imprima a soma deles.'''

'''a = 27
b = 354
print(a + b)'''

'''6.Peça ao usuário para digitar um número e calcule o dobro dele.'''

'''numero = int(input("Digite um número: "))
resultado = numero * 2
print(resultado)'''

'''7.Converta uma temperatura de Celsius para Fahrenheit (F = C * 9/5 + 32).'''

'''temperatura = float(input("Converta esta temperatura para Fahrenheit: "))
conversao = temperatura * 9/5 + 32
print(f"A {temperatura} em graus Celsius fica a {conversao}º Fahrenheit ")'''


'''8.Calcule a área de um círculo (A = π * raio²). Use 3.14 para π.'''
'''import math #Okay, essa biblioteca eu não esqueci então tentei chamar ela no código!
valor_de_pi = math.pi #Obtendo o valor de pi
raio = float(input("Digite o raio do círculo: ")) #Já que eu não queria um valor exato, mais um exercicío com função input para calcular área de qualquer número
area = math.pi * math.pow(raio, 2)  #Usando math.pow para calcular o raio ao quadrado
print(f"A área do círculo com raio {raio} é: {area}")'''
#Achei meio complicado porque eu não entendo nada desse tipo de conta... Porém, consegui fazer algumas coisas de cabeça então fiquei feliz!


'''9.Crie uma variável com seu nome e outra com sua idade. Imprima: "Meu nome é [nome] e tenho [idade] anos."'''
#EASY! Fiz várias vezes 
'''nome = "Ana"
idade = 26
print("Meu nome é:") 
print(nome)
print('')
print("Eu tenho:")
print(idade, "anos!")'''
#A f-string é o amor da minha vida kkkkk #print(f"Meu nome é {nome} e eu tenho: {idade} anos!") -- Beeem melhor 

'''10.🔍 Operadores de Comparação
Peça dois números e diga se o primeiro é maior que o segundo.'''

'''a = 12
b = 45
print(a > b)'''
#Dá pra fazer uma variável para fazer a comparação, mas, da pra fazer dentro da função print() também!

'''11.Verifique se um número digitado é igual a zero.'''
'''numero = int(input("Escolha um número"))
print(numero == 0)'''
#Tranquilo, só queria lembrar como faz o while ai poderia fazer o programa iterar mais vezes, por hora ta bom né 

'''12.Peça a idade do usuário e diga se ele é maior de idade:'''
'''idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Já é maior de idade! Pode tirar habilitação!")
else:
    print("Você ainda é menor de idade.")'''


'''13.Compare duas strings (palavras) e diga se são iguais.'''

'''wordA = "Ana"
wordB = "Maria"
print(wordA == wordB)'''

'''14.Verifique se um número é par (use % para o resto da divisão).'''

'''comparacao = float(input("Digite um número: "))
if comparacao % 2 == 0:
    print(f"{comparacao} é número par!")
else:
    print(f"{comparacao} é ímpar! ")'''
#Okay, fiquei confusa porque já tem exercicío assim, e eu tinha certeza que havia usado outro operador aritmetico... mas ok.

'''🧠 15.Operadores Lógicos (and, or, not)
Peça idade e salário, e diga se a pessoa pode pegar empréstimo (idade >= 18 e salário > 2000).'''

'''print("Seja bem-vindo ao nosso chat-bot! Você gostaria de simular um empréstimo hoje?")
seu_nome = input("Digite seu nome completo: ")
sua_idade = int(input("Por favor, digite sua idade: "))
salario = float(input("Qual o valor do seu salário?: "))
if sua_idade >= 18 and salario >= 2000:
    print(f"Parabéns Sr(a) {seu_nome}! Você atende aos requisitos para solicitar um empréstimo! ")
else:
    print(f"Sr(a) {seu_nome}, sentimos muito mas você não atende aos requisitos para solicitação de empréstimos. Por favor, tente novamente em breve. ")'''

'''16.Verifique se um número está entre 10 e 20 (inclusive).'''

'''nota_de_qualidade = int(input("Qual a sua avaliação?: "))
if 10 <= nota_de_qualidade <= 20:
    print("A nota atende aos critérios de avaliação.")
else:
    print("Qualidade reprovada. ")'''
    #Eu não sabia que eu podia por o número na condição antes de chamar a variável! Nice ><

'''17.Peça uma letra e diga se é vogal ou consoante.'''

'''letra = input("Digite uma letra: ").lower() #Lower para converter em letras minúsculas

if letra in ['a', 'e', 'i', 'o', 'u']:
    print(f"A letra '{letra}' é uma vogal.")
elif letra.isalpha() and len(letra) == 1:
    
    print(f"A letra '{letra}' é uma consoante.")
else:
    print("Por favor, insira apenas uma letra válida.")'''

#OBS: A função isalpha() é um método de string em Python que retorna True se todos os caracteres da string forem letras (alfabéticas) e houver pelo menos um caractere. Caso contrário, ela retorna False. Essa função ignora espaços em branco e caracteres de pontuação, focando apenas em letras.


'''18.Verifique se um ano é bissexto (divisível por 4, mas não por 100, a menos que seja por 400).'''

'''ano = int(input("Insira um ano e veja se ele é bissexto!: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano de {ano} não é bissexto!")'''

'''19.Crie uma senha e peça ao usuário para digitar. Se for correta ("1234"), dê acesso.'''

'''password = input("Qual é a senha?")
if password == '1234':
    print('Acesso permitido!')
else:
    print('Acesso negado.')'''

'''🔄20. Condições (if, elif, else)
Peça um número e diga se é positivo, negativo ou zero.'''

'''
numero = float(input("Digite um número! : ")) #Float porque aí pode ser qualquer número mesmo.
if numero > 0: #Compara se é maior que zero
    print('O número é positivo! ex: 1, 2, 3, 4... ')
elif numero < 0: #Compara se é menor que zero
    print('O número é negativo! ex: -1, -2, -3 , -4... ')
else: #Senão for maior nem menor, então o resultado vai ser zero.
    print('O número é ZERO. ')
'''


'''21.Classifique um aluno com base na nota (A >= 9, B >= 7, C >= 5, D < 5).'''
'''
nota = int(input("Por favor, digite a nota do aluno: "))
if nota >= 9:
    print("Tirou A, parabéns")
elif nota >= 7:
    print("Tirou: B, Bom.")
elif nota >= 5:
    print("Tirou: C, Regular.")
else:
    print("Tirou: D, O aluno está de recuperação.")
'''

'''22.Peça dois números e mostre o maior deles.'''
'''
a = 21
b = 26
if a > b:
    print('A letra A tem o valor maior.')
else:
    print('A letra B tem o valor maior. ')
'''

'''23.Verifique se um triângulo é válido (soma de dois lados > terceiro lado).'''

 
''' 
    # Entrada dos lados do triângulo
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))


#Verificando o tipo de triângulo
if lado1 == lado2 == lado3:
    print("Tipo: Triângulo Equilátero (3 lados iguais)")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Tipo: Triângulo Isósceles (2 lados iguais)")
else:
    print("Tipo: Triângulo Escaleno (3 lados diferentes)")
'''

'''24.Crie um sistema de login com usuário e senha. Se ambos corretos, dê acesso.'''
'''
user_login = input('Insira o usuário: ')
user_password = input('Insira a senha: ')
login = 'user01'
password = '1234'

if user_login == login and user_password == password:
    print('Acesso permitido.')
else:
    print('Acesso negado.')
'''

'''🌀 25.Loops (while, for)
Imprima os números de 1 a 10 usando while.'''
'''
for i in range(11):
    print(i)
'''
