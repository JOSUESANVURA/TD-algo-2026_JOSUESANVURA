import random

nombre_secret = random.randint(1, 100)
essai = None
nb_tentatives = 0

while essai != nombre_secret:
    essai = int(input("Devine le nombre (1-100) : "))
    nb_tentatives += 1
    if essai < nombre_secret:
        print("Trop petit.")
    elif essai > nombre_secret:
        print("Trop grand.")
    else:
        print(f"Bravo, tu as trouvé en {nb_tentatives} tentatives !")