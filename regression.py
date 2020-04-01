import numpy as np
from sklearn.linear_model import LinearRegression
import math
import matplotlib.pyplot as plt
"""
tab_X = np.loadtxt('data_X.dat')
tab_Y = np.loadtxt('data_Y.dat')
print(tab_Y)
for i in range(len(tab_Y)):
    #tab_Y[i] = math.sqrt(-2*math.log(tab_Y[i]/300))
    tab_Y[i] = tab_Y[i]
    #tab_Y[i] = np.log(tab_Y[i]+0.01)
model = LinearRegression().fit(tab_X,tab_Y)
print(model.score(tab_X, tab_Y))
tab_XX = tab_X[:,0]
plt.plot(tab_XX, tab_Y)
plt.show()
"""

#idée étant donnée des données d'entrainement et de sortie, renvoyer la fonction de régression

def regresser(tab_X, tab_Y):
    model = LinearRegression().fit(tab_X,tab_Y)
    return model.coef_
