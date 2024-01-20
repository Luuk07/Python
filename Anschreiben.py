import random
Dein_Name = input("Bitte geben Sie Ihren Namen ein.")
Frage = ("Ist Ihr Ansprechpartner männlich? (ja/nein)")
Name = input("Bitte geben Sie den vollen Namen Ihres Ansprechpartners ein.")
NU = input("Bitte geben Sie den Namen des Unternehemens ein.")
Straße = input("Bitte geben Sie die Straße des Unternehmens an.")
HNummer= input("Bitte geben Sie die Hausnummer des Unternehmens an.")
Pl= input("Bitte geben Sie die Postleitzal vom Unternehem an")
St = input("Bitte geben Sie die Stadt an, wo das Unternehmen liegt")
Art= input("Bitte geben Sie an, als was Sie sich bewerben wollen.")
Dt = input("Bitte geben Sie das Datum an, ab wann sie die Stelle haben wollen (in Zahlen).")
HD = input("Bitte geben Sie das heutige Datum in Zahlen an")
Heutiges_Datum = HD
Frage = ("Ist der Ansprechpartner männlich? (ja/nein)")
antwort = input(Frage)


List_1 = [Name, NU, f"{Straße} {HNummer}", f"{Pl} {St}"]

print()
for D in List_1:
    print(D)


print("{:>50}".format(Heutiges_Datum))
print()
print("Hiermit Bewerbe ich mich, als "  + Art + " ab dem " + Dt + ".")
print()



if antwort.lower() == "ja":
    print("Sehr geehrter Herr " +(Name)+ ","  )
elif antwort.lower() == "nein":
    print("Sehr geehrte Frau "+(Name)+ "," )
else:
    print("Error")



AS1 =("ich bewerbe mich mit großem Interesse um eine Position, als " +(Art)+ "in Ihrem Unternehmen. "
      "Ich bin ich überzeugt, einen wertvollen Beitrag zu Ihrem Team leisten zu können."
      "Ich freue mich darauf, in einem persönlichen Gespräch mehr über die Möglichkeiten zu erfahren und meine Qualifikationen zu erläutern.")
AS2 =("mit großem Interesse bewerbe ich mich initiativ für eine Position, als" +(Art)+ "in Ihrem renommierten Unternehmen. "
      "Ich bin ich überzeugt, einen Mehrwert für Ihr Team zu bieten.")

Anschreiben = random.choice([AS1,AS2])

print(Anschreiben)
print()
print("Liebe Grüße" +Dein_Name)


input("Drücken Sie irgendeine Taste, um das Programm zu schließen")

