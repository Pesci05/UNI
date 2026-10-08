Un'immagine è una **funzione multidimensionale** del tipo
$$
I(u,v)\epsilon R, u,v\epsilon N
$$
Come una funziona a 2 variabili che restituisce **valori d'intensità**.

Questa funzione può avere un output dato da un unico valore(scalare) che viene detto **intensità o livelo di grigio**.
Può dare anche **valori vettoriali**, come nel caso della terna **(RGB)**.
## Immagini a colori
![[Pasted image 20260917104646.png]]
- A,L sono altezza e larghezza
- Per ogni pixel corrispondono 3 valori numerici, 
- In questo caso la funzione sarà:
$$
I \epsilon R^{3},u,v\epsilon N
$$
- Un'immagine di questo tipo è detta a **3 canali**
- Ogni canale è rappresentato da una matrice e l’insieme delle 3 matrici è detto "tensore"

# IMMAGINI
Ogni immagine è composta da un numero finiti di elementi detti **pixel**, i quali hanno una posizione finita e con un **propri valore**.
Quando sia le coordinate che i valori restituiti della funzione sono discreti e finiti diciamo che l’immagine è **digitale**.
Es. La funzione che rappresenta un'immagine in scala di grigi è data da:
$$
I:\{1\dots L\} X \{1\dots A\} \to \{0\dots 255\}
$$

## IMAGE PROCESSING
Sono algoritmi che hanno in **input un'immagine** e ne **restituiscono un'altra**, questo si fa per:
- Image display and printing 
- Image editing 
- Image enhancement 
- Image restoration 
- Image compression
Oppure estrarre da queste immagini informazioni utili.
[[01_Introduzione.pdf#page=12|01_Introduzione, pagina 12]]
Anche se queste operazioni possono essere eseguite da un IA, quest'ultima ha comunque bisogno di **grandi potenze di calcolo** e anche grossi insiemi di dati per l'addestramento.

Questo tipo di algortmi vengono utilizzati in caso:
- Impossibilità di utilizzo della GPU
- Non si ha abbastanza dati per addestrare l'IA
- L'elaborazione deve avvenire in Real Time

### PER COSA SI PUÒ USARE?
- **ISPEZIONE INDUSTRIALE**
- **Telerilevamento**
- **Riconoscimento di un target**
- **Medical imaging**
- **Rimozione del rumore**
- **Correzione del contrasto**
- **Edge detection**
- **Riconoscimento di regioni, segmentazione**
- **Compressione dell'immagine**
- **Image Inpainting**
- **Effetti speciali**

# IMMAGINI DIGITALI
Le immagini sono formate dalla radiazione elettromagnetica(EM), come:
- Luce
- Raggi x
- Onde radio
- Etc...
Lo spettro EM è l'insieme di tutte le possibili frequenze della radiazione elettromagnetica.
Lo spettro è diviso in base alle lunghezze d'onda.
Nel caso della luce si può suddividere in base alla luce visibile dall'occhio umano:
![[Pasted image 20260917112926.png]]

La relazione tra la **lunghezza d'onda** della radaiazione($\lambda$) e la sua frequenza($\ni$) è data da:
$$
\lambda=\frac{c}{v}
$$
c = la velocita dell luce
La lunghezza d'onda si misura in metro.

I colori percepiti dagli essere umani, sono determinati dalla **lunghezza d'onda** della luce che viene riflessa da un'oggetto.

## ACQUISIZIONE DELLE IMMAGINI
Le immagini sono in genere acquisite illuminando una scena e catturando l’energia riflessa dagli oggetti della scena.

L'energia in ingresso (ad esempio la luce) colpisce un materiale reattivo a quel tipo di energia, generando una tensione.

Le risposte dei sensori determinano l’immagine finale
![[Pasted image 20260917114618.png]]

Impossobile acquisire le immagini in modo continuo, per questo si esegue un tipo di **campionamento spaziale**, che permette di avere un'immagine discreta in corrispondenza in base alle coordinate discrete (u,v).

Questo vale anche per l'acuisizione dell'immagine nel tempo, per questo si esegue un **campionamento temporale**, a intervalli discreti.

**CAMPIONARE UN SEGNALE** siginifica misurarlo in posizioni e tempi discreti.

Anche i valori d'**intensità** devono essere **dicreti e limitati**, la **quantizzazione** è il processo di conversione di un segnale analogico continuo nella sua rappresentazione digitale. L’immagine è pertanto composta di valori quantizzati, e può assumere solo un numero finito di valori.
![[Pasted image 20260917115211.png]]

Un'immagine può essere rappresentata come funzione discreta, grazie ai meccanismi di quantizzazione e campionamente, e la funzione sarà:
$$
I:\{1\dots L\}X\{1\dots A\} \to \{0\dots K-1\}
$$

## RAPPRESENTAZIONE DELLE IMMAGINI
La struttura dati utilizzata per rappresentare le immagini a livello di grigio è una matrice 2D che contiene il valore dei pixel.
Il sistema di coordinate (u,v) dei pixel normalmente parte dal primo pixel in alto a sinistra.
I valori della matrice possono essere espressi in qualsiasi tipo di dati 
![[Pasted image 20260917115844.png]]

La **risoluzione spaziale** è determinata dal modo in cui è stato eseguito il campionamento: un campionamento fine produce una maggiore risoluzione spaziale.
La risoluzione spaziale è data dal più piccolo dettaglio dell'immagine distinguibile
- Una telecamera digitale ha una "risoluzione" che dipende dal numero di pixel 
- Nella stampa la risoluzione è espressa in punti per pollice (DPI)

**Saturazione**: dovuta al massimo livello di intensità rappresentabile 
**Rumore**: dovuto al processo di acquisizione e/o di memorizzazione.

# ISTOGRAMMI
#22/09
Gli algoritmi di image processing usano gli **istogrammi** come **struttura dati di base**.
Un istogramma indica quante volte ogni valore quantizzato di intensità compresa in $\{ 0, …, K-1\}$ è presente in un’immagine.

Un istogramma per un immagine a un canale avrà intensità nel range:
$$
I(u,v) \in \{0,K-1\}
$$
Ha esattamente K **bin**, ovvero K elementi.
Nel caso di un'immagine grigia a 8 bit si ha, $K=2^8=256$ bin.

L'istogramma contiene informazioni di tipo statistico, sualla **distribuzione** dei valori de pixel, però la **distribuzione spaziale** non viene presa in considerazione.

# L'UMINOSITÀ DELL'IMMAGINE
La luminosità di un immagine ad un canale, è l'intensità media di tutti i pixel dell'immagine:
$$
L(I)=\frac{1}{AL}\sum ^L_{u=1}\sum^A_{v=1}I(u,v)
$$
In modo equivalente si può fare prendendo in esame l'istogramma:
$$
L(I)=\frac{1}{AL}\sum^{K-1}_{i=0}h(i)i
$$
![[Pasted image 20260922142939.png]]


Il **contrasto** in un’immagine indica la differenza tra le parti chiare e quelle scure e, di conseguenza, la "facilità" con cui gli oggetti nell'immagine possono essere distinti:
- Immagine a contrasto elevato: sono presenti molti valori distinti di intensità .
- Immagine a basso contrasto: l'immagine utilizza solo pochi valori di intensità.

Per definire il contrasto si può utilizzare una formula come:
$$
C_{M}(I)=\frac{max(I)-min(I)}{max(I)+min(I)}
$$
dove il denominatore è uguale a 2 volte la media delle luminosità massime e minime, $media=\frac{max(I)+min(I)}{2}$ .
Ma in questo caso un valore tanto basso a confronto con il resto dell'istogramma, corromperà il risultato della media e per questo bisogna mettere una **soglia**, così da scartare quel valore.
![[Pasted image 20260922144047.png]]
Gli istogrammi permettono di rilevare anche problemi di esposizione/saturazione:
[[03_Istogrammi.pdf#page=13|03_Istogrammi, pagina 13]]

Gli istogrammi possono **mostrare**, l**a modifca dell'immagine,** ma nel caso contrario non garantisce che non si stata manipolata.

## BINNING
Immagini ad alta risoluzione dei livelli d'intensità possono produrre istogrammi molto grandi.
Per ovviare a questo problema si deve effettuare il **binning**, cioè l'intervallo totale verrà suddiviso in sotto-intervalli.
![[Pasted image 20260922145201.png]]

Gli intervalli sono suddivisi per avere la stessa dimensione quindi:
$$
\frac{K}{number\_of\_bins}
$$
Per sapere a quale bin appartiene un livello d'intensità:
$$
I(u,v)*\frac{B}{K}
$$
dove:
- I(u,v) indica il valore del pixel
- K è il numero di intensità dlell'immagine
- B è il numero totale di bin dell'istogramma
- la divisione è intera

## IMMAGINI A PIÙ COLORI
Per immagini a più colori, quidni a 3 canali,  il suo istogrammi possono essere calcolati:
- Convertendo l'immagine a un solo canale
- Calcolare un istogramma per ogni canale dell'immagine
Ma in entrambe le soluzione perdo informazioni.
Per rappresentare tutti i colori devono quindi essere rappresentati tramite un **istogramma tridimensionale**, dove tutti i colori vengono congiunti dove **ogni bin è associato ad una possibile terna di valori RGB**.
In tal caso, per rappresentare l’istogramma tridimensionale, ho bisogno di un tensore di dimensioni K x K x K.
![[Pasted image 20260922153114.png]]

Anche in questo caso è possibile effettuare **binning**.

# OPERATORI PUNTUALI
Gli operatori puntuali **cambiano l'ntnsità di un pixel** in base ad una funzione che dipende solo da quel pixel.

Gli operatori puntuali sono chiamati **omogenei** quando $f()$ non dipende dalle specifiche coordinate (u,v).

- **Addizione**
- **Moltiplicazione**
- **Funzioni a valori reali**
- **Thresholding (Soglia)**
	Se un pixel **supera** un certa soglia, il valore sarà settato ad un certo valore, la stessa cosa succede anche al contrario.
	![[Pasted image 20260922155030.png|359]]
- **Clamping**
	L’operatore di clamping (descritto dalla formula qui sotto) serve a "tagliare" i valori dei pixel in un determinato intervallo.
- **Inversione dell'immagine**
	$f_{invert}(a)=-a+a_{max}=a_{max}-a$
- **Regolazione automatica del contrasto**
	Modifica le intensità dei pixel in modo tale che l'intervallo di valori sia usato completamente, si può usare anche per diminuire il contrasto

## EQUALIZZAZIONE DEGLI ISTOGRAMMI
Utilizzare gli operatori puntuali per avere una **distribuzione uniforme all'interno dell'istogramma**.

Avviene grazie a questa funzione: 
$$
s = T(i) = K\sum^i_{j=0} p_{r}(j)
$$
- $i = l(u,v) \to$ Luminosità di un pixel all'interno di una qualsiasi  MxN
- $p_{r} = \frac{h(i)}{MN} \to$ è la probabilità di occorrenza di i
- K è il numero di livelli d'intensità dell'immmagine
- $T(i)$ è la funzione di mapping ed è monotona non decrescente
- s è il valore d'intensità del pixel alle coordinate (u,v) nell'immagine risultante
![[Pasted image 20261006174009.png]]

# FILTRI
Un filtro spaziale utilizza (anche) il valore dei pixel circostanti, selezionati tramite una finestra dell’immagine centrata sul pixel corrente.
![[Pasted image 20261001112916.png]]

Un filtro molto comune è quello del **blurring**, e consiste nel usare una finestra 3x3 e calcolarne la media.

Esistono diversi tipi di filtri, e possono variare in base a:
- **Filter shape**
	I filtri non sono necessariamente quadrati
- **Filter size**
	Variare in grandezza 3x3,4x4,5x5...
- **Filter function**
	Può essere **lineare** o non lineare

## FILTER FUNCTION LINEARE
Si basa su una funzione lineare come:
$$
f(R_{u,w})=w_{1}l(u-1,v-1)+w_{2}(u-1,v)+\dots
$$
Dove  $w_{1},w_{2}\dots$ sono i pesi del filtro.

Il **Kernel** anche detto **Filter Matrix**, H contiene il valore dei **pesi** che caratterizzano lo specifico filtro lineare, questo kernel è una matrice di valori reali con la stessa dimensione e forma di R.
$$
H(i,j) = \left[ \begin{matrix}
\frac{1}{9} \space\frac{1}{9}\space\frac{1}{9} \\ \frac{1}{9}\space\frac{1}{9}\space\frac{1}{9} \\ \frac{1}{9}\space\frac{1}{9}\space\frac{1}{9}
\end{matrix} \right] =  \frac{1}{9}\left[\begin{matrix}
 1\space 1\space 1 \\ 1\space 1\space 1 \\ 1\space1\space1 
\end{matrix}\right]
$$
La **convoluzione** è l'applicazione di un filtro lineare ad un'immagine.

Quando si incontrano i borid di un'immagine si può fare:
- **Cropping**
	Ritaglio un’immagine più piccola escludendo i bordi
- **Padding**
	Aggiungo una cornice all’immagine di larghezza K e altezza L prima di applicare il filtr

### FILTRO GAUSSIANO
Posso esprimere il valore del generico peso (i,j) di H, kernel Gaussiano, usando la definizione di funzione Gaussiana (bidimensionale):
$$
H(i,j) = Ke^{-(i^2+j^2)/2\sigma^2}=Ke^{-r^2/2\sigma^2} 
$$
- r è la distanza di (i,j) dall'hotspot
- $\sigma$ è la larghezza della curva a campana
- K è una costante che serve ad esprimere il valore del peso massimo, corrispondente all'hot spot

# RUMORE E FILTRI NON LINEARI
Quando si acquisisce un'immagine, si possono creare degli **errori, degradazioni** dell'immagine, questo si chiama ==**RUMORE**==.

## IMAGE RESTORATION
È la pratica di **rimozione del rumore** da un'immagine.

Può essere fatta:
- Nel dominio **spaziale**
- Nel dominio delle **frequenza**

## TIPI DI RUMORE
- **SALT AND PEPPER NOISE**
	
- 
# EDGE DETECTION
Un **edge** viene definito come un cambio drastico della luminosità, spesso avviene in corrispondenza dei bordi.

L'==**EDGE DETECTION**== è la processo di rilevamento degli edge, gi edge vengono utilizzati per definire la forma degli oggetti.
Il suo output sarà un'immagine binaria che rappresenta gli edge dell'immagine input.
![[Pasted image 20261008104052.png]]

Visto che può essere definito come un cambio drastico di luminosità può essere vista come una **step function**, rispetto ad una data direzione.
![[Pasted image 20261008104154.png]]

Gli edge in realtà non sono un salto drastico tra una luminosità e l'altra, ma il cambio di luminosità cambià in maniera pià *smussata*.
In altri termini, un edge reale corrisponde ad un rapido incremento o decremento dell’intensità dei pixel rispetto ad una data direzione

Possiamo supporre che le immagini sia funzioni unidimensionali dette l(x).
La derivata prima di l(x)rileverà che ci sarà un picco in l'(x) in corrisponenza dell'edge.
La derivata seconda l'' cambia segno e viene detta anche **zero crossing**. 
![[Pasted image 20261008105549.png]]

L’idea generale nell’edge detection è **ricondurre il problema dell’individuazione degli edge al calcolo della derivata prima di I**, e poi selezionare come punti di "edge" quei pixel corrispondenti ai valori (in modulo) più alti di I’.

Però questo crea problemi nel calcolo della derivata poiche la funzione dell'immagine sarà:
- l() è una funzione campionata, con un dominio discreto
- l() non è definita in modo analitico
Soluzione:
La derivata l() può essere calcolata usando le **differenze finite**.
Le differenze possono essere:
- **Destra**
	$\Delta+f(x)=f(x+1)-f(x)$
- **Sinistra**
	$\Delta -f(x) = f(x)-f(x-1)$
- **Centrale**
	$\Delta f(x) = \frac{1}{2}(f(x+1)-f(x-1))$

Però un'immagine è formata da 2 dimensioni, per cui dobbiamo estendere questo approccio nelle funzioni a 2 variabili, questo si può fare grazie al **gradiente**(derivate parziali).

Per utilizzare il gradiente su un'immagine si deve calcolare le derivate pariali sia per la direzione verticael, sia per quella orizzontale.
$$\frac{\partial l}{ \partial u} \space e \space \frac{\partial l}{ \partial v}$$
Il gradiente dell'immagine sarà:
$$
\nabla l(u,v) =\left[   \begin{matrix}
\frac{\partial l}{\partial u}(u,v) \\
\frac{\partial l}{\partial v}(u,v)
\end{matrix}  \right]
$$


