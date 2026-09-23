beginstand = float(input())
eindstand = float(input())
liters = float(input())

gereden_kilometers = eindstand - beginstand
verbruik = (liters / gereden_kilometers) * 100

print(verbruik)
