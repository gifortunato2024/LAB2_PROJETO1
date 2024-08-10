import random

def cumprimento(texto):
    return f"Olá, {texto}"

print(cumprimento("Giovanna Fortunato Pinto Santos"))

def calcula_media_aleatoria():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    media = (num1 + num2 + num3) / 3
    return media

print("Média de três números aleatórios:", calcula_media_aleatoria())
