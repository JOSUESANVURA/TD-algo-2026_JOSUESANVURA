note = float(input("Entrez une note sur 100 : "))

if note >= 90:
    mention = "Excellent"
elif note >= 75:
    mention = "Très Bien"
elif note >= 60:
    mention = "Bien"
elif note >= 50:
    mention = "Passable"
else:
    mention = "Insuffisant"

print(f"Mention : {mention}")