# Bibliotecas:
from time import sleep 

# Definição de cores da tabela ANSI:
vermelho = "\033[1;31m"
verde = "\033[1;32m"
amarelo = "\033[1;33m"
azul = "\033[1;34m"
magenta = "\033[1;35m"
ciano = "\033[1;36m"
cinza = "\033[1;37m"
reset_cor = "\033[0m"

# Definição das funções:
def exibica_menu ():
    print ("\nInicializando Sistema....")
    sleep(1)
    print (f"\n{magenta}Seja bem-vindo ao sistema de cadastro de cliente segue o menu abaixo:{reset_cor}")  
    print ("-=-" * 20)
    print (f"{ciano}           SISTEMA-CADASTRO-CLIENTE 2.0 PATRÃO{reset_cor}")
    print (f"{amarelo}            (1)-CADASTRAR-CLIENTE{reset_cor}")
    print (f"{amarelo}            (2)-LISTAR-CLIENTE{reset_cor}")
    print (f"{amarelo}            (3)-BUSCAR-CLIENTE{reset_cor}")
    print (f"{amarelo}            (4)-ATUALIZAR-CLIENTE{reset_cor}")
    print (f"{cinza}            (5)-ENCERRAR{reset_cor}")
    print ("-=-"*20)

def listar_cliente ():
    # Porto
    pass

def cadastrar_cliente ():
    # Kaynan
    pass

def buscar_aluno ():
    # Daniel
    pass

def atualizar_cliente ():
    # Pedro
    pass

# Chamando a função menu:

exibica_menu ()

# Variáveis de escopo global:
escolha_usuario = None
tentativas_usuario = 0
caminho_arquivo = "sistema-cadastro-cliente.txt"
# Estrutura de repetição para construção do código.

while True:

    try:
        escolha_usuario = int(input("Escolha uma das opções acima: "))
        if escolha_usuario in range (1, 6, +1):
            pass # Comando pass serve apenas para continuar o codigo
        else:
            print (f"{vermelho}ERROR: Opção inválida. Escolha um número de 1 a 5.{reset_cor}")
    except ValueError:
        # Valor digitado seja um valor que não comporte o seu tipo primitivo.
        print (f"{vermelho}ERROR: Digite apenas números inteiros.{reset_cor}")
    except KeyboardInterrupt:
        # Exceção para caso o usuário digite Control + C.
        print(f"\n{vermelho}Programa interrompido pelo usuário. Saindo...{reset_cor}")
        break

    # Ideia para caso o usuario repita o erro tenha o numeros de tentativas excedida o programa se encerra.
    if escolha_usuario != 1 and escolha_usuario != 2 and escolha_usuario != 3 and escolha_usuario != 4 and escolha_usuario != 5:
        tentativas_usuario += 1
        if tentativas_usuario >= 3:
            print(f"{vermelho}Número máximo de tentativas excedido! Encerrando...{reset_cor}")
            break
    # Decidir o switch case para trocar um pouco a condicional façam o codigo de vocês dentro de cada case.    
    match escolha_usuario:
        case 1:
            print ("Continua o codigo aqui Kaynan***")
            break
        case 2:
            print ("Continua o codigo aqui Porto***") 
            break
        case 3:
            print ("Continua o codigo aqui Daniel") 
            break
        case 4:
            print ("Continua o codigo aqui Pedro") 
            break
        case 5:
            # Loop contagem regressiva + biblioteca sleep finalizando o programa.
            for loop in range (5, 0, -1):
                print (f"Encerrando em {loop}...")
                sleep(1)
            print (f"{verde}Programa encerrado com sucesso!!!{reset_cor}")
            break