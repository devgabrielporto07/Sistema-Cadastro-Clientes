# cores
roxo = '\033[1;32m'
vermelho = '\033[1;31m'
vermelho_suave = '\033[38;5;203m'
amarelo = '\033[1;33m'
verde = '\033[1;36m'
magenta = '\033[1;35m'
fim = '\033[0m'
# Sistema de cadastramento de aluno
while True:
    print(f"{roxo}----------------CADASTRO DE ALUNOS----------------{fim}") #Menu feito por kaynan
    print(f"{verde}1 - Cadastrar Aluno{fim}")
    print(f"{verde}2 - Listar Aluno{fim}")
    print(f"{verde}3 - Buscar Aluno{fim}")
    print(f"{verde}4 - Atualizar Aluno{fim}")
    print(f"{vermelho_suave}5 - Sair{fim}")
    escolha = input("Escolha uma opção!")
    