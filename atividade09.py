# Solicita ao usuário que insira uma nota
nota = float(input("Digite a nota (entre 0 e 10): "))

# Verifica a classificação da nota
if nota >= 7:
    print("Aprovado.")
elif 5 <= nota < 7:
    print("Recuperação.")
else:
    print("Reprovado.")
