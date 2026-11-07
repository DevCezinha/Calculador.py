def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("DIGITE APENAS NÚMEROS")


print("---------- ESCOLHA UMA OPÇÃO DE 1 A 4 ----------")
print("[1] + Adição")
print("[2] - Subtração")
print("[3] x Multiplicação")
print("[4] / Divisão")

opcao = input("Digite a opção: ")

if opcao not in ("1", "2", "3", "4"):
    print("Opção inválida")
else:
    numero_1 = ler_numero("Digite um número: ")
    numero_2 = ler_numero("Digite outro número: ")

    if opcao == "1":
        print(numero_1 + numero_2)
    elif opcao == "2":
        print(numero_1 - numero_2)
    elif opcao == "3":
        print(numero_1 * numero_2)
    elif opcao == "4":
        if numero_2 == 0:
            print("Não é possível dividir por zero")
        else:
            print(numero_1 / numero_2)