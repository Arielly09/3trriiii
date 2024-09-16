# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 3 e 5
if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e 5.")
else:
    print("O número não é divisível por 3 e 5.")

