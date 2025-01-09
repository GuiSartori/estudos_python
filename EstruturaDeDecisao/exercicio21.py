saque = 127
notas = [100, 50, 10, 5, 1]
quantidades = {}

for nota in notas:
    quantidades[nota] = saque // nota
    saque %= nota

for nota, quantidade in quantidades.items():
    if quantidade > 0:
        print(f"{quantidade} notas de R${nota},00")

print(quantidades)