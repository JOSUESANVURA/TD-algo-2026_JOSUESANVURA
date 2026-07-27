age = 24
statut = "étudiant"

print(f"Âge : {age} ans")
print(f"Statut : {statut}")

if age < 18:
    tarif = 5
else:
    if 18 <= age <= 25:
        if statut == "étudiant":
            tarif = 6
        elif statut == "salarié":
            tarif = 8
        else:
            tarif = 10
    else:
        if statut == "retraité":
            tarif = 7
        else:
            tarif = 10

print(f"Votre tarif est de {tarif} €.")