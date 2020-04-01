import scenario

scen = scenario.scenario(10000,24,2)
somme1 = 0
somme2 = 0
for i in range(10000):
    tab = scen.simuler(12,[1,10])
    somme1+=tab[0]
    somme2+=tab[1]
print(somme1/10000)
print(somme2/10000)
