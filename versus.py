from getpass import getpass

def versus_player():
    Nome1 = input("\nJogador 1, Insira seu nome (Ou deixe vazio): ") or "Jogador 1"
    Nome2 = input("Jogador 2, Insira seu nome (Ou deixe vazio): ") or "Jogador 2"

    from jogo import Jogo

    escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]

    pontos_jogador = 0
    pontos_jogador_2 = 0

    print("\nEscolha entre Pedra, Papel, Tesoura, Lagarto ou Spock:")

    def verificação():
        escolha = getpass(f"{Nome1}: ").lower()
        while escolha not in escolhas:
            escolha = getpass("Opção inválida, tente novamente: ").lower()
        return escolha
    
    def verificação2():
        escolha = getpass(f"{Nome2}: ").lower()
        while escolha not in escolhas:
            escolha = getpass("Opção inválida, tente novamente: ").lower()
        return escolha

    for rodada in range(5):
        opcao = verificação()
        opcao2 = verificação2()
        
        print(f"\n{rodada + 1}ª rodada:")
        resultado = Jogo(opcao, opcao2)
        if resultado == "Você venceu!":
            pontos_jogador += 1
            print(f"{Nome1} venceu!")
        elif resultado == "Você perdeu!":
            pontos_jogador_2 += 1
            print(f"{Nome2} venceu!")
        print(f"{pontos_jogador}  X  {pontos_jogador_2}")
        print(f"{Nome1} jogou: {opcao}")
        print(f"{Nome2} jogou: {opcao2}\n")

    print(f"Resultado final:")
    print(f"{Nome1}  X  {Nome2} \n  {pontos_jogador}   X   {pontos_jogador_2}")
