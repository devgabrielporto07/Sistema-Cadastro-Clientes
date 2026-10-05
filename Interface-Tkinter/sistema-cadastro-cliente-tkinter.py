"""Cadastro de clientes com interface gráfica Tkinter.

Este exemplo usa funções e variáveis simples, sem criar classes.
Os dados ficam em clientes-tkinter.txt, nesta mesma pasta.
"""

from pathlib import Path
import re
import tkinter as tk
from tkinter import messagebox, ttk


# Path(__file__) aponta para esta pasta, independentemente de onde o programa
# for iniciado no terminal.
ARQUIVO_CLIENTES = Path(__file__).with_name("clientes-tkinter.txt")
FORMATO_CPF = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")


def ler_clientes():
    """Lê os clientes e devolve uma lista de dicionários."""
    if not ARQUIVO_CLIENTES.exists():
        return []

    clientes = []
    conteudo = ARQUIVO_CLIENTES.read_text(encoding="utf-8")

    for numero_linha, linha in enumerate(conteudo.splitlines(), start=1):
        partes = linha.split(" - ")
        if len(partes) != 4:
            raise ValueError(f"Formato inválido na linha {numero_linha} do arquivo.")

        identificador, nome, cpf, idade = partes
        if not (
            identificador.isdigit()
            and nome.startswith("Nome do cliente: ")
            and cpf.startswith("Numero do CPF: ")
            and idade.startswith("Idade: ")
        ):
            raise ValueError(f"Formato inválido na linha {numero_linha} do arquivo.")

        clientes.append(
            {
                "id": identificador,
                "nome": nome.removeprefix("Nome do cliente: "),
                "cpf": cpf.removeprefix("Numero do CPF: "),
                "idade": idade.removeprefix("Idade: "),
            }
        )

    return clientes


def salvar_clientes(clientes):
    """Grava a lista inteira no arquivo de dados desta interface."""
    linhas = []
    for cliente in clientes:
        linha = (
            f"{cliente['id']} - Nome do cliente: {cliente['nome']}"
            f" - Numero do CPF: {cliente['cpf']}"
            f" - Idade: {cliente['idade']}"
        )
        linhas.append(linha)

    texto = "\n".join(linhas)
    if linhas:
        texto += "\n"
    ARQUIVO_CLIENTES.write_text(texto, encoding="utf-8")


def validar_nome(nome):
    """Devolve o nome normalizado ou informa por que ele é inválido."""
    nome = " ".join(nome.split())
    if not nome or not nome.replace(" ", "").isalpha():
        return None
    return nome.upper()


def validar_cpf(cpf):
    """Confere se o CPF está no formato 000.000.000-00."""
    return bool(FORMATO_CPF.fullmatch(cpf.strip()))


def validar_idade(idade):
    """Aceita idade com um ou dois algarismos, como no programa de terminal."""
    idade = idade.strip()
    if idade.isdigit() and 1 <= len(idade) <= 2:
        return idade
    return None


def main():
    """Cria a janela, os campos e as ações da interface."""
    janela = tk.Tk()
    janela.title("Sistema de Cadastro de Clientes")
    janela.geometry("900x590")
    janela.minsize(760, 500)

    estilo = ttk.Style(janela)
    if "clam" in estilo.theme_names():
        estilo.theme_use("clam")

    ttk.Label(
        janela,
        text="Sistema de Cadastro de Clientes",
        font=("Segoe UI", 18, "bold"),
    ).pack(pady=(16, 2))
    ttk.Label(
        janela,
        text="Cadastre, consulte, atualize e exclua clientes.",
    ).pack(pady=(0, 14))

    formulario = ttk.LabelFrame(janela, text="Dados do cliente", padding=12)
    formulario.pack(fill="x", padx=18, pady=4)
    formulario.columnconfigure(1, weight=1)

    ttk.Label(formulario, text="Nome:").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=5)
    nome_entrada = ttk.Entry(formulario)
    nome_entrada.grid(row=0, column=1, sticky="ew", pady=5)

    ttk.Label(formulario, text="CPF (000.000.000-00):").grid(
        row=1, column=0, sticky="w", padx=(0, 8), pady=5
    )
    cpf_entrada = ttk.Entry(formulario)
    cpf_entrada.grid(row=1, column=1, sticky="ew", pady=5)

    ttk.Label(formulario, text="Idade:").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=5)
    idade_entrada = ttk.Entry(formulario, width=12)
    idade_entrada.grid(row=2, column=1, sticky="w", pady=5)

    area_botoes = ttk.Frame(formulario)
    area_botoes.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 0))

    area_busca = ttk.Frame(janela)
    area_busca.pack(fill="x", padx=18, pady=(12, 6))
    ttk.Label(area_busca, text="Buscar por nome ou CPF:").pack(side="left")
    busca_entrada = ttk.Entry(area_busca)
    busca_entrada.pack(side="left", fill="x", expand=True, padx=8)

    tabela_frame = ttk.Frame(janela)
    tabela_frame.pack(fill="both", expand=True, padx=18, pady=(0, 8))
    tabela_frame.rowconfigure(0, weight=1)
    tabela_frame.columnconfigure(0, weight=1)

    colunas = ("nome", "cpf", "idade")
    tabela = ttk.Treeview(tabela_frame, columns=colunas, show="headings", height=10)
    tabela.heading("nome", text="Nome")
    tabela.heading("cpf", text="CPF")
    tabela.heading("idade", text="Idade")
    tabela.column("nome", width=420, anchor="w")
    tabela.column("cpf", width=180, anchor="center")
    tabela.column("idade", width=90, anchor="center")
    tabela.grid(row=0, column=0, sticky="nsew")

    barra_vertical = ttk.Scrollbar(tabela_frame, orient="vertical", command=tabela.yview)
    barra_vertical.grid(row=0, column=1, sticky="ns")
    tabela.configure(yscrollcommand=barra_vertical.set)

    status = tk.StringVar(value=f"Os dados serão salvos em: {ARQUIVO_CLIENTES.name}")
    ttk.Label(janela, textvariable=status, anchor="w").pack(fill="x", padx=18, pady=(0, 12))

    def mostrar_clientes(clientes=None):
        """Atualiza a tabela, aplicando a busca se houver um texto digitado."""
        try:
            if clientes is None:
                clientes = ler_clientes()
        except (OSError, UnicodeError, ValueError) as erro:
            messagebox.showerror("Erro ao ler clientes", str(erro), parent=janela)
            return

        termo = busca_entrada.get().strip().casefold()
        for item in tabela.get_children():
            tabela.delete(item)

        exibidos = 0
        for cliente in clientes:
            if termo and termo not in cliente["nome"].casefold() and termo not in cliente["cpf"]:
                continue
            tabela.insert(
                "",
                "end",
                iid=cliente["id"],
                values=(cliente["nome"], cliente["cpf"], cliente["idade"]),
            )
            exibidos += 1

        status.set(f"{exibidos} cliente(s) exibido(s).")

    def limpar_campos():
        nome_entrada.delete(0, tk.END)
        cpf_entrada.delete(0, tk.END)
        idade_entrada.delete(0, tk.END)
        tabela.selection_remove(tabela.selection())
        nome_entrada.focus()

    def cadastrar():
        nome = validar_nome(nome_entrada.get())
        cpf = cpf_entrada.get().strip()
        idade = validar_idade(idade_entrada.get())

        if nome is None:
            messagebox.showwarning(
                "Nome inválido",
                "Digite um nome usando apenas letras e espaços.",
                parent=janela,
            )
            nome_entrada.focus()
            return
        if not validar_cpf(cpf):
            messagebox.showwarning(
                "CPF inválido",
                "Digite o CPF no formato 000.000.000-00.",
                parent=janela,
            )
            cpf_entrada.focus()
            return
        if idade is None:
            messagebox.showwarning(
                "Idade inválida",
                "Digite uma idade com um ou dois algarismos.",
                parent=janela,
            )
            idade_entrada.focus()
            return

        try:
            clientes = ler_clientes()
            if any(cliente["cpf"] == cpf for cliente in clientes):
                messagebox.showwarning(
                    "CPF já cadastrado",
                    "Já existe um cliente com esse CPF.",
                    parent=janela,
                )
                return

            proximo_id = max((int(cliente["id"]) for cliente in clientes), default=0) + 1
            clientes.append(
                {"id": str(proximo_id), "nome": nome, "cpf": cpf, "idade": idade}
            )
            salvar_clientes(clientes)
        except (OSError, UnicodeError, ValueError) as erro:
            messagebox.showerror("Erro ao salvar cliente", str(erro), parent=janela)
            return

        limpar_campos()
        mostrar_clientes()
        messagebox.showinfo("Cadastro concluído", "Cliente cadastrado com sucesso.", parent=janela)

    def selecionar_cliente(*_):
        """Coloca os dados da linha selecionada nos campos do formulário."""
        selecao = tabela.selection()
        if not selecao:
            return

        valores = tabela.item(selecao[0], "values")
        nome_entrada.delete(0, tk.END)
        nome_entrada.insert(0, valores[0])
        cpf_entrada.delete(0, tk.END)
        cpf_entrada.insert(0, valores[1])
        idade_entrada.delete(0, tk.END)
        idade_entrada.insert(0, valores[2])

    def atualizar():
        selecao = tabela.selection()
        if not selecao:
            messagebox.showwarning(
                "Selecione um cliente",
                "Clique em um cliente da tabela antes de atualizar.",
                parent=janela,
            )
            return

        nome = validar_nome(nome_entrada.get())
        idade = validar_idade(idade_entrada.get())
        if nome is None:
            messagebox.showwarning(
                "Nome inválido",
                "Digite um nome usando apenas letras e espaços.",
                parent=janela,
            )
            nome_entrada.focus()
            return
        if idade is None:
            messagebox.showwarning(
                "Idade inválida",
                "Digite uma idade com um ou dois algarismos.",
                parent=janela,
            )
            idade_entrada.focus()
            return

        identificador = selecao[0]
        try:
            clientes = ler_clientes()
            for cliente in clientes:
                if cliente["id"] == identificador:
                    cliente["nome"] = nome
                    cliente["idade"] = idade
                    break
            else:
                messagebox.showerror(
                    "Cliente não encontrado",
                    "Não foi possível localizar o cliente selecionado.",
                    parent=janela,
                )
                mostrar_clientes(clientes)
                return
            salvar_clientes(clientes)
        except (OSError, UnicodeError, ValueError) as erro:
            messagebox.showerror("Erro ao atualizar cliente", str(erro), parent=janela)
            return

        limpar_campos()
        mostrar_clientes()
        messagebox.showinfo("Atualização concluída", "Cliente atualizado.", parent=janela)

    def excluir():
        selecao = tabela.selection()
        if not selecao:
            messagebox.showwarning(
                "Selecione um cliente",
                "Clique em um cliente da tabela antes de excluir.",
                parent=janela,
            )
            return

        if not messagebox.askyesno(
            "Confirmar exclusão",
            "Deseja excluir o cliente selecionado?",
            parent=janela,
        ):
            return

        identificador = selecao[0]
        try:
            clientes = ler_clientes()
            clientes_atualizados = [
                cliente for cliente in clientes if cliente["id"] != identificador
            ]
            if len(clientes_atualizados) == len(clientes):
                messagebox.showerror(
                    "Cliente não encontrado",
                    "Não foi possível localizar o cliente selecionado.",
                    parent=janela,
                )
                mostrar_clientes(clientes)
                return
            salvar_clientes(clientes_atualizados)
        except (OSError, UnicodeError, ValueError) as erro:
            messagebox.showerror("Erro ao excluir cliente", str(erro), parent=janela)
            return

        limpar_campos()
        mostrar_clientes()
        messagebox.showinfo("Exclusão concluída", "Cliente excluído.", parent=janela)

    ttk.Button(area_botoes, text="Cadastrar", command=cadastrar).pack(side="left", padx=(0, 6))
    ttk.Button(area_botoes, text="Atualizar selecionado", command=atualizar).pack(
        side="left", padx=6
    )
    ttk.Button(area_botoes, text="Excluir selecionado", command=excluir).pack(
        side="left", padx=6
    )
    ttk.Button(area_botoes, text="Limpar campos", command=limpar_campos).pack(
        side="left", padx=6
    )

    ttk.Button(area_busca, text="Buscar", command=mostrar_clientes).pack(side="left")
    ttk.Button(
        area_busca,
        text="Mostrar todos",
        command=lambda: (busca_entrada.delete(0, tk.END), mostrar_clientes()),
    ).pack(side="left", padx=(6, 0))
    tabela.bind("<<TreeviewSelect>>", selecionar_cliente)
    busca_entrada.bind("<Return>", lambda *_: mostrar_clientes())

    mostrar_clientes()
    janela.mainloop()


if __name__ == "__main__":
    main()
