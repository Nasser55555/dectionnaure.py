First_dict = {
    "Appareil": "Laptop",
    "Marque": "IBM",
    "Carte mère": "MSI Z490",
    "Carte Graphique": "GeForce RTX 3070",
    "RAM": "16G",
    "Processeur": "Intel core i7-G11",
    "SSD": "1 To"
}

First_dict["RAM"] = "32G"

print("Clés :", list(First_dict.keys()))
print("Valeurs :", list(First_dict.values()))
print("Paires clé-valeur :", list(First_dict.items()))

temp = First_dict["Processeur"]
First_dict["Processeur"] = First_dict["Carte Graphique"]
First_dict["Carte Graphique"] = temp

First_dict["Système d’exploitation"] = "Windows 10"


print("Dictionnaire final :", First_dict)
