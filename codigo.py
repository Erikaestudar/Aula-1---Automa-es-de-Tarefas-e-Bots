# Bibliotecas = pacotes de código
# pip install pyautogui


import pyautogui
import time
import pyperclip
import pandas as pd

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
# Clicar no campo de email
login = "pythonimpressionador@gmail.com"
pyperclip.copy(login)
time.sleep(1)
pyautogui.click(x=960, y=540) # coordenadas do campo de email

pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Abrir a base de dados
# pip install pandas openpyxl  - uso de panilhas

# pandas.read_excel(sheet_name="Vendas")  NO EXCEL
table = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
for line in table.index:
    # codigo
    pyautogui.click(x=865, y=394)
    codigo = str(table.loc[line, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(table.loc[line, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(table.loc[line, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(table.loc[line, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco
    preco = str(table.loc[line, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #custo
    custo = str(table.loc[line, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(table.loc[line, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")         

    pyautogui.press("enter")
    # Voltar para o inicio da tela
    pyautogui.scroll(5000)

    # Para parar a automação, mova o mouse para o canto superior 0,0 da tela
    
# Passo 5: Repetir o passo 4 até acabar a lista de produtos