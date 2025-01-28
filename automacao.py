# palavra chave da segunda aula: automação

import pandas as pd
import pyautogui
import time
import os

# Definir variável DISPLAY para evitar erro de conexão
os.environ["DISPLAY"] = ":0"

# Conceder permissão ao usuário para acessar o servidor X
os.system("xhost +SI:localuser:$USER")

# Iniciando a automação
pyautogui.PAUSE = 0.5

# Abrir o navegador (Firefox)
os.system("firefox &")  # Executa o Firefox em segundo plano

time.sleep(5)  # Tempo maior para garantir que o navegador esteja carregado

# Garantir que o Firefox está em primeiro plano
os.system("xdotool search --sync --onlyvisible --class Firefox windowactivate")
time.sleep(1)

# Alternar para o Firefox manualmente se necessário
time.sleep(1)
pyautogui.hotkey("alt", "tab")
time.sleep(1)

# Entrar no link
time.sleep(2)
pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
time.sleep(5)

# Fazer login
pyautogui.click(x=1213, y=441)  # Ajustar coordenadas conforme necessário
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")
pyautogui.click(x=888, y=543)  # Ajustar coordenadas conforme necessário

time.sleep(5)

# Importar a base de alunos para cadastrar
tabela = pd.read_csv("alunos.csv")

# Cadastrar um aluno
for linha in tabela.index:
    pyautogui.click(x=839, y=385)  # Ajustar coordenadas conforme necessário
    pyautogui.write(str(tabela.loc[linha, "Nome"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "Email"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "Endereco"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "Telefone"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  # Enviar o formulário
    pyautogui.scroll(5000)  # Dar scroll para cima
