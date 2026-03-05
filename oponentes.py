import random

def Sheldon(rodada):
    if rodada == 1:
        return "papel"

    return random.choice(["pedra", "papel", "tesoura", "lagarto", "spock"])

def Monarca(jogador):
    if jogador == "pedra":
        return "spock"
    elif jogador == "tesoura":
        return "pedra"
    elif jogador == "papel":
        return "lagarto"
    elif jogador == "lagarto":
        return "tesoura"
    elif jogador == "spock":
        return "papel"

    return random.choice(["pedra", "papel", "tesoura", "lagarto", "spock"])

def Sósia(jogador):
    return jogador
    
def Spock(pontos_jogador, pontos_rival):
    if pontos_rival > pontos_jogador:
        return "spock"
    
    return random.choice(["pedra", "papel", "tesoura", "lagarto", "spock"])
    
def dialogo_especial(rodada, rival, pontos_jogador, pontos_rival):
        if rodada != 4:
            return
        else:
            if rival == "Sheldon":
                if pontos_rival > pontos_jogador:
                    print('"Bazinga!"')
                elif pontos_jogador > pontos_rival:
                    print('"Estatisticamente, esse placar é ilógico."')
                else:
                    print('"Estou com pena de ganhar de você."')

            elif rival == "Monarca":
                if pontos_rival > pontos_jogador:
                    print('"Ajoelhe-se perante a mim!"')
                elif pontos_jogador > pontos_rival:
                    print('"Tropas, recuar!"')
                else:
                    print('"Um duelo acirrado, eu diria."')
        
            elif rival == "Spock":
                if pontos_rival > pontos_jogador:
                    print('"Vida longa e próspera."')
                elif pontos_jogador > pontos_rival:
                    print('"Exemplar de espécie sub-desenvolvida."')
                else:
                    print('"Um erro de cálculo."')

            elif rival == "Sósia":
                if pontos_rival > pontos_jogador:
                    print('"Copying..."')
                elif pontos_jogador > pontos_rival:
                    print('"Copying..."')
                else:
                    print('"Copying..."')
