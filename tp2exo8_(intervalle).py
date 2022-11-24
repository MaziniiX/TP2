while True:
    x=float(input("Veuillez saisir un nombre réel :"))
    if 0 < x < 3 or -2 < x < -10 or x == -2 or x == -10:
        print("x appartient à I")
    else:
     print("x n'appartient pas à I")