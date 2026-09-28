import tkinter as tk
import contador


def atualizar_tela(novo_valor):
    """Esta é a função de CALLBACK que passamos para o contador"""
    janela.after(0, lambda: label_contador.config(text=str(novo_valor)))

def verificar_encerramento():
    if contador.programa_encerrado:
        janela.quit()
        janela.destroy()
    else:
        janela.after(100, verificar_encerramento)
0
janela = tk.Tk()
janela.configure(bg="#1e1e1e")
janela.title("Contador de Reset")
janela.geometry("350x200")

label_contador = tk.Label(
    janela, 
    text="0", 
    font=("Arial", 40, "bold"),
    bg="#1e1e1e",
    fg="white"
    )
label_contador.pack(expand=True)
contador.iniciar_escuta(callback_da_interface=atualizar_tela, valor_inicial=0)

verificar_encerramento()

janela.mainloop()