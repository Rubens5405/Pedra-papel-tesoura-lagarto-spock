import random

def Sheldon(rodada):
    if rodada == 1:
        return "papel"
    
    return random.choice(["pedra", "papel", "tesoura", "lagarto", "spock"])

def Monarca(jogador):
    if jogador == "pedra":
        return "papel"
    elif jogador == "tesoura":
        return "tesoura"
    elif jogador == "papel":
        return "papel"

    return random.choice(["pedra", "papel", "tesoura", "lagarto", "spock"])

def dialogo_especial(rodada, rival, pontos_jogador, pontos_rival):
        if rodada != 4:
            return
        if rival == Sheldon:
            if pontos_rival > pontos_jogador:
                print("Bazinga!")
            elif pontos_jogador > pontos_rival:
                print("Estatisticamente, esse placar é ilógico.")
            else:
                print("Estou com pena de ganhar de você.")

        elif rival == Monarca:
            if pontos_rival > pontos_jogador:
                print("Ajoelhe-se perante a mim!")
            elif pontos_jogador > pontos_rival:
                print("Tropas, recuar!")
            else:
                print("Um duelo acirrado, eu diria.")