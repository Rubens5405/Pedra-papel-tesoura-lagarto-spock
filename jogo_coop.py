def Jogo(jogador, jogador_2):
    if (jogador == "pedra" and jogador_2 == "tesoura") or \
    (jogador == "pedra" and jogador_2 == "lagarto") or \
    (jogador == "papel" and jogador_2 == "pedra") or \
    (jogador == "papel" and jogador_2 == "spock") or \
    (jogador == "tesoura" and jogador_2 == "papel") or \
    (jogador == "tesoura" and jogador_2 == "lagarto") or \
    (jogador == "lagarto" and jogador_2 == "spock") or \
    (jogador == "lagarto" and jogador_2 == "papel") or \
    (jogador == "spock" and jogador_2 == "tesoura") or \
    (jogador == "spock" and jogador_2 == "pedra"):
        return ("Jogador 1 Venceu!")
    
    elif jogador == jogador_2:
        return ("Empate!")

    else:
        return ("Jogador 2 Venceu!")
