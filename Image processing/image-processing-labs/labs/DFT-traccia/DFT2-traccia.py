# Il codice seguente legge un'immagine, la converte in scala di grigi
# e la memorizza nella matrice I. 
# L'esercizio consiste nel definire la funzione che calcola la 2D DFT di I
#
# Suggerimenti:
# - Usare -2j * np.pi per calcolare il termine "-2 pi greco radice di - 1"
# - F = np.zeros((N, M),dtype=complex) inizializza un ndarray a valori complessi
# - np.exp(c) calcola la funzione esponente e il suo argomento c può essere un numero complesso


import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def DFT(I):
    N, M = I.shape
    F = np.zeros((N, M),dtype=complex)

    for i in M:
        for j in N:
            s = 0
            

    return F


# Immagine: ---------------------------
im= io.imread('./rettangolo.png')
#im= io.imread('./rettangolo-trasl.png')
#im= io.imread('./rettangolo-rot.png')

# conversione RGB -> scala di grigi
#I= 1/3 * (im[:,:,0] +  im[:,:,1] +  im[:,:,2])
I= 0.2125 * im[:,:,0] +  0.7154 * im[:,:,1] +  0.072 * im[:,:,2]
I= np.rint(I)

fig=plt.figure()
imgplot = plt.imshow(I, cmap='gray', vmin=0, vmax=255)


F= DFT(I)