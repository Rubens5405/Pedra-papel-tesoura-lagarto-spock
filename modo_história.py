import time
import keyboard

velocidade_padrao = 0.04
velocidade_media = 0.10
velocidade_lenta = 0.20

def escrita(texto, velocidade_texto):
    pulou = False
    for letra in texto:
        if keyboard.is_pressed('shift'):
            pulou = True
        
        print(letra, end='', flush=True)
        
        if not pulou:
            time.sleep(velocidade_texto)
    print()

def introdução():
    texto = "Muito tempo atrás, a terra era indomável. E por ela, vagavam seres lendários.\n" \
    "Esses seres eram divididos em cinco tribos...\n"

    escrita(texto, velocidade_padrao)

    print(" ")

    texto2 = "Pedra. Tribais e extremamente fortes.\n" \
    "Papel. Monges pacíficos, mas poderosos.\n" \
    "Tesoura. Com o intelecto mais elevado.\n" \
    "Lagarto. Criaturas inexprimíveis que agiam por instinto.\n" \
    "Spock. Misteriosos seres vindos de um mundo distante.\n"

    escrita(texto2, velocidade_media)

    print(" ")

    texto3 = "As tribos viviam em harmonia, mas com o passar dos séculos, elas foram sendo " \
    "esquecidas,\ne seu único resquício histórico é o famoso\n" \
    "Pedra-papel-tesoura-lagarto-spock, jogo popular ao redor dos reinos.\n" \
    "Hoje, o rei está prestes a deixar seu trono, e por não ter herdeiros,\n" \
    "decidiu deixar seu reino nas mãos do vencedor de um grande torneio.\n" \
    "Seres poderosos de todos os continentes estão vindo para jogar, e entre eles, está você.\n"

    escrita(texto3, velocidade_padrao)

    print(" ")

    texto4 = "VOCÊ ESTÁ PRONTO?"

    escrita(texto4, velocidade_lenta)