dico_notes = {"Ali": 12, "Sara": 18, "Zineb": 14, "Youssef": 9}
dico_trie = dict(sorted(dico_notes.items(), key=lambda item: item[1]))

print("Dictionnaire trié par valeurs :", dico_trie)
