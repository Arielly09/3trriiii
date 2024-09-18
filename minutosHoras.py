# Recebe a quantidade de minutos do usuário
minutos = int(input("Digite a quantidade de minutos: "))

# Calcula horas e minutos
horas = minutos // 60
minutos_restantes = minutos % 60

# Imprime o resultado
print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")
