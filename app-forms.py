import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


class SistemaCadastroClientes:

  def __init__(self, root):
    self.root = root
    self.root.title("Cadastro de Clientes")
    self.root.geometry("450x260")
    self.root.resizable(False, False)

    # Inicializa o banco de dados
    self.conectar_banco()

    # Cria os elementos da interface
    self.criar_widgets()

  def conectar_banco(self):
    """Cria a conexão com o SQLite e a tabela caso não exista."""
    self.conn = sqlite3.connect("clientes.db")
    self.cursor = self.conn.cursor()
    self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)
    self.conn.commit()

  def criar_widgets(self):
    """Monta os rótulos, campos de entrada e botões na tela."""
    frame_principal = tk.Frame(self.root, padx=20, pady=20)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    # Campo Nome
    tk.Label(frame_principal, text="Nome Completo:", font=("Arial", 10)).grid(
        row=0, column=0, sticky=tk.W, pady=5
    )
    self.entry_nome = tk.Entry(frame_principal, width=38, font=("Arial", 10))
    self.entry_nome.grid(row=0, column=1, pady=5)

    # Campo E-mail
    tk.Label(frame_principal, text="E-mail:", font=("Arial", 10)).grid(
        row=1, column=0, sticky=tk.W, pady=5
    )
    self.entry_email = tk.Entry(frame_principal, width=38, font=("Arial", 10))
    self.entry_email.grid(row=1, column=1, pady=5)

    # Campo Telefone
    tk.Label(frame_principal, text="Telefone:", font=("Arial", 10)).grid(
        row=2, column=0, sticky=tk.W, pady=5
    )
    self.entry_telefone = tk.Entry(frame_principal, width=38, font=("Arial", 10))
    self.entry_telefone.grid(row=2, column=1, pady=5)

    # Frame para os botões
    frame_botoes = tk.Frame(frame_principal, pady=20)
    frame_botoes.grid(row=3, column=0, columnspan=2)

    # Botão Salvar
    btn_salvar = tk.Button(
        frame_botoes,
        text="Salvar Cliente",
        command=self.salvar_cliente,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 9, "bold"),
        width=14,
    )
    btn_salvar.pack(side=tk.LEFT, padx=5)

    # Botão Limpar
    btn_limpar = tk.Button(
        frame_botoes,
        text="Limpar",
        command=self.limpar_formulario,
        bg="#f44336",
        fg="white",
        font=("Arial", 9, "bold"),
        width=12,
    )
    btn_limpar.pack(side=tk.LEFT, padx=5)

    # Botão Visualizar Clientes (NOVO)
    btn_visualizar = tk.Button(
        frame_botoes,
        text="Visualizar Clientes",
        command=self.visualizar_clientes,
        bg="#2196F3",
        fg="white",
        font=("Arial", 9, "bold"),
        width=16,
    )
    btn_visualizar.pack(side=tk.LEFT, padx=5)

    # Foca automaticamente no primeiro campo ao abrir
    self.entry_nome.focus()

  def salvar_cliente(self):
    """Valida os dados e insere o novo cliente no banco de dados."""
    nome = self.entry_nome.get().strip()
    email = self.entry_email.get().strip()
    telefone = self.entry_telefone.get().strip()

    if not nome or not email or not telefone:
      messagebox.showwarning(
          "Campos Obrigatórios",
          "Por favor, preencha todos os campos antes de salvar.",
      )
      return

    if "@" not in email or "." not in email:
      messagebox.showwarning(
          "E-mail Inválido", "Por favor, insira um endereço de e-mail válido."
      )
      return

    try:
      self.cursor.execute(
          """
                INSERT INTO clientes (nome, email, telefone)
                VALUES (?, ?, ?)
            """,
          (nome, email, telefone),
      )
      self.conn.commit()

      messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
      self.limpar_formulario()

    except sqlite3.Error as erro:
      messagebox.showerror(
          "Erro no Banco de Dados", f"Não foi possível salvar os dados:\n{erro}"
      )

  def limpar_formulario(self):
    """Apaga o conteúdo de todos os campos de entrada."""
    self.entry_nome.delete(0, tk.END)
    self.entry_email.delete(0, tk.END)
    self.entry_telefone.delete(0, tk.END)
    self.entry_nome.focus()

  def visualizar_clientes(self):
    """Abre uma nova janela listando todos os clientes cadastrados."""
    try:
      self.cursor.execute(
          "SELECT id, nome, email, telefone FROM clientes ORDER BY id ASC"
      )
      registros = self.cursor.fetchall()
    except sqlite3.Error as erro:
      messagebox.showerror(
          "Erro no Banco de Dados",
          f"Não foi possível carregar os clientes:\n{erro}",
      )
      return

    # Cria a janela secundária
    janela_lista = tk.Toplevel(self.root)
    janela_lista.title("Clientes Cadastrados")
    janela_lista.geometry("620x350")
    janela_lista.transient(self.root)  # Mantém a janela associada à principal

    frame_tabela = tk.Frame(janela_lista, padx=10, pady=10)
    frame_tabela.pack(fill=tk.BOTH, expand=True)

    # Configuração da tabela (Treeview)
    colunas = ("id", "nome", "email", "telefone")
    tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

    # Cabeçalhos das colunas
    tabela.heading("id", text="ID")
    tabela.heading("nome", text="Nome Completo")
    tabela.heading("email", text="E-mail")
    tabela.heading("telefone", text="Telefone")

    # Largura e alinhamento das colunas
    tabela.column("id", width=50, anchor=tk.CENTER)
    tabela.column("nome", width=210, anchor=tk.W)
    tabela.column("email", width=200, anchor=tk.W)
    tabela.column("telefone", width=120, anchor=tk.CENTER)

    # Barra de rolagem vertical
    scrollbar = ttk.Scrollbar(
        frame_tabela, orient=tk.VERTICAL, command=tabela.yview
    )
    tabela.configure(yscroll=scrollbar.set)

    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Preenche a tabela com os dados retornados do SQLite
    for cliente in registros:
      tabela.insert("", tk.END, values=cliente)

    # Rodapé com total de registros e botão fechar
    frame_rodape = tk.Frame(janela_lista, pady=8)
    frame_rodape.pack(fill=tk.X, padx=10)

    tk.Label(
        frame_rodape,
        text=f"Total de clientes cadastrados: {len(registros)}",
        font=("Arial", 9, "bold"),
    ).pack(side=tk.LEFT)

    tk.Button(
        frame_rodape, text="Fechar", command=janela_lista.destroy, width=12
    ).pack(side=tk.RIGHT)

  def __del__(self):
    """Garante o fechamento seguro da conexão com o banco ao encerrar."""
    if hasattr(self, "conn"):
      self.conn.close()


if __name__ == "__main__":
  janela = tk.Tk()
  app = SistemaCadastroClientes(janela)
  janela.mainloop()
