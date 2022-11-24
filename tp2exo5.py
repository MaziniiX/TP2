nombre = float(input("Entrez un nombre entier :"))

pair=0
impair=0
positif=0
negatif=0

if nombre>0:
    positif=1
elif nombre<0:
    negatif=1

if nombre%2==0:
    pair=1
else:
    impair=1

if ((positif==1) and (pair==1)):
    print("Le nombre est positif et pair")
elif ((positif == 1) and (impair == 1)):
    print("Le nombre est positif et impair")
elif ((negatif == 1) and (pair == 1)):
    print("Le nombre est négatif et pair")
elif ((negatif == 1) and (impair == 1)):
    print("Le nombre est négatif et impair")
else:
    print("Le nombre est zéro (et il est pair)")





