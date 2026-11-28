# Rumore e Filtri Non Lineari

> **Slide:** [[06_Rumore e filtri non lineari.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

Quando si acquisisce un'immagine, si possono creare degli **errori, degradazioni** dell'immagine: questo si chiama ==**RUMORE**==.
Il rumore può essere causato da:
- Focus Blurring (vedi anche [[IMAGE FORMATION#Depth of focus]])
- Blurring due to camera motion (vedi [[IMAGE FORMATION#Integrazione temporale (Temporal integration and sampling)]])
- Analog to digital conversion errors (vedi [[IMAGE FORMATION#Sorgenti di rumore]])
- Transmission errors
- etc...

## Image Restoration
È la pratica di **rimozione del rumore** da un'immagine.

Può essere fatta:
- Nel dominio **spaziale**
- Nel dominio delle **frequenze** (vedi [[11 - Trasformata di Fourier#Filtri selettivi]])

## Tipi di Rumore
- **Salt and Pepper Noise**
	Causato da transmission errors, interferenze elettromagnetiche, ...
- **Gaussian Noise**
	È un tipo di rumore bianco aggiunto ad un'immagine e distribuito seguendo una distribuzione Gaussiana.
	Ogni pixel dell'immagine è soggetto ad una perturbazione *additiva $n$*:
	$$
	I'(u,v) = I(u,v) + n
	$$
	Dove $n$ è un rumore casuale i cui valori possibili sono distribuiti in maniera *Gaussiana*.
	![[Pasted image 20261110224105.png]]
- **Speckle Noise**
	Simile al rumore Gaussiano, con pixel perturbati in maniera casuale.
	Il rumore in questo caso non è additivo ma moltiplicativo:
	$$
	I'(u,v) = I(u,v) \cdot n
	$$
	con $n$ variabile da pixel a pixel.
- **Periodic Noise**
	Causato da disturbi hardware di natura periodica.

Salt and pepper, Gaussian e speckle possono essere **eliminati o ridotti tramite i filtri spaziali**.
Periodic noise invece può essere eliminato **usando i filtri nel frequency domain** ([[11 - Trasformata di Fourier#Filtri selettivi]]).

Di solito per fare un'Image Restoration si preferisce utilizzare un filtro **non lineare**.

## Filtri Non Lineari
I pixel contenuti nella finestra $R$ del filtro sono combinati utilizzando una funzione non lineare.
![[Pasted image 20261110224809.png]]

### MIN e MAX
$$
I'(u,v) = f(R_{u,v}) = \min\{ I(u+i,v+j) \mid -k\leq i\leq k, -k\leq j\leq k \}
$$
$$
I'(u,v) = f(R_{u,v}) = \max\{ I(u+i,v+j) \mid -k\leq i\leq k, -k\leq j\leq k \}
$$
[[06_Rumore e filtri non lineari.pdf#page=13|06_Rumore e filtri non lineari, pagina 13]]

### Median Filter
Riesce a rimuovere meglio il rumore mantenendo gran parte della struttura dell'immagine:
$$
I'(u,v) = f(R_{u,v}) = \text{median}\{ I(u+i,v+j) \mid -k\leq i\leq k, -k\leq j\leq k \}
$$
![[Pasted image 20261110225358.png]]
[[06_Rumore e filtri non lineari.pdf#page=15|06_Rumore e filtri non lineari, pagina 15]]
