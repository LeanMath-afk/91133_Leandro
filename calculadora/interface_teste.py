import tkinter as tk
from tkinter import messagebox
import calculadora

def executar_operacao(operacao):
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())

        if operacao == 'somar':
            resultado = calculadora.somar(a, b)
        elif operacao == 'subtrair':
            resultado = calculadora.subtrair(a, b)
        elif operacao == 'multiplicar':
            resultado = calculadora.multiplicar(a, b)
        elif operacao == 'dividir':
            resultado = calculadora.dividir(a, b)
        else:
            resultado = "Operação inválida"

        label_resultado.config(text=f"Resultado: {resultado}")

    except ValueError as ve:
        messagebox.showerror("Erro", str(ve))
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def resetar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

# Criar janela
janela = tk.Tk()
janela.title("Calculadora Bonita")
janela.geometry("400x380")
janela.configure(bg="#f0f0f0")  # Cor de fundo

# Estilo
fonte_padrao = ("Helvetica", 12)
cor_botao = "#4CAF50"
cor_botao_texto = "white"

# Título
tk.Label(janela, text="Calculadora", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Frame para inputs
frame_inputs = tk.Frame(janela, bg="#f0f0f0")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Valor 1:", font=fonte_padrao, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada1 = tk.Entry(frame_inputs, font=fonte_padrao, width=15)
entrada1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Valor 2:", font=fonte_padrao, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entrada2 = tk.Entry(frame_inputs, font=fonte_padrao, width=15)
entrada2.grid(row=1, column=1, padx=10, pady=5)

# Frame para botões de operação
frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.pack(pady=10)

estilo_botao = {
    "font": fonte_padrao,
    "bg": cor_botao,
    "fg": cor_botao_texto,
    "width": 15,
    "relief": "raised",
    "bd": 2
}

tk.Button(frame_botoes, text="Somar", command=lambda: executar_operacao('somar'), **estilo_botao).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botoes, text="Subtrair", command=lambda: executar_operacao('subtrair'), **estilo_botao).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botoes, text="Multiplicar", command=lambda: executar_operacao('multiplicar'), **estilo_botao).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botoes, text="Dividir", command=lambda: executar_operacao('dividir'), **estilo_botao).grid(row=1, column=1, padx=5, pady=5)

# Botão de Reset
tk.Button(janela, text="Resetar", command=resetar, bg="#f44336", fg="white", font=fonte_padrao, width=20, relief="raised", bd=2).pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="Resultado: ", font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
label_resultado.pack(pady=20)

# Iniciar loop
janela.mainloop()
