from pynput import keyboard
from datetime import datetime
#Receber um número base para o contador

qtd = 0
func_atualizar_janela = None
programa_encerrado = False

def salvar():
    """Salva o total de resets em um arquivo de texto"""
    global qtd
    data_agora = datetime.now()
    data_formatada = data_agora.strftime("%d/%m/%Y - %H:%M")

    with open("memoria.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{data_formatada} -> {qtd} vezes\n")

def ativado_r():
    """Executa a cada CTRL + R"""
    global qtd
    qtd += 4
    if func_atualizar_janela:
        func_atualizar_janela(qtd)

def encerrar():
    """Encerra o loop de escuta do teclado e já salva"""
    global programa_encerrado
    salvar()
    programa_encerrado = True
    raise keyboard.Listener.StopException

def iniciar_escuta(callback_da_interface, callback_de_encerrar=None, valor_inicial=0):
    global func_atualizar_janela, func_fechar_janela, qtd
    func_atualizar_janela = callback_da_interface
    programa_encerrado = False

    qtd = valor_inicial

    atalhos = keyboard.GlobalHotKeys({
        '<ctrl>+q' : encerrar, '<ctrl>+r' : ativado_r
    })

    atalhos.start()




