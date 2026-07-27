mdp = ""

while mdp != "python2025":
    mdp = input("Entrez le mot de passe : ").lower()
    if mdp != "python2025":
        print("Mot de passe incorrect, réessayez.")

print("Mot de passe correct, accès autorisé.")