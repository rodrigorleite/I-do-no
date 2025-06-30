import random
import os
import sys
import time
import webbrowser

def sortear():
    opcao = 6
    numSorteado = random.randint(1, opcao)
    # print("O número sorteado é: ", numSorteado)2

    try:
        escolha = int(input(f"Escolha um Número entre 1 e {opcao}: "))
        if escolha < 1 or escolha > opcao:
            raise ValueError("Número fora de intervalo!: ")
    except ValueError as e:
        print(f"entrada invalida:  {e} Adicione novamente!")
        sortear()
    if escolha == numSorteado:
        print("Tigrinho não soltou a Carta!")
    else:
        print("Tigrinho soltou a Carta!")
        time.sleep(5)
        if sys.platform =="win32":
            os.system("shutdown /s /t 1")
        elif sys.platform == "linux" or sys.platform == "linux2":
            os.system("shutdown now")
        elif sys.platform == "darwin":
            os.system("shutdown now")

sortear()