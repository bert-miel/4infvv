taakjes = int(input("Hoeveel taakjes heb je gedaan? "))
niet_afgeruimd = int(input("Hoeveel keer heb je de tafel niet afgeruimd? "))

zakgeld = 5
zakgeld = zakgeld + taakjes * 2
zakgeld = zakgeld - niet_afgeruimd

print("Lio krijgt", zakgeld, "euro zakgeld deze week")