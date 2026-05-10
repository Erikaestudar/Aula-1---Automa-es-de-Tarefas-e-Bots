# Bibliotecas = pacotes de código
# pip install pyautogui


import pyautogui
import time
import pyperclip

# COMANDOS - Cheat Sheet
# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla 
# pyautogui.hotkey -> aperta um atalho (hotkey)
# pyautogui.scroll -> scroll do mouse

# pyautogui.hotkey("command", "space") no MAC
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# PASSO A PASSO DO SEU PROGRAMA
# Passo 1: Entrar no sistema da empresa 
# Abriria o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

# Copiar o link para a área de transferência e colar
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3)


# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos