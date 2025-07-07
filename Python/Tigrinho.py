import random
import os
import sys
import time
import webbrowser
import tkinter as tk
from tkinter import messagebox

def sortear():
    opcao = 6
    numSorteado = random.randint(1, opcao)
    # print("O número sorteado é: ", numSorteado)2

    # try:
    #     escolha = int(input(f"Escolha um Número entre 1 e {opcao}: "))
    #     if escolha < 1 or escolha > opcao:
    #         raise ValueError("Número fora de intervalo!: ")
    # except ValueError as e:
    #     print(f"entrada invalida:  {e} Adicione novamente!")
    #     sortear()

    def verificarescolha(escolha):
        if escolha == numSorteado:
            print("Tigrinho não soltou a Carta!")
            messagebox.showerror("Perdeu!", "O computador será desligado!")
        
            time.sleep(5)
            if sys.platform =="win32":
                os.system("shutdown /s /t 1")
            elif sys.platform == "linux" or sys.platform == "linux2":
                os.system("shutdown now")
            elif sys.platform == "darwin":
                os.system("shutdown now")
        else:
            print("Tigrinho soltou a Carta!")
            messagebox.showinfo("Olha o Bonus!", "O Tigrinho ta no horario pagante!")
    janela = tk.Toplevel()
    janela.title("Number choise")
    tk.Label(janela, text=("Choise a number in 1 or 6.")).pack(pady=10)

    for i in range(1,6):
         tk.Button(janela, text=str(i), command=lambda i=i: [janela.destroy(), verificarescolha(i)]).pack(pady=10)
# sortear()

def exibirregras():
    regras =(
        "       Rules of Game \n"
        "\n"
        "\n"
        "1 | Choise a nunber in 1 or 6. \n"
        "\n"
        "2 | if you coise a number null your computer is turn off! \n"
        "\n"
        "3 | Caso contrario o jogo continua. \n"
        "\n"
        "                   Good Luck, you need!"
    )
    messagebox.showinfo("Regras", regras)

def sair():
    root.destroy()

root = tk.Tk()
root.title("Fortune Tigger!")
tk.Label(root, text="Welcome to Fortune Tigger", font=("Arial", 20)).pack(pady=15)
tk.Button(root, text="Start Game", width=20, command=sortear).pack(pady=10)
tk.Button(root, text="View Rules", width=20, command=exibirregras).pack(pady=10)
tk.Button(root, text="Exit", width=20, command=sair).pack(pady=10)

root.mainloop()