import random
import time

NocheineRunde = True
PSS = ["Papier", "Stein", "Schere"]

def check():
    RandomPSS = random.choice(PSS)
    print(RandomPSS)
    if RandomPSS == "Papier" and Antwort.lower() == "schere":
        time.sleep(1)
        print(RandomPSS)
        print("Du hast gewonnen")
    elif RandomPSS == "Papier" and Antwort.lower() == "stein":
        time.sleep(1)
        print(RandomPSS)
        print("Du hast verloren")
    elif RandomPSS == "Papier" and Antwort.lower() == "papier":
        time.sleep(1)
        print(RandomPSS)
        print("Unentschieden")
    elif RandomPSS == "Stein" and Antwort.lower() == "schere":
        time.sleep(1)
        print(RandomPSS)
        print("Du hast verloren")
    elif RandomPSS == "Stein" and Antwort.lower() == "papier":
        time.sleep(1)
        print(RandomPSS)
        print("Du hast gewonnen")
    elif RandomPSS == "Stein" and Antwort.lower() == "stein":
        time.sleep(1)
        print(RandomPSS)
        print("Unentschieden")
    elif RandomPSS == "Schere" and Antwort.lower() == "schere":
        time.sleep(1)
        print(RandomPSS)
        print("Unentschieden")
    elif RandomPSS == "Schere" and Antwort.lower() == "stein":
        time.sleep(1)
        print(RandomPSS)
        print("Du hast gewonnen")
    elif RandomPSS == "Schere" and Antwort.lower() == "papier":
        time.sleep(1)
        print(RandomPSS)
        print("Du hast verloren")
    elif Antwort.lower() != "Schere" or Antwort.lower() != "Papier" or Antwort.lower() != "Stein":
        time.sleep(1)
        print("Bitte gib Schere, Stein oder Papier ein.")



def NeueRunde():
    Verlassen = True
    global NocheineRunde

    while Verlassen:
        Antwort2 = input("Willst du noch eine Runde Spielen? (ja/nein)")
        if Antwort2.lower() == "ja":
            time.sleep(1)
            print("Toll")
            Verlassen = False
        elif Antwort2.lower() == "nein":
            time.sleep(1)
            print("Schade")
            time.sleep(1)
            Verlassen = False
            NocheineRunde = False

        else:
            time.sleep(1)
            print("Bitte gib ja oder nein ein!")
            Verlassen = True






while NocheineRunde:
    Antwort = input("Nimm bitte Schere, Stein oder Papier!")
    check()
    NeueRunde()
