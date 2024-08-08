"""
- Agendamento de Desligamento PC

-> Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
"""
import os

# 1 - Desligar o computador em 1 hora
def turn_off_one_hour():
    os.system("shutdown /s /t 3600")

# 2 - Desligar o computador em meia hora
def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")
    
def cancel_shutdown():
    os.system("shutdown /a")
    
turn_off_one_hour()
cancel_shutdown()