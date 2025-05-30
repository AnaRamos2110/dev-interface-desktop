'''
Introdução a Orientação a Objetos com Python
Também conhecida como POO (Programação Orientada a Objetos), trata-se de um modelo
ou paradigma de projeto de um programa, totalmente baseado em na abstração digital,
atualmente com interações entre diversas unidades, o que chamamos de "Objetos" e
"Classes".
'''

'''Introdução a Orientação a Objetos com Python
Esses "Objetos" e "Classes", representam objetos, identidades, propriedades e métodos,
todos baseados em 4 componentes da programação OO, são eles:

-Abstração
-Encapsulamento
-Herança
-Polimorfismo'''

#Exemplo 1-- Abstração 

#Criando uma classe para demonstrar sobre:
'''
class Celular:
    fabricante = 'Nokia'
    modelo = '3310'
    cor = 'Azul'
    camera = False
    bateria = 'Infinita'

    #As funções def (definition) fazer parte do objeto
    #Toda função no python, por padrão, é utilizando o SELF que representa instância da própria classe

    #Funções:
    def fazer_ligacao(self):
        print('Fazer ligações')

    def fazer_calculo(self):
        print('Fazer cálculos')

    def jogar(self):
        print('Abrindo snake-game ')
    
    def despertador(self):
        print('Iniciar despertador todos os dias às 8h da manhã')
'''

'''
Repare que cada objeto pode ser definido
como uma instância de uma classe, tornando
uma hierarquia de classes unidas, através de
um relacionamento de herança, alguns
aspectos devem ser compreendidos e não
podemos deixar de entender,
são eles:
● Cada objeto é uma instância de uma classe;
● Classes são relacionadas com heranças;
● Funções em um bloco de código ou mais;
● Objetos se comunicam com mensagens;
'''

#Exemplo 2-- Herança Para ficar mais claro, este conceito de Orientação a Objetos, vejamos mais um exemplo de Herança de uma forma mais clara:

'''
class Carro:
    combustao = 'Fossil'
    tipo_combustao = 'Flex'
    tipo_de_carro = 'Passeio'
    fabricante = 'FIAT'
    modelo = 500
    ano = 2020
    cavalos = 69

    #Exemplo de FUNÇÕES básicas do objeto CARRO:
    def aceleracao(self):
        print('0 a 100 em 13 segundos...')
    
    def frenagem(self):
        print('Acionamento de ABS')

    def seguranca(self):
        print('Acionamento de AirBag...')


class Argo(Carro):
    modelo = 'Trekking'
    ano = 2024
    cv = 72

#Criando uma instância da classe Argo
argo = Argo()

#Chamando os métodos
argo.aceleracao()
argo.frenagem()
argo.seguranca()

#Imprimindo informações do Argo
print(f"Modelo: {argo.modelo}, Ano: {argo.ano}, Cavalos: {argo.cavalos}")
'''

#Exemplo 3-- Polimorfismo
'''
O prefixo "poli-" tem origem no grego "polus",
que significa "muito" ou "muitos".
Ele é usado em várias palavras ou objetos
para indicar multiplicidade ou variedade. O termo "morfismo" é usado em várias áreas, mas geralmente se refere a uma estrutura que
mantém as propriedades de um objeto quando este é transformado ou mapeado.
'''
#Definimos uma classe chamada 'Animal'

class Animal:
    #Método (função) que será compartilhado por todos os animais que criaremos.
    #Aqui, "emitir_som" não faz nada especifíco ainda, apenas retorna a palavra 'Animal':
    def emitir_som(self):
        return Animal
    
#Criamos uma nova classe chamada 'cachorro' que herda as caracteristicas de 'animal'
#Isso significa que 'cachorro' é um tipo especifíco de 'animal'
class Cachorro(Animal):
    #Sobrescrevemos (substituimos) o método 'emitir_som' da classe Animal
    #Agora, sempre que um objeto 'cachorro' chamar 'emitir_som', ele vai imprimir 'Au au'
    def emitir_som(self):
        print('O som que o cachorro faz é Au au')


class Gato(Animal):
    #Assim como no 'cachorro', o gato tem sua própria versão do método 'emitir_som'
    #Agora, sempre que um objeto 'cachorro' chamar 'emitir_som' ele vai imprimir 'au au'
    def emitir_som(self):
        print('O gato faz Miau miau.')



cachorro = Cachorro() #Uma variável para chamar a classe que criamos acima 
#Criando esta variável ele vai associar a função que estamos ordenando ao código
cachorro.emitir_som()

#Faremos o mesmo para o gato
gato = Gato()
#Aqui imprime que o gato faz 'miau miau'
gato.emitir_som()