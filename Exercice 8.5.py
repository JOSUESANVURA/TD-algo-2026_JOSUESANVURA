texte = input("Entrez un texte : ")
voyelles = "aeiouyAEIOUY"

print("Consonnes :")
for char in texte:
    if char.isalpha() and char not in voyelles:
        print(char, end=" ")