import regression
import scenario
import mdp

import math
import numpy as np

n_periodes =24
n_clients = 10000
n_jours_training = 1000
n_jours_simu = 1
n_plat = 2


liste_prix = []
stock_beg = 50
def fonctionDemandeInitiale(time,price):

    return stock_beg*math.exp(-price)*math.exp(-(time-12)**2/24)

liste_MDP = []
pmin = 1
pmax = 10
k = 10
for i in range(n_plat):

    mdipi = mdp.mdp(n_periodes, stock_beg, fonctionDemandeInitiale, pmin, pmax, k)
    mdipi.remplir_MDP()
    liste_MDP.append(mdipi)
    state = 0
    print("HOP UN DE FAIT")
    #là le MDP est rempli avec toutes les valeurs disponibles


listeDemandesFinal = []  #va nous permettre de faire les régressions etc.
listePrixFinal = []
print("MDP INITIALISES!!")

def z():
    return


def updateNoteMatrix():
    return 0

def remplirListePrix(pe):
    liste = [0 for i in range(n_plat)]
    for i in range(n_plat):
        liste[i] = np.random.randint(1,10,1)[0]
    return liste

#PARTIE SIMULATION DES PREMIERES PERIODES AVEC PRIX AU HASARD
#définir listePRIX
liste_tab_Y = [[] for i in range(n_plat)]
liste_tab_X = [[] for i in range(n_plat)]
listeRevenus = [[] for i in range(n_plat)]
for i in range(n_jours_training):
    state = [50 for i in range(n_plat)]
    scen = scenario.scenario(n_clients, n_periodes, n_plat)
    for pe in range(n_periodes):
        liste_prix = remplirListePrix(pe)
        print(liste_prix)

        listeDemandes = scen.simuler(pe, liste_prix)
        print(listeDemandes)
        for plat in range(n_plat):
            state[plat] -= listeDemandes[plat]
            state[plat] = max(0, state[plat])
            listeRevenus[plat].append(listeDemandes[plat]*liste_prix[plat])

        # rajouter la partie NOTES....
        listePrixFinal.append([pe]+liste_prix)

        # revoir cette ligne
        listeDemandesFinal.append(listeDemandes)
        liste_prix = remplirListePrix(pe)
        # problème, PRENDRE EN COMPTE LE TEMPS

for i in range(len(listePrixFinal)):

    for plat in range(n_plat):
        liste_tab_X[plat].append([listePrixFinal[i][0],listePrixFinal[i][plat+1]])

for i in range(len(listeDemandesFinal)):
    for plat in range(n_plat):
        liste_tab_Y[plat].append(listeDemandesFinal[i][plat])


for i in range(n_jours_simu):
    print("Jour ", i)
    state = [50 for i in range(n_plat)]
    scen = scenario.scenario(n_clients, n_periodes,n_plat)
    for plat in range(n_plat):

        coeff = regression.regresser(liste_tab_X[plat], liste_tab_Y[plat])
        liste_MDP[plat].coef1 =  coeff[0]
        liste_MDP[plat].coef2 = coeff[1]
        liste_MDP[plat].remplir_MDP()
#le -1 est là car on ne regarde pas ce qu'il se pass eà la fin de la journée!!
    for pe in range(n_periodes-1):



        listeDemandes = scen.simuler(pe, liste_prix)

        for plat in range(n_plat):
            state[plat] -= listeDemandes[plat]
            state[plat] = max(0,state[plat])
            listeRevenus[plat].append(listeDemandes[plat]*liste_prix[plat])

            liste_tab_X[plat].append([pe,liste_prix[plat]])
            liste_tab_Y[plat].append(listeDemandes[plat])

            liste_prix[plat] = liste_MDP[plat].findPrice([pe, state[plat]])
        #rajouter la partie NOTES....
        listePrixFinal.append(liste_prix)

        #revoir cette ligne
        listeDemandesFinal.append(listeDemandes)

        #problème, PRENDRE EN COMPTE LE TEMPS


print(listeRevenus[0][:n_jours_training])
print(listeRevenus[0][n_jours_training:])
print(len(listeRevenus))
print(listeRevenus)
print("FINI")

