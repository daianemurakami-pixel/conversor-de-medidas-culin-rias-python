import tkinter as tk
from tkinter import ttk
from fractions import Fraction

# Dicionário de conversões
conversoes = {                  
    "farinha": 120,
    "acucar": 200,
    "chocolate em po": 90,
    "leite em po": 100,
    "manteiga": 227,
    "fubá": 150,
    "amido de milho": 100,
    "liquidos":240
}

# Função de conversão
def converter():
    ingrediente = combo_ingrediente.get().lower()
    entrada = campo_valor.get()
    modo = combo_modo.get()

    if ingrediente not in conversoes:
        resultado.set("Ingrediente não encontrado.")
        return

    try:
        if modo == "Xícaras → Gramas/ML":
            xicaras = float(Fraction(entrada))
            gramas = conversoes[ingrediente] * xicaras
            mls = 240 * xicaras
            resultado.set(f"{xicaras:.2f} xícara(s) = {gramas:.2f} g | {mls:.2f} ml")

        else:  # Gramas → Xícaras/ML
            gramas = float(entrada)
            xicaras = gramas / conversoes[ingrediente]
            mls = xicaras * 240
            resultado.set(f"{gramas} g = {xicaras:.2f} xícara(s) | {mls:.2f} ml")

    except:
        resultado.set("Valor inválido. Tente 1/2, 3/4, 2 1/2...")

# Função para adicionar novos ingredientes
def adicionar_ingrediente():
    janela_add = tk.Toplevel(janela)
    janela_add.title("Adicionar Ingrediente")
    janela_add.geometry("300x200")

    tk.Label(janela_add, text="Nome do ingrediente:").pack()
    nome_entry = tk.Entry(janela_add)
    nome_entry.pack()

    tk.Label(janela_add, text="Gramas por xícara:").pack()
    gramas_entry = tk.Entry(janela_add)
    gramas_entry.pack()

    def salvar():
        nome = nome_entry.get().lower()
        try:
            gramas = float(gramas_entry.get())
        except:
            resultado.set("Valor inválido para gramas.")
            return

        conversoes[nome] = gramas

        # Atualiza o combobox
        combo_ingrediente["values"] = list(conversoes.keys())

        janela_add.destroy()
        resultado.set(f"Ingrediente '{nome}' adicionado com sucesso!")

    tk.Button(janela_add, text="Salvar", command=salvar).pack(pady=10)

# Criar janela principal
janela = tk.Tk()
janela.title("Conversor de Medidas Culinárias")
janela.geometry("400x350")

# Widgets
tk.Label(janela, text="Ingrediente:").pack()
combo_ingrediente = ttk.Combobox(janela, values=list(conversoes.keys()))
combo_ingrediente.pack()

tk.Button(janela, text="Adicionar ingrediente", command=adicionar_ingrediente).pack(pady=5)

tk.Label(janela, text="Modo de conversão:").pack()
combo_modo = ttk.Combobox(janela, values=["Xícaras → Gramas/ML", "Gramas → Xícaras/ML"])
combo_modo.pack()

tk.Label(janela, text="Valor:").pack()
campo_valor = tk.Entry(janela)
campo_valor.pack()

botao = tk.Button(janela, text="Converter", command=converter)
botao.pack(pady=10)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, font=("Arial", 12), wraplength=350).pack()

# Rodar janela
janela.mainloop()
