from oponentes import Sheldon, Monarca, dialogo_especial
from jogo import Jogo
import random

escolhas = ["pedra", "papel", "tesoura", "lagarto", "spok"]
oponentes = [Sheldon, Monarca]

rival = random.choice(oponentes)

rodada = 1
pontos_jogador = 0
pontos_rival = 0

for i in range(5):
    opcao = input("Escolha Pedra, Papel, Tesoura, Lagarto ou Spok: ").lower()
    if rival == Sheldon:
        jogada_rival = Sheldon(rodada)
    elif rival == Monarca:
        jogada_rival = Monarca(opcao)

    print(f"{rodada}ª rodada:")
    resultado = Jogo(opcao, jogada_rival)
    if resultado == "Você venceu!":
        pontos_jogador += 1
    elif resultado == "Você perdeu!":
        pontos_rival += 1
    print(resultado)
    print(f"{pontos_jogador}  X  {pontos_rival} \n")
    rodada +=1
    dialogo_especial(rodada, rival, pontos_jogador, pontos_rival)

print(f"Seu oponente era: {rival.__name__}")
print(f"\nVocê  X  {rival.__name__} \n  {pontos_jogador}   X   {pontos_rival}")

