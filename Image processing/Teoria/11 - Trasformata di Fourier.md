# Trasformata di Fourier

> **Slide:** [[11_Trasformata di fourie_I.pdf]] | [[12_Trasformata di Fourier - Parte II.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

Le immagini fino ad ora le abbiamo viste come matrici, definite dal valore di 2 funzioni, dove vengono contenuti i valori dei pixel; questo tipo di rappresentazione viene nominata nel **dominio spaziale** a 2 dimensioni.

Però le immagini possono essere rappresentate anche nel **dominio delle frequenze**, dove alcune operazioni di manipolazione delle immagini diventano più semplici da effettuare.

## Idea base
La trasformata di Fourier permette di esprimere una qualsiasi funzione $f()$ come combinazione lineare di una **base di funzioni**.

Le funzioni base sono delle **sinusoidi** (seni e coseni), e l'output della trasformata sono i *coefficienti* della combinazione lineare.

[[11_Trasformata di fourie_I.pdf#page=11|11_Trasformata di fourie_I, pagina 11]]

---
## Tecniche spettrali
Per trasformare segnali audio, immagini, video ecc. dal dominio temporale/spaziale al dominio delle frequenze è possibile utilizzare diverse trasformazioni, tra loro simili:

- **Fourier Transform**
- **Discrete Fourier Transform (DFT)**
- **Discrete Cosine Transform (DCT)**

Una sinusoide viene definita da **tre grandezze principali**:
- **Lunghezza d'onda** $\to$ inversa della frequenza ($T = 1/f$, nello spazio coincide con $\lambda$)
- **Ampiezza**: massima oscillazione del segnale
- **Fase**: *phase shift* (traslazione dell'onda)

### Concetti matematici
Formula di Eulero:
$$
e^{i\rho} = \cos \rho + i \sin \rho
$$
Numeri complessi espressi in coordinate polari:
$$
z = re^{i\rho} = r(\cos \rho + i \sin \rho)
$$
Dove $r$ è il modulo:
$$
r = |z| = \sqrt{x^2 + y^2}
$$

[[11_Trasformata di fourie_I.pdf#page=21|11_Trasformata di fourie_I, pagina 21]]

## Serie di Fourier
Quasi tutte le funzioni periodiche $f(x)$ con periodo $T$ possono essere rappresentate come una sommatoria infinita di sinusoidi, detta **serie di Fourier**:
$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos\left(\frac{2\pi n x}{T}\right) + b_n \sin\left(\frac{2\pi n x}{T}\right) \right)
$$
dove $a_n$ e $b_n$ sono i **coefficienti di Fourier**.

Però se una funzione non è periodica si può prendere in esame un periodo finito e replicare questo periodo all'infinito (estensione periodica).

## Trasformata di Fourier
La trasformata di Fourier **estende la serie di Fourier a qualsiasi funzione**, comprese anche quelle non definite in un intervallo limitato ($T \to \infty$), utilizzando la formula di Eulero:

$$
F(\mu) = \int_{-\infty}^{+\infty} f(t) e^{-j 2\pi \mu t}\,dt
$$
o, equivalentemente:
$$
F(\mu) = \int_{-\infty}^{+\infty} f(t)\left[\cos(2\pi \mu t) - j\sin(2\pi \mu t)\right]dt
$$

In entrambi i casi $F()$ è definita per $\mu \in \mathbb{R}$.
La variabile $\mu$ indica una **frequenza continua** (e può assumere anche valori negativi).

La funzione $F(\mu)$ solitamente è una **funzione complessa**, **periodica**, dove il suo modulo $|F(\mu)|$ **è il suo spettro**.

Se si ha solo la funzione $F(\mu)$ si può ricavare la funzione $f(t)$ tramite la **trasformata inversa**:
$$
f(t) = \int_{-\infty}^{+\infty} F(\mu) e^{j 2\pi \mu t}\,d\mu
$$
$f(t)$ ed $F(\mu)$ formano una *Fourier Transform pair*.

## Discrete Fourier Transform (DFT)
Un segnale digitale è campionato in modo discreto.
- **1D DFT** su $M$ campioni $\{y_0, \dots, y_{M-1}\}$:
  $$
  F(m) = \sum_{k=0}^{M-1} y_k e^{-j 2\pi \frac{mk}{M}}, \qquad m = 0, \dots, M-1
  $$
  e **IDFT**:
  $$
  y_k = \frac{1}{M}\sum_{m=0}^{M-1} F(m) e^{j 2\pi \frac{mk}{M}}, \qquad k = 0, \dots, M-1
  $$
- **Complessità**: la DFT diretta ha complessità $O(M^2)$; tramite **Fast Fourier Transform (FFT)** si scende a $O(M \log M)$ (vedi [[10 - Complessità Computazionale]]).

### 2D Discrete Fourier Transform (immagini)
Data un'immagine $f(x,y)$ di dimensioni $M \times N$:
$$
F(u,v) = \sum_{x=0}^{M-1}\sum_{y=0}^{N-1} f(x,y) e^{-j 2\pi \left(\frac{ux}{M} + \frac{vy}{N}\right)}
$$
$$
f(x,y) = \frac{1}{MN}\sum_{u=0}^{M-1}\sum_{v=0}^{N-1} F(u,v) e^{j 2\pi \left(\frac{ux}{M} + \frac{vy}{N}\right)}
$$
- $F(0,0)$ è il **DC coefficient** ed equivale alla somma delle intensità di tutti i pixel ($= \text{Luminosità} \cdot MN$).
- **Spettro e Fase** (in coordinate polari $F(u,v) = |F(u,v)| e^{j\phi(u,v)}$):
  - **Modulo (spettro)** $|F(u,v)|$: indica l'ampiezza/intensità con cui le sinusoidi a frequenza $(u/M, v/N)$ sono presenti nell'immagine. È invariante alla traslazione ma ruota con l'immagine.
  - **Fase** $\phi(u,v)$: esprime la traslazione (*phase shift*) e contiene l'informazione strutturale su *dove* si trovano le caratteristiche nell'immagine.
- **DFT Centering**: moltiplicando $f(x,y)$ per $(-1)^{x+y}$ prima della DFT si sposta il DC coefficient al centro di $F$ (scambiando i quadranti), raggruppando le basse frequenze al centro. Per visualizzare lo spettro riducendo il contrasto del DC si usa spesso $\log(1 + |F(u,v)|)$.

## Teorema della convoluzione (Convolution Theorem)
Siano $f$ ed $h$ due funzioni ed $F$ ed $H$ le corrispondenti **Trasformate di Fourier** con:
$$
F = \mathcal{F}(f), \quad H = \mathcal{F}(h)
$$
Allora la Trasformata di Fourier della convoluzione tra $f$ ed $h$ è uguale al prodotto elemento per elemento tra $F$ ed $H$ (**Convolution Theorem**):
$$
\mathcal{F}(f * h) = F \cdot H \qquad \Longleftrightarrow \qquad f * h = \mathcal{F}^{-1}(F \cdot H)
$$

## Convoluzione tramite DFT
Per applicare un filtro direttamente nel dominio delle frequenze:
1. Calcolare la DFT centrata dell'immagine $I$ ottenendo $F$.
2. Moltiplicare elemento per elemento $F$ per una **maschera** $H$ (della stessa dimensione di $F$) costruita nel dominio delle frequenze.
3. Applicare la IDFT a $F \cdot H$ per tornare nel dominio spaziale.

*(Se si parte da un filtro spaziale più piccolo dell'immagine, si applica zero-padding prima della DFT).*

### Filtro passa basso
Mantiene tutte le frequenze al di sotto di una data frequenza di cutoff $D_0$, per eliminare le frequenze più alte, producendo un effetto simile al **blurring**.

Un filtro passa basso ideale è una **maschera** binaria $N \times M$ ($H(u,v) = 1$ se $D(u,v) \le D_0$, $0$ altrimenti):
![[Pasted image 20261126114348.png]]
La maschera è applicata su $F$ e non sull'immagine di partenza. Un taglio netto può causare artefatti di *ringing*.

### Filtro passa alto
Filtro che mantiene tutte le frequenze più alte di una certa frequenza (evidenziando i dettagli/bordi); questo è l'**inverso (complementare) del filtro passa-basso**:
$$
H_{\text{HP}}(u,v) = 1 - H_{\text{LP}}(u,v)
$$

### Filtro gaussiano
Filtro che permette un graduale passaggio da un valore basso ad un valore alto (evitando il *ringing*), spesso utilizzato per smussare questi passaggi:
$$
H_{\text{LP}}(u,v) = e^{-\frac{D^2(u,v)}{2D_0^2}}, \qquad H_{\text{HP}}(u,v) = 1 - e^{-\frac{D^2(u,v)}{2D_0^2}}
$$
dove $D(u,v)$ è la distanza dal centro $(M/2, N/2)$. Utilizzato anche per comprimere il segnale (es. DCT in JPEG).

### Filtro Butterworth
Alternativa ai filtri Gaussiani in cui l'ordine $n$ controlla la pendenza della transizione:
$$
H_{\text{HP}}(u,v) = \frac{1}{1 + \left(\frac{D_0}{D(u,v)}\right)^{2n}}
$$

### Filtri selettivi
Utilizzati per mascherare solo alcune frequenze specifiche (es. rimozione del **rumore periodico**, vedi [[06 - Rumore e Filtri Non Lineari#Tipi di Rumore]]):
- **Bandpass e bandreject filter** (mascherano/mantengono una banda circolare di frequenze)
- **Notch reject e notch pass filter** (azzerano/isolano specifici picchi di frequenza nello spettro)

## Vantaggi dei filtri tramite frequenze
Il [[#Teorema della convoluzione (Convolution Theorem)|Teorema della convoluzione]] dice che esiste un **filtro spaziale, il quale dà come risultato lo stesso di un filtro nel dominio delle frequenze**, però questo solo **teoricamente**: non è semplice trovare un filtro spaziale tale che dia lo stesso risultato di un filtro in frequenza; un esempio di questi filtri sono quelli **selettivi**.

Inoltre, dal punto di vista computazionale, per immagini $M \times M$ e kernel spaziali $k \times k$:
- Convoluzione spaziale: $O(M^2 k^2)$
- Filtraggio tramite FFT: $O(M^2 (2\log M + 1))$

Conviene usare la FFT quando il kernel è grande ($k^2 > 2\log M + 1$, ad es. per $M = 300$, $k \ge 6$).
