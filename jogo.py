def Jogo(jogador, oponente):
    if (jogador == "pedra" and oponente == "tesoura") or \
    (jogador == "pedra" and oponente == "lagarto") or \
    (jogador == "papel" and oponente == "pedra") or \
    (jogador == "papel" and oponente == "spock") or \
    (jogador == "tesoura" and oponente == "papel") or \
    (jogador == "tesoura" and oponente == "lagarto") or \
    (jogador == "lagarto" and oponente == "spock") or \
    (jogador == "lagarto" and oponente == "papel") or \
    (jogador == "spock" and oponente == "tesoura") or \
    (jogador == "spock" and oponente == "pedra"):
        return ("Você venceu!")
    
    elif jogador == oponente:
        return ("Empate!")

    else:
        return ("Você perdeu!")
