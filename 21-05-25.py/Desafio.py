'''
DESAFIO:
O cliente da rede de postos de gasolina ESSO-CAMP necessita de um programa coleta dados de
consumo de combustível de diferentes modelos de carros e calcula o gasto estimado em uma viagem
de 1000 km, além de identificar o carro mais econômico.
Para desenvolver o programa, o cliente ESSO-CAMP, nos passou as seguintes informações que
já foi gerado um levantamento de requisitos para o problema, as informações são:

Variáveis Iniciais:
preco = 5.25: Define o preço do combustível por litro.
distancia = 1000: Define a distância da viagem em quilômetros.
carros = [ ] Inicializa uma lista para armazenar os nomes dos modelos de carros.
consumos = [ ]: Inicializa uma lista para armazenar o consumo de combustível (em km por litro) de cada
carro.

Laço While para Inserção de Dados:
O laço while True permite que o programa continue pedindo ao usuário o modelo do carro e seu consumo.
Se o usuário não inserir nenhum nome para o carro (ou seja, pressionar Enter com a entrada vazia), o laço
termina.
Para cada carro inserido, o código verifica se o modelo já está na lista:
Se o modelo já existir, ele adiciona o novo consumo à lista correspondente.
Se for um modelo novo, ele adiciona o carro à lista carros e o consumo à lista consumos.

Cálculo do Consumo Médio:
Para cada carro, o consumo médio é calculado dividindo a soma de todos os consumos registrados pela
quantidade de entradas para aquele carro;
O código identifica o carro com o melhor consumo (maior média de km por litro) e imprime o nome desse
carro.
Cálculo do Custo da Viagem:
Para cada carro, calcula-se o custo da viagem de 1000 km com base no consumo médio. O gasto é dado
pela fórmula: distancia / consumo_medio * preco
O programa exibe o custo de combustível para cada carro.

Impressões Finais:
As listas de carros e consumos são exibidas ao final para que o usuário possa ver os dados coletados.
O código utiliza listas aninhadas para armazenar múltiplos consumos por carro, calculando e exibindo os resultados conforme necessário.
'''
#Para melhor entendimento do usuário, iniciarei o programa colocando uma string explicando a situação para ele entender melhor sobre o nosso aluguel!
linha_maior = '-' * 150
linha = '-' * 60
print(linha_maior)
print(linha, "Olá, bem vindo a RentPerMile!", linha,"\nAqui na RentPerMile, você paga equivalente à sua quilometragem por cada 1000km rodados. --PARA MAIS REGRAS ENTRE EM CONTATO COM O NOSSO SAC. 123-3450-000 ",                         linha_maior)

preco = 5.25  #Preço do combustível por litro
distancia = 1000  #Distância da viagem em km
carros = []  #Lista para armazenar os nomes dos carros
consumos = []  #Lista para armazenar os consumos de cada carro (em listas)


while True:
    modelo = input("Insira o nome do carro --OU PRESSIONE ENTER PARA SAIR: ")
    if modelo == "":
        break #Precisa encerrar o loop e se apertar o enter, sai como uma string vazia.

    consumo = float(input(f"Insira o consumo do {modelo} em km/1: "))

    if modelo in carros: #Usamos o in para percorrer 
        indice = carros.index(modelo)
        consumos[indice].append(consumo) #Acrescentando o consumo na lista vazia e usando o index para procurar o modelo de carro, caso ele não existir ele será adicionado na lista de carros 
    else:
        carros.append(modelo)
        consumos.append([consumo]) #Para criar o consumo

#Calculando os consumos de combustivel
print('\nRelatório de consumo dos carros: ')
print(linha)

#Iniciando os cálculos com strings vazias e partindo do ZERO

consumo_bom = 0
carro_mais_economico = "" 

# Chamando um loop para percorrer no nosso programa!
for i in range(len(carros)):
    # Calcula a média de consumo do carro solicitado
    media = sum(consumos[i]) / len(consumos[i])
    # Calcula o custo da viagem com base no calculo:
    custo = distancia / media * preco

    # Função print para exibir os resultados para este carro:
    print(f"{carros[i]} - Consumo médio: {media:.2f} km/l - Custo da viagem: R${custo:.2f}")

    # Avalia qual é o modelo mais econômico:
    if media > consumo_bom:
        consumo_bom = media
        carro_mais_economico = carros[i]

# Exibe o carro mais econômico no final
print("\nO Carro mais econômico da lista é :")
print(f"{carro_mais_economico} com média de {consumo_bom:.2f} km/l")
