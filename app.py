# Automação de Sistemas e Processos com Python

# Desafio:

# Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
# O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a quantidade de produtos compradas e o preço médio dos produtos.


import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 0.5

#passo 0: abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

time.sleep(5)

# passo 1: entrar no sistema da empresa (no link)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(3) #esperando o navegador carregar

# passo 2: fazer login no sistema
pyautogui.click(x=615, y=374)
pyautogui.write("vitorusuario")
time.sleep(2)
pyautogui.click(x=601, y=449)
pyautogui.write("vitorsenha")
pyautogui.click(x=643, y=525)

time.sleep(5)

# passo 3: exportar base de dados
pyautogui.click(x=396, y=363)
pyautogui.click(x=1105, y=184)
pyautogui.click(x=847, y=619)
time.sleep(5)
pyautogui.click(x=1063, y=152)
pyautogui.press("enter")

# passo 4: calcular os indicadores
tabela = pd.read_csv(r"D:\Documentos\Conhecimento\Intensivão de Python - Hashtag\Aula 1\Compras.csv", sep=";")
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto/quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)

# passo 5: enviar o email
#abrindo o site do gmail
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/")
pyautogui.press("enter")
time.sleep(3) #esperando o navegador carregar

#digitando o destinatário
pyautogui.click(x=150, y=203)
pyautogui.write("vitorrocha@alunos.utfpr.edu.br")
pyautogui.press("tab")

#digitando assunto do email
pyautogui.press("tab")
pyperclip.copy("Relatório de encerramento do dia")
pyautogui.hotkey("ctrl", "v")

#digitando o email com os valores solicitados
pyautogui.press("tab")
corpo_do_email = f"""Olá Vitor, espero que esteja bem.

Segue o relatório solicitado:
Total gasto: R${total_gasto:,.2f}
Quantidade: {quantidade}
Preço médio: R${preco_medio:,.2f}

Att,
Equipe Financeiro
"""
pyperclip.copy(corpo_do_email)
pyautogui.hotkey("ctrl", "v")


pyautogui.hotkey("ctrl", "enter")