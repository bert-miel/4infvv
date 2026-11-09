punten = float(input("Hoeveel punten heb je behaald? "))
totaal = float(input("Op hoeveel punten stond de toets? "))

percentage = punten / totaal * 100

print("Je hebt " + str(percentage))

if percentage >= 50:
    print("Proficiat, je bent geslaagd!")

if percentage < 50:
    print("Jammer, je bent niet geslaagd.")