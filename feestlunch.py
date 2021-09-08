#prijzen van producten
prijscroissant = 0.39
prijsstokbrood = 2.78
waardekorting  = 0.50

#hoeveelheid producten
aantcroissant = 17
aantstokbrood = 2
aantkorting   = 3

# print(aantcroissant * prijscroissant + aantstokbrood * prijsstokbrood - aantkorting * waardekorting)
prijs = aantcroissant * prijscroissant + aantstokbrood * prijsstokbrood - aantkorting * waardekorting

print("De feestlunch kost je bij de bakker " + str(prijs) + " euro voor de " + str(aantcroissant) + " croissantjes en de " + str(aantstokbrood) + " stokbroden als de " + str(aantkorting) + " kortingsbonnen nog geldig zijn!")