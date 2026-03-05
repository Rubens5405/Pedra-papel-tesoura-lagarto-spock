from modo_história import introdução
from jogar import versus_cpu

print("Bem-vindo, escolha seu modo de jogo:")

while True:
    opcoes = input("Modo História - 1 \nContra o Computador - 2\nVersus Local -"\
" Em construção \nSair do jogo - 4")
    
    if opcoes == "1":
        print ("Segure shift para pular a introdução.")
        introdução()

    elif opcoes == "2": 
        versus_cpu()

    elif opcoes == "4":
        break

    else: 
        print("Opção inválida!")