entree = input("Entrez une liste de mots séparés par des espaces : ")
mots = entree.split()
voyelles = "aeiouyAEIOUY"
total_voyelles = 0

for mot in mots:
    for char in mot:
        if char in voyelles:
            total_voyelles += 1

print(f"Nombre total de voyelles : {total_voyelles}")