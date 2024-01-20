Auswahl = int(input("Bitte geben Sie ihr gewünschtes Rezept an:"
                    "1:Pfannkuchen, 2: Käsekuchen 3: Waffeln"))
portions = int(input("Geben sie die Anzahl der Portionen ein."))

if Auswahl == 1:
    if portions == 1:
        for x in [str(portions * 1) + " Ei", str(portions * 200) + " ml Milch", str(portions * 300) + " g Mehl."]:
            print(x)

    elif portions >1:
        for z in [str(portions * 1) + " Eier", str(portions * 200) + " ml Milch", str(portions * 300) + " g Mehl."]:
            print(z)



elif Auswahl == 2:
    if portions == 1:
        for b in [str(portions * 150) + " g Mehl", str(portions * 60) + " g Zucker",
                  str(portions * 1) + " Pck. Vanilinzucker", str(portions * 1) + " Prise Salz",
                  str(portions * 100) + " g weiche Butter"]:
            print(b)
    elif portions >1:
        for c in [str(portions * 150) + " g Mehl", str(portions * 60) + " g Zucker",
                  str(portions * 1) + " Pck. Vanilinzucker", str(portions * 1) + " Prisen Salz",
                  str(portions * 100) + " g weiche Butter"]:
             print(c)

elif Auswahl == 3:
    if portions == 1:
        for u in [str(portions * 125) + " g weiche Butter", str(portions * 100) + " g Zucker",
                  str(portions * 1) + " Pck. Vanillezucker", "1 Ei", str(portions * 250) + " g Mehl",
                  "1 Prise Salz", str(portions * 1) + " TL Backpulver", str(portions * 200) + " ml Milch" ]:
            print(u)
    elif portions >1:
        for i in [str(portions * 125) + " g weiche Butter", str(portions * 100) + " g Zucker",
                  str(portions * 1) + " Pck. Vanillezucker", str(portions * 1) + " Eier", str(portions * 250) + " g Mehl",
                  str(portions * 1) + " Prisen Salz", str(portions * 1) + " TL Backpulver", str(portions * 200) + " ml Milch" ]:
            print(i)




input(" Drücken Sie eine beliebige Taste, um das Programm zu schließen.")