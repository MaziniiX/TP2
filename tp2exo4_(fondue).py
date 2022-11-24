BASE=4
fromage=800.0
eau=2
ail=2
pain=400
nbConvives=int(input("Veuillez saisir le nombre de convives :"))
nouvelleQuantiteFromage=fromage*nbConvives/BASE
nouvelleQuantiteEau=eau*nbConvives/BASE
nouvelleQuantiteAil=ail*nbConvives/BASE
nouvelleQuantitePain=pain*nbConvives/BASE
print("Pour faire une fondue fribourgeoise pour", nbConvives ,"personnes, il vous faut :")
print("- ",nouvelleQuantiteFromage,"gr de fromage")
print("- ",nouvelleQuantiteEau,"dl d'eau")
print("- ",nouvelleQuantiteAil,"gousse(s) d'ail")
print("- ",nouvelleQuantitePain,"gr de pain")

