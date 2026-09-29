valor = float(input("Valor: "))
cup = input("Tem cupom? s/n :")

if cup == "s" or "S":
    fret = True
    valor = valor * 0.20

if valor > 300:
    fret = True

if fret == False:
    if valor > 100 and < 300: