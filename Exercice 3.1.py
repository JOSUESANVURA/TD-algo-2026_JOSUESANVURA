# Vos informations
age = 24
pays = "congo"

print(f"Âge : {age} ans")
print(f"Pays : {pays}")

if age >= 18 and (pays == "congo" or pays == "cameroun"):
    print("✅ Inscription autorisée.")
elif age < 18:
    print("❌ Vous êtes trop jeune pour vous inscrire.")
else:
    print("❌ Désolé, programme réservé aux ressortissants du Congo ou Cameroun.")