import pyautogui as py
import random



py.hotkey('alt', 'tab')
py.click(330, 466)
py.click(940,980)
bomDia = ["bom diaa amor", "bom dia neném", "bom dia vidaa"]
mensagem = random.choice(bomDia)
py.hotkey('ctrl', 'c')
py.write(mensagem)
py.hotkey('ctrl', 'v')
py.click(1859, 982)

