# Define a senha correta
senha_correta = "senha123"

# Solicita ao usuário que insira a senha
senha_inserida = input("Digite a senha: ")

# Verifica se a senha inserida está correta
if senha_inserida == senha_correta:
    print("Senha correta.")
else:
    print("Senha incorreta.")

