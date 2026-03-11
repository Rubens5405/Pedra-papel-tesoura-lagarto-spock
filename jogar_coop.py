from getpass import getpass

def versus_player(): 
    from jogo_coop import Jogo

    escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]

    pontos_jogador = 0
    pontos_jogador_2 = 0

    print("Escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ")

    def verificação():
        escolha = getpass("Jogador 1: ").lower()
        while escolha not in escolhas:
            print("Opção inválida.")
            escolha = getpass("Tente novamente: ").lower()
        return escolha
    
    def verificação2():
        escolha = getpass("Escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ").lower()
        while escolha not in escolhas:
            print("Opção inválida.")
            escolha = getpass("Tente novamente: ").lower()
        return escolha

    for rodada in range(5):
        opcao = verificação()
        opcao2 = verificação2()
        
        resultado = Jogo(opcao, opcao2)
        if resultado == "Jogador 1 venceu!":
            pontos_jogador += 1
        elif resultado == "Jogador 2 venceu!":
            pontos_jogador_2 += 1

        print(f"{rodada + 1}ª rodada:")
        print(resultado)
        print(f"{pontos_jogador}  X  {pontos_jogador_2}")
        print(f"Seu opononente jogou: {opcao2}")
        print(" ")

    print(f"Resultado final:")
    print(f"\nJogador 1  X  Jogador 2 \n  {pontos_jogador}   X   {pontos_jogador_2}")

versus_player()