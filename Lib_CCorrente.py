import os
from datetime import date, datetime
saldo_cc = 0.0
extratocc = ""

def deposito(valor):
        global saldo_cc, extratocc
        saldo_cc += valor
        extratocc += f"-▷ Depósito efetuado no valor de R${valor:.2f}\n"
        print(f"▷ Depósito de R${valor:.2f} realizado com sucesso.")

def saque(valor):
        global saldo_cc, extratocc
        if valor <= saldo_cc:
            saldo_cc -= valor
            extratocc += f"- ▷ Saque efetuado no valor de R${valor:.2f}\n"
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("▷ Saldo insuficiente para realizar o saque.")

def extrato():
        global extratocc
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"▷ Extrato da conta corrente em {data_atual}:")
        print(extratocc if extratocc else "▷Nenhuma operação realizada.")

def saldo():
        global saldo_cc
        print(f"▷Saldo atual da conta corrente: R${saldo_cc:.2f}")

        
def finaizar_app():
        os.system("cls")
        print("""
    ███████╗██╗███╗░░░███╗  ██████╗░░█████╗░
    ██╔════╝██║████╗░████║  ██╔══██╗██╔══██╗
    █████╗░░██║██╔████╔██║  ██║░░██║██║░░██║
    ██╔══╝░░██║██║╚██╔╝██║  ██║░░██║██║░░██║
    ██║░░░░░██║██║░╚═╝░██║  ██████╔╝╚█████╔╝
    ╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░░╚════╝░

    ██████╗░██████╗░░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║██╔══██╗██║
    ██████╔╝██████╔╝██║░░██║██║░░██╗░██████╔╝███████║██╔████╔██║███████║██║
    ██╔═══╝░██╔══██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║╚═╝
    ██║░░░░░██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░░██║██╗
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝\n""")
        
