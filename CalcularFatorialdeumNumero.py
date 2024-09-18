# Recebe o número do usuário
numero = int(input("Digite um número: "))

# Inicializa o fatorial
fatorial = 1

# Calcula o fatorial
for i in range(1, numero + 1):
    fatorial *= i

# Imprime o resultado
print(f"O fatorial de {numero} é: {fatorial}")
