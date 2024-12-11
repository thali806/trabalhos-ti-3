import tkinter as tk
from tkinter import messagebox, colorchooser
from tkcalendar import Calendar

# Função para salvar o compromisso na lista
def salvar_compromisso():
    compromisso = entrada_compromisso.get()
    descricao = entrada_descricao.get()
    data = calendario.get_date()
    cor = cor_selecionada

    if compromisso == "" or descricao == "" or cor == "":
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos e escolha uma cor.")
    else:
        compromisso_formatado = f"{compromisso} - {data} - {descricao}"
        lista_compromissos.insert(tk.END, compromisso_formatado)
        lista_compromissos.itemconfig(tk.END, {'bg': cor})
        
        # Limpar os campos após salvar
        entrada_compromisso.delete(0, tk.END)
        entrada_descricao.delete(0, tk.END)

# Função para remover o compromisso selecionado
def remover_compromisso():
    try:
        selecionado = lista_compromissos.curselection()
        lista_compromissos.delete(selecionado)
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione um compromisso para remover.")

# Função para escolher a cor do compromisso
def escolher_cor():
    cor_escolhida = colorchooser.askcolor()[1]  # Retorna a cor escolhida no formato hexadecimal
    if cor_escolhida:
        cor_button.config(bg=cor_escolhida)
        global cor_selecionada
        cor_selecionada = cor_escolhida

# Criar a janela principal
root = tk.Tk()
root.title("Agenda Pessoal")

# Inicializar a variável para armazenar a cor selecionada
cor_selecionada = ""

# Criar campos de entrada
label_compromisso = tk.Label(root, text="Compromisso:")
label_compromisso.grid(row=0, column=0, padx=10, pady=10)
entrada_compromisso = tk.Entry(root, width=40)
entrada_compromisso.grid(row=0, column=1, padx=10, pady=10)

label_descricao = tk.Label(root, text="Descrição:")
label_descricao.grid(row=1, column=0, padx=10, pady=10)
entrada_descricao = tk.Entry(root, width=40)
entrada_descricao.grid(row=1, column=1, padx=10, pady=10)

# Criar o calendário
label_calendario = tk.Label(root, text="Escolha a data:")
label_calendario.grid(row=2, column=0, padx=10, pady=10)
calendario = Calendar(root, selectmode='day', date_pattern='dd/mm/yyyy')
calendario.grid(row=2, column=1, padx=10, pady=10)

# Botão para escolher a cor do compromisso
cor_button = tk.Button(root, text="Escolher cor", command=escolher_cor)
cor_button.grid(row=3, column=0, padx=10, pady=10)

# Criar a lista de compromissos
lista_compromissos = tk.Listbox(root, width=50, height=10)
lista_compromissos.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Criar os botões
botao_salvar = tk.Button(root, text="Salvar", command=salvar_compromisso)
botao_salvar.grid(row=5, column=0, padx=10, pady=10)

botao_remover = tk.Button(root, text="Remover", command=remover_compromisso)
botao_remover.grid(row=5, column=1, padx=10, pady=10)

# Iniciar a interface gráfica
root.mainloop()