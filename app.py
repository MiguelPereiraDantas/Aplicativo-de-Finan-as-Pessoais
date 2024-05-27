import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Função para adicionar uma transação ao banco de dados
def adicionar_transacao(tipo, categoria, descricao, valor, data):
    conn = sqlite3.connect('financas_pessoais.db')
    c = conn.cursor()
    c.execute("INSERT INTO transacoes (tipo, categoria, descricao, valor, data) VALUES (?, ?, ?, ?, ?)",
              (tipo, categoria, descricao, valor, data))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")

# Função para obter todas as transações do banco de dados
def obter_transacoes():
    conn = sqlite3.connect('financas_pessoais.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transacoes")
    transacoes = c.fetchall()
    conn.close()
    return transacoes

# Função para exibir as transações no console
def exibir_transacoes():
    transacoes = obter_transacoes()
    for transacao in transacoes:
        print(transacao)

# Função para gerar relatórios com base no período (mensal ou anual)
def gerar_relatorio(periodo):
    conn = sqlite3.connect('financas_pessoais.db')
    query = "SELECT * FROM transacoes"
    df = pd.read_sql_query(query, conn)
    df['data'] = pd.to_datetime(df['data'])
    
    if periodo == 'mensal':
        df = df.groupby(df['data'].dt.to_period('M')).sum()
    elif periodo == 'anual':
        df = df.groupby(df['data'].dt.to_period('Y')).sum()
    
    conn.close()
    return df

# Função para exibir o relatório no console
def exibir_relatorio(periodo):
    relatorio = gerar_relatorio(periodo)
    print(relatorio)

# Função para plotar gráficos usando Matplotlib
def plotar_grafico_matplotlib(periodo):
    df = gerar_relatorio(periodo)
    df.plot(kind='bar')
    plt.title(f'Relatório {periodo}')
    plt.xlabel('Período')
    plt.ylabel('Valor')
    plt.show()

# Função principal para criar a interface gráfica
def criar_janela_principal():
    root = tk.Tk()
    root.title("Gerenciador de Finanças Pessoais")

    # Campos do formulário
    tk.Label(root, text="Tipo").grid(row=0, column=0)
    tipo_var = tk.StringVar()
    ttk.Combobox(root, textvariable=tipo_var, values=["Receita", "Despesa"]).grid(row=0, column=1)

    tk.Label(root, text="Categoria").grid(row=1, column=0)
    categoria_var = tk.StringVar()
    tk.Entry(root, textvariable=categoria_var).grid(row=1, column=1)

    tk.Label(root, text="Descrição").grid(row=2, column=0)
    descricao_var = tk.StringVar()
    tk.Entry(root, textvariable=descricao_var).grid(row=2, column=1)

    tk.Label(root, text="Valor").grid(row=3, column=0)
    valor_var = tk.DoubleVar()
    tk.Entry(root, textvariable=valor_var).grid(row=3, column=1)

    tk.Label(root, text="Data").grid(row=4, column=0)
    data_var = tk.StringVar()
    DateEntry(root, textvariable=data_var, date_pattern='yyyy-mm-dd').grid(row=4, column=1)

    # Botão para adicionar transação
    tk.Button(root, text="Adicionar", command=lambda: adicionar_transacao(
        tipo_var.get(), categoria_var.get(), descricao_var.get(), valor_var.get(), data_var.get())
    ).grid(row=5, column=0, columnspan=2)

    # Botão para exibir transações
    tk.Button(root, text="Exibir Transações", command=exibir_transacoes).grid(row=6, column=0, columnspan=2)

    # Botões para exibir relatórios
    tk.Button(root, text="Relatório Mensal", command=lambda: exibir_relatorio('mensal')).grid(row=7, column=0, columnspan=2)
    tk.Button(root, text="Relatório Anual", command=lambda: exibir_relatorio('anual')).grid(row=8, column=0, columnspan=2)

    # Botões para exibir gráficos
    tk.Button(root, text="Gráfico Mensal", command=lambda: plotar_grafico_matplotlib('mensal')).grid(row=9, column=0, columnspan=2)
    tk.Button(root, text="Gráfico Anual", command=lambda: plotar_grafico_matplotlib('anual')).grid(row=10, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    criar_janela_principal()
