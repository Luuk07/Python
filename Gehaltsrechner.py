import time

def Nettogehalt(Jahr):
    if Jahr <= 10000:
        return Jahr
    elif Jahr >= 10000 and Jahr <= 16000:
        return Jahr * 0.78
    elif Jahr >= 16000 and Jahr <= 30000:
        return Jahr * 0.70
    elif Jahr >= 30000 and Jahr <= 60000:
        return Jahr * 0.60
    elif Jahr >= 60000:
         return Jahr * 0.5
# Das sind irgendwelche Zahlen, ich kenne die genauen Steuern nicht.

x = input("Gebe Sie Ihren Stundenlohn an")
tag = 8 * float(x)
monat = 20 * tag
Jahr = 12 * monat
Nettomonat = monat * 0.8



Nettogehalt_Jahr = Nettogehalt(Jahr)


print("Ihr Jahresgehalt beträgt " + str(Jahr) + " Euro")
time.sleep(1)
print("Ihr Tageslohn beträgt " + str(tag) + " Euro")
time.sleep(1)
print("Ihr Monatslohn beträgt " + str(monat) + " Euro")
time.sleep(1)
print("Ihr Nettojahreslohn beträgt " + str(Nettogehalt_Jahr) + "Euro")
time.sleep(1)
print("Ihr Nettomonatslohn beträgt " + str(Nettogehalt_Jahr / 12) + "Euro")
time.sleep(1)
print("Ihr Nettotageslohn beträgt " + str(Nettogehalt_Jahr / 240)+ "Euro")
time.sleep(1)
print("Ihr Nettostundenlohn beträgt " + str(Nettogehalt_Jahr / (240*8))+ "Euro")
time.sleep(1)
input("Klicken Sie eine Taste um das Programm zu beenden")
