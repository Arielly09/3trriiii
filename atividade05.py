# Solicita ao usuário que insira dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica qual número é maior
if numero1 > numero2:
    print(f"O número {numero1} é maior.")
elif numero1 < numero2:
    print(f"O número {numero2} é maior.")
else:
    print("Os dois números são iguais.")
