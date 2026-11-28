# Filtri

> **Slide:** [[05_Filtri.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

Un filtro spaziale utilizza (anche) il valore dei pixel circostanti, selezionati tramite una finestra dell'immagine centrata sul pixel corrente.
![[Pasted image 20261001112916.png]]

Un filtro molto comune è quello del **blurring**, e consiste nell'usare una finestra $3 \times 3$ e calcolarne la media.

Esistono diversi tipi di filtri, e possono variare in base a:
- **Filter shape**: i filtri non sono necessariamente quadrati
- **Filter size**: variano in grandezza $3\times 3, 4\times 4, 5\times 5\dots$
- **Filter function**: può essere **lineare** o non lineare (vedi [[06 - Rumore e Filtri Non Lineari]])

## Filter Function Lineare
Si basa su una funzione lineare come:
$$
f(R_{u,v}) = w_{1}I(u-1,v-1) + w_{2}I(u-1,v) + \dots
$$
Dove $w_{1}, w_{2}, \dots$ sono i pesi del filtro.

Il **Kernel** (anche detto **Filter Matrix**), $H$, contiene il valore dei **pesi** che caratterizzano lo specifico filtro lineare; questo kernel è una matrice di valori reali con la stessa dimensione e forma di $R$.
$$
H(i,j) = \begin{bmatrix}
\frac{1}{9} & \frac{1}{9} & \frac{1}{9} \\
\frac{1}{9} & \frac{1}{9} & \frac{1}{9} \\
\frac{1}{9} & \frac{1}{9} & \frac{1}{9}
\end{bmatrix}
= \frac{1}{9}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
$$
La **convoluzione** è l'applicazione di un filtro lineare ad un'immagine (per la convoluzione nel dominio delle frequenze vedi [[11 - Trasformata di Fourier#Teorema della convoluzione (Convolution Theorem)]]).

Quando si incontrano i bordi di un'immagine si può fare:
- **Cropping**: ritaglio un'immagine più piccola escludendo i bordi
- **Padding**: aggiungo una cornice all'immagine di larghezza $K$ e altezza $L$ prima di applicare il filtro

### Filtro Gaussiano
Posso esprimere il valore del generico peso $(i,j)$ di $H$, kernel Gaussiano, usando la definizione di funzione Gaussiana (bidimensionale):
$$
H(i,j) = K e^{-(i^2+j^2)/2\sigma^2} = K e^{-r^2/2\sigma^2}
$$
- $r$ è la distanza di $(i,j)$ dall'hotspot
- $\sigma$ è la larghezza della curva a campana
- $K$ è una costante che serve ad esprimere il valore del peso massimo, corrispondente all'hotspot

> **Applicazioni in Lab:** Il Gaussian smoothing è il primo passo della pipeline di [[IMAGE FORMATION#CANNY edge detector: Pipeline|Canny edge detection]].
