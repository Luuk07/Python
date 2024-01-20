import random
import sys
import time

Falsche_Antwort = True
Zahlen_Liste = list(range(1, 101))
Zufällige_Zahl = random.choice(Zahlen_Liste)
Spieler = int(input("Bitte geben Sie eine Zahl zwischen 1 und 100 ein"))



def Fehler():
    if Spieler >= 100 or Spieler <= 0:
     print("Bitte wählen Sie eine Zahl zwischen 0 und 100")






def spiel():
   if Spieler == Zufällige_Zahl:
    print("Sie haben gewonnen")
    input("")
    sys.exit()



   else:
    print("")








def Tipps():

    if Spieler >= 100 or Spieler <= 0:
        print("")

    elif Spieler >= Zufällige_Zahl:
        print("Ihre Zahl ist niedriger, als die Ausgewählte Zahl")

    else:
        print("Ihre Zahl ist höher als, die Ausgewählte Zahl ")












while Falsche_Antwort:
   Fehler()
   spiel()
   Tipps()
   time.sleep(0.5)
   Spieler = int(input("Nächster Versuch, bitte geben Sie eine Zahl ein."))
























