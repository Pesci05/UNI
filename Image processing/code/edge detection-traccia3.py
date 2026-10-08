# Il codice seguente legge un'immagine, la converte in scala di grigi
# e la memorizza nella matrice I. 
# L'esercizio consiste in: 
# 1) Creare dei kernel convolutivi per il calcolo delle derivate orizzontali e verticali tramite 
#   operatore di Sobel (kernel size: 3X3)
# 2) Calcolare le derivate orizzontali e verticali di I applicando tali kernel alla matrice I utilizzando
#    la procedura di convoluzione (con cropping) creata nell'esercizio sui filtri
# 3) Calcolare il valore del modulo del gradiente usando i valori delle derivate risultanti

import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from scipy import signal  



def ConvoluzioneEfficiente(I,kernel):
    N = I.shape[0]
    M = I.shape[1]
    kH = kernel.shape[0]
    kW = kernel.shape[1]
    L= (kH - 1) // 2
    K= (kW - 1) // 2
    
    oH, oW = N - kH + 1, M - kW + 1
    out = np.zeros((oH, oW))
    
    for u in range(K, M - K):
        for v in range(L, N - L):
            out[v - L, u - K] = np.sum(I[v - L: v + L + 1, u - K: u + K + 1] * kernel)
    
    out= np.rint(out)
    
    return out



# Immagine: ---------------------------
im= io.imread('./operatore_puntuale-traccia/animali.png')
#im= io.imread('./roditore.bmp')

fig=plt.figure()
imgplot = plt.imshow(im)
plt.show()

# conversione RGB -> scala di grigi
#I= 1/3 * (im[:,:,0] +  im[:,:,1] +  im[:,:,2])
I= 0.2125 * im[:,:,0] +  0.7154 * im[:,:,1] +  0.072 * im[:,:,2]
I= np.rint(I)

fig=plt.figure()
imgplot = plt.imshow(I, cmap='gray', vmin=0, vmax=255)
plt.show()


# Soluzione ------------------------------

# Creo i kernel per Sobel:
vertical_kernel = np.array([[1, 0, -1],
                            [2, 0, -2], 
                            [1, 0, -1]])
orizontal_kernel = np.array([[1, 2, 1],
                             [0, 0, 0], 
                             [-1, -2, -1]])    
# [TO DO]   


# Calcolo le derivate parziali orizzontale (du) 
# e verticale (dv) usando la funzione ConvoluzioneEfficiente:
    
# [TO DO]
conv_du = ConvoluzioneEfficiente(I, orizontal_kernel)
conv_dv = ConvoluzioneEfficiente(I, vertical_kernel)

# Mostro le derivate:
plt.figure()
plt.imshow(conv_du, cmap='gray', vmin=0, vmax=255)
plt.show()

plt.figure()
plt.imshow(conv_dv, cmap='gray', vmin=0, vmax=255)
plt.show()


# Calcolo e mostro il modulo del gradiente:
    
# [TO DO]
magnitude = np.sqrt(conv_du**2 + conv_dv**2)
plt.figure()
plt.imshow(magnitude, cmap='gray', vmin=0, vmax=255)
plt.show()