# Definição de cores ansi:
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
magenta = "\033[35m"
ciano = "\033[36m"
cinza = "\033[37m"
reset_cor = "\033[0m"

def exibica_menu ():
    print ("-=-" * 20)
    print (f"{ciano}      SISTEMA-CADASTRO-CLIENTE 2.0 PATRÃO{reset_cor}")
    print ("       (1)-CADASTRAR CLIENTE")
    print ("       (2)-LISTAR CLIENTE")
    print ("       (3)-BUSCAR ALUNO")
    print ("       (4)-ATUALIZAR")
    print ("       (5)-SAIR")

    print ("-=-"*20)

exibica_menu ()

escolha_usuario = None

while True:
    try:
        escolha_usuario = int(input("Escolha uma das opções acima: "))
        break
    except ValueError:
        print (f"{vermelho}Erro: digite apenas números inteiros!{reset_cor}\n")

        if escolha_usuario == 1:
            print ()
            break
        elif escolha_usuario == 2:
            print ()
            break
        elif escolha_usuario == 3:
            print ()
            break
        elif escolha_usuario == 4:
            print ()
            break
        elif escolha_usuario == 5:
            print ()
            break
        else:
            print ()