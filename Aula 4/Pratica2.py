livros = {"Roberto, o verdadeiro judas": 65.35, "the little princeso": 94.35, "João e o pé de arroz": 762.32, "Estevão gulosso": 57.99}

def itens_validos(item):
    for item in livros:
        if item in livros:
            livros.append(item)

itens_validos("Roberto, o verdadeiro judas")