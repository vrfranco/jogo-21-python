import random
import os

def pegar_baralho():

    base = []

    cartas = []

    base.append({'nome': 'A','valor': 1})

    base.extend([{'nome': index, 'valor': index}  for index in range(2,11)])

    base.extend([{'nome': index, 'valor': 10} for index in ['J', 'Q', 'K']])

    for item in base:
        for tipo in ['ouros', 'paus', 'copas', 'espadas']:
            cartas.append({
                'nome': item['nome'],
                'valor': item['valor'],
                'tipo': tipo
            })

    return cartas

def pegar_jogadores():

    quantidade = input("Quantos Jogadores?")

    jogadores = []

    for indice in range(0, quantidade):
        jogadores.append({
            'nome': 'Jogador %d' % (indice+1),
            'cartas': []
        })

    return jogadores

def pegar_carta(baralho):

    escolhido = random.choice(baralho)

    indice = baralho.index(escolhido)
    
    del baralho[indice]

    return escolhido

def distribuir_cartas(jogadores, baralho):

    for jogador in jogadores:
        jogador['cartas'].append( pegar_carta(baralho) )
        jogador['cartas'].append( pegar_carta(baralho) )

    return jogadores

def obter_pontos(jogador):
    return sum([carta['valor'] for carta in jogador['cartas']])

def obter_pontos_as(jogador):
    return sum([11 if carta['nome'] == 'A' else carta['valor'] for carta in jogador['cartas']])

def tem_as(jogador):

    return len( filter(lambda x: x['nome'] == 'A', jogador['cartas']) ) > 0

def mostrar_informacoes(jogadores):

    for jogador in jogadores:

        print("---------")
        print(jogador['nome'])

        mesa = ['%s(%s)' %(carta['nome'], carta['tipo']) for carta in jogador['cartas']]

        if tem_as(jogador):
        
            pontos = obter_pontos_as(jogador)

            print('[Pontos]: %d (com As)' % (pontos))

        pontos = obter_pontos(jogador)

        print('[Pontos]: %d (sem As)' % (pontos))
        print('[Cartas]: %s' % (','.join(mesa)))

os.system('clear')

vez = 0

descartadas = []

baralho = pegar_baralho()

jogadores = pegar_jogadores()

jogadores = distribuir_cartas(jogadores, baralho)

while True:

    os.system('clear')

    print('=========')
    print('JOGADORES')

    mostrar_informacoes(jogadores)

    if len(descartadas)>0:
        print('\n')
        print('=========')
        print('ULTIMA CARTA DESCARTADA')
        print('Carta: %s (%s)' % (descartadas[-1]['nome'], descartadas[-1]['tipo']))

    print('\n')
    print('=========')
    print('%s Escolhe a Jogada' % (jogadores[vez]['nome']))
    print('---------')
    print('1) Pegar Carta do Baralho')
    print('2) Pegar Carta Descartada')
    print('3) Encerrar Jogo')

    evento = input("Escolha: ")

    if evento == 1:

        print('\n')
        print('=========')
        print('%s Resolve a Carta Obtida' % (jogadores[vez]['nome']))
        print('---------')

        escolhido = pegar_carta(baralho)

        print('Carta obtida: %s(%s)' %(escolhido['nome'], escolhido['tipo']))
        print('---------')

        print('1) Pegar')
        print('2) Pegar e Descartar')
        print('3) Descartar')

        evento = input("Escolha: ")

        if evento == 1:

            jogadores[vez]['cartas'].append(escolhido)

        elif evento == 2:

            print('\n')
            print('=========')
            print('%s Escolha a carta para Descartar' % (jogadores[vez]['nome']))

            print('Cartas disponiveis')

            for indice, carta in enumerate(jogadores[vez]['cartas']):
                print('%d) %s (%s)' %(indice, carta['nome'], carta['tipo']))
            
            indice = input("Escolha a Carta a descartar: ")

            descartado = jogadores[vez]['cartas'][indice]

            del jogadores[vez]['cartas'][indice]

            descartadas.append(descartado)

            jogadores[vez]['cartas'].append(escolhido)

        elif evento == 3:

            descartadas.append(escolhido)

    elif evento == 2:
        
        escolhido = descartadas[-1]

        del descartadas[-1]

        jogadores[vez]['cartas'].append(escolhido)

    elif evento == 3:

        break

    if vez < len(jogadores) - 1:
        vez = vez + 1
    else:
        vez = 0

print("+++++++++++")
print("FIM DE JOGO")
print("-----------")
mostrar_informacoes(jogadores)
print("+++++++++++")