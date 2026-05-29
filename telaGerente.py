import tkinter as tk
from tkinter import ttk


def enviar_dados():
    titular = entry_titular.get().strip()
    agencia = entry_agencia.get().strip()
    cpf = entry_cpf.get().strip()

    if not titular or not agencia or not cpf:
        label_resposta.config(
            text="❌ Preencha todos os campos!", 
            foreground="red"
        )
    else:
        resposta = f"✅ Dados enviados com sucesso!\n\n" \
                   f"Titular: {titular}\n" \
                   f"Agência: {agencia}\n" \
                   f"CPF: {cpf}"
        
        label_resposta.config(
            text=resposta, 
            foreground="green"
        )


# ==================== Janela Principal ====================
janela = tk.Tk()
janela.title("Cadastro de Conta")
janela.geometry("400x350")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Cadastro de Conta", font=("Arial", 16, "bold"))
titulo.pack(pady=15)

# Frame para os campos
frame = tk.Frame(janela)
frame.pack(pady=10, padx=30, fill="x")

# Titular
tk.Label(frame, text="Titular:", font=("Arial", 10)).pack(anchor="w")
entry_titular = tk.Entry(frame, font=("Arial", 11), width=40)
entry_titular.pack(pady=5, fill="x")

# Agência
tk.Label(frame, text="Agência:", font=("Arial", 10)).pack(anchor="w")
entry_agencia = tk.Entry(frame, font=("Arial", 11), width=40)
entry_agencia.pack(pady=5, fill="x")

# CPF
tk.Label(frame, text="CPF:", font=("Arial", 10)).pack(anchor="w")
entry_cpf = tk.Entry(frame, font=("Arial", 11), width=40)
entry_cpf.pack(pady=5, fill="x")

# Botão Enviar
btn_enviar = ttk.Button(janela, text="ENVIAR", command=enviar_dados)
btn_enviar.pack(pady=20)

# Label de Resposta
label_resposta = tk.Label(
    janela, 
    text="", 
    font=("Arial", 10), 
    justify="center", 
    wraplength=350
)
label_resposta.pack(pady=10)

# Rodapé
rodape = tk.Label(janela, text="© 2026 - Sistema Simples", font=("Arial", 8), fg="gray")
rodape.pack(side="bottom", pady=10)

janela.mainloop()