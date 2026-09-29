servicos = ["Alugar", "Comprar", "Reservar", "Atrasados"]

for servico in servicos:
    print(servico)


for i, servico_nu in enumerate(servicos, start=1):
    print(i, servico_nu)


comanda = [22.50, 54.35, 64.30, 48.84, 62.77]
preco = 0

for valor in comanda:
    preco += valor

print(f"O preço total é {preco}")


livros = {"Roberto, o verdadeiro judas": 65.35, "the little princeso": 94.35, "João e o pé de arroz": 762.32, "Estevão gulosso": 57.99}
preco1 = 0

while preco1 >= 200:
    preco1 += 