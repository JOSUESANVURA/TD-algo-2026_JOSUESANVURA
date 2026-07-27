phrase = "Josue Sanvura Fernandez"
mots = phrase.split()
acronyme = ""

for mot in mots:
    acronyme += mot[0].upper()

print(f"Phrase : {phrase}")
print(f"Acronyme : {acronyme}")