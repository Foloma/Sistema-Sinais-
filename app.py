import tkinter as tk
from tkinter import messagebox
import random

# Configurações iniciais
wins = 0
losses = 0
perdas_seguidas = 0
aposta = 1.0
taxa = 0.0

# Função para gerar sinal
def gerar_sinal():
    global sinal, digito_mercado, sinal_forte
    digito_mercado = random.randint(0, 9)
    sinal = "PAR" if digito_mercado % 2 == 0 else "IMPAR"
    # Sinal forte aleatório 50% chance
    sinal_forte = random.choice([True, False])
    texto_sinal.set(f"SINAL: {sinal} {'(FORTE)' if sinal_forte else '(FRACO)'} | Dígito do mercado: {digito_mercado}")

# Função quando o usuário clica
def entrar(entrada):
    global wins, losses, perdas_seguidas, aposta, taxa
    resultado = "WIN" if entrada == sinal else "LOSS"
    
    # Atualiza estatísticas
    if resultado == "WIN":
        wins += 1
        perdas_seguidas = 0
        aposta = 1.0  # reset aposta
    else:
        losses += 1
        perdas_seguidas += 1
        aposta *= 1.5  # martingale
    
    taxa = (wins / (wins + losses)) * 100 if (wins + losses) > 0 else 0
    
    # Atualiza histórico
    historico_texto.set(
        f"{historico_texto.get()}\nSINAL: {sinal} | Entrada: {entrada} | Resultado: {resultado} | Aposta: {aposta:.2f}\n"
    )
    
    # Atualiza status
    status_texto.set(f"Wins: {wins} | Losses: {losses} | Taxa: {taxa:.2f}% | Perdas seguidas: {perdas_seguidas}")
    
    # Se houver muitas perdas consecutivas
    if perdas_seguidas >= 3:
        messagebox.showwarning("Alerta", "Sistema parado: Muitas perdas consecutivas!")
        root.quit()
    
    # Gera próximo sinal automaticamente
    gerar_sinal()

# Configura janela principal
root = tk.Tk()
root.title("Sistema de Sinais Profissional")
root.geometry("600x500")
root.configure(bg="#1e1e2f")

# Texto do sinal
texto_sinal = tk.StringVar()
texto_sinal.set("Clique em 'Gerar Sinal' para iniciar")
label_sinal = tk.Label(root, textvariable=texto_sinal, font=("Arial", 16, "bold"), fg="#00ff00", bg="#1e1e2f")
label_sinal.pack(pady=20)

# Botões de entrada
frame_botoes = tk.Frame(root, bg="#1e1e2f")
frame_botoes.pack(pady=10)

btn_par = tk.Button(frame_botoes, text="PAR", width=10, height=2, bg="#007acc", fg="white", command=lambda: entrar("PAR"))
btn_par.grid(row=0, column=0, padx=10)

btn_impar = tk.Button(frame_botoes, text="IMPAR", width=10, height=2, bg="#e91e63", fg="white", command=lambda: entrar("IMPAR"))
btn_impar.grid(row=0, column=1, padx=10)

# Botão gerar sinal manual (opcional)
btn_gerar = tk.Button(root, text="Gerar Sinal", width=15, height=2, bg="#ff9800", fg="white", command=gerar_sinal)
btn_gerar.pack(pady=10)

# Status do sistema
status_texto = tk.StringVar()
status_texto.set(f"Wins: {wins} | Losses: {losses} | Taxa: {taxa:.2f}% | Perdas seguidas: {perdas_seguidas}")
label_status = tk.Label(root, textvariable=status_texto, font=("Arial", 12), fg="#ffffff", bg="#1e1e2f")
label_status.pack(pady=10)

# Histórico de operações
historico_texto = tk.StringVar()
historico_texto.set("Histórico de operações:")
label_historico = tk.Label(root, textvariable=historico_texto, font=("Arial", 10), fg="#cccccc", bg="#1e1e2f", justify="left")
label_historico.pack(pady=10)

# Inicia o primeiro sinal automaticamente
gerar_sinal()

# Executa a janela
root.mainloop()
