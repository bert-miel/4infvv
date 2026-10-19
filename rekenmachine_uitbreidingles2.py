getal1 = float(input("Geef getal1: "))
getal2 = float(input("Geef getal2: "))
bewerking = input("welke bewerking wil je uitvoeren? (+,-,/,*,m):")

if bewerking == "+": #== : is gelijk aan ; <= : kleiner dan en gelijk aan ; < : kleiner dan; != : Niet gelijk aan
    print(f"De som van {getal1} + {getal2} ={getal1+getal2}.")

if bewerking == "-": 
    print(f"De som van {getal1} - {getal2} ={getal1-getal2}.")

if bewerking == "/": 
    print(f"De som van {getal1} / {getal2} ={getal1/getal2}.")

if bewerking == "*": 
    print(f"De som van {getal1} . {getal2} ={getal1*getal2}.")

if bewerking == "m": 
    print(f"De som van {getal1} tot de {getal2}e macht ={getal1 ** getal2}.")