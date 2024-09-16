# Solicita ao usuário que insira uma letra
letra = input("Digite uma letra: ").lower()

# Verifica se a letra é uma vogal ou consoante
if letra in 'aeiou':
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")
