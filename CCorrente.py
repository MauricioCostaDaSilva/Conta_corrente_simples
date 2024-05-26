
from Lib_CCorrente import deposito, saque, extrato, saldo, finaizar_app

print("""\n >>>𝗚𝗘𝗦𝗧𝗔̃𝗢 𝗗𝗘 𝗖𝗢𝗡𝗧𝗔 𝗖𝗢𝗥𝗥𝗘𝗡𝗧𝗘<<<\n ＊＊＊＊＊＊＊＊＊＊＊＊＊＊""")

def main():
        while True:
            
            print("  𝟏. DEPOSITO")
            print("  𝟐. SAQUE")
            print("  𝟑. EXTRATO")
            print("  𝟒. SALDO ")
            print("  𝟓. SAIR")
            print("＊＊＊＊＊＊＊＊＊＊＊＊＊＊")

            opcao = input("DIGITE: ")

            if opcao == '1':
                valor = float(input("DIGITE O VALOR: "))
                deposito(valor)
            elif opcao == '2':
                valor = float(input("DIGETE O VALOR: "))
                saque(valor)
            elif opcao == '3':
                extrato()
            elif opcao == '4':
                saldo()
            elif opcao == '5':
                finaizar_app()

                break
            else:
                print("""𝐎𝐏𝐂̧𝐀̃𝐎 𝐈𝐍𝐕𝐀𝐋𝐈𝐃𝐀. \n 𝐓𝐄𝐍𝐓𝐄 𝐌𝐀𝐈𝐒 𝐔𝐌𝐀 𝐕𝐄𝐙.""")


if __name__ == "__main__":
    main()
