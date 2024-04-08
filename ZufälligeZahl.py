import random
import time

Falscheantwort = True
KoZ = ["Kopf", "Zahl"]
Zahlenliste1 = list(range(1, 11))
Zahlenliste2 = list(range(1, 7))





def check():
    Random_KoZ = random.choice(KoZ)
    Random_Zl1 = random.choice(Zahlenliste1)
    Random_Zl2 = random.choice(Zahlenliste2)
    if Antwort == "1":
            time.sleep(0.5)
            print(Random_KoZ)

    elif Antwort == "2":
            time.sleep(0.5)
            print(Random_Zl1)



    elif Antwort == "3":
            time.sleep(0.5)
            print(Random_Zl2)

    else:
            print("Bitte gib eine Zahl zwischen 1 und 3 ein ")








while True:
    Antwort = (input("Drücke 1 für Kopf oder Zahl \n"
                     "Drücke 2 für die Zahlenliste von 1-10 \n"
                     "Drücke 3 für die zahlenliste von 1-6 "))

    check()
    time.sleep(2)






