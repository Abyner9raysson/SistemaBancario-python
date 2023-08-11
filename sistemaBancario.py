Menu = """

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
saques_feito = 0 
extrato = ""
LIMITE_SAQUES = 3


while True:
    
    opcao = input(Menu)

    if opcao == "1":
        valor_dep = float(input("valor do deposito: "))

        if valor_dep > 0:
            saldo += valor_dep
            extrato += f"Deposito de: R$ {valor_dep:.2f}\n"

        else:
            print("falha no deposito, valor para deposito inválido.")

    elif opcao == "2":
        valor_saq = float(input("valor do saque: "))

        execedeu_saldo = valor_saq > saldo

        execedeu_limite = valor_saq > limite

        execedeu_saq = saques_feito >= LIMITE_SAQUES

        if execedeu_saldo:
            print("Falha na operação, sem saldo suficiente!")

        elif execedeu_limite:
            print("Falha na operação, valor do saque execede o limite!")

        elif execedeu_saq:
            print("Falha na operação, valor maximo de saque execedido!")

        elif valor_saq > 0:
            saldo -= valor_saq
            extrato += f"saque: R$ {valor_saq:.2f}\n"
            saques_feito += 1


        else:
            print("falha na operação! valor invalido")
            

    elif opcao == "3":
        print("\n ===========EXTRATO===========")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("=================================")

    elif opcao == "4":  
        break

    else:
        print("Operação invalida!")