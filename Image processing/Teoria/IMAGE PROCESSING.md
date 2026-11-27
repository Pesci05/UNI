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
- **Edge detection** ^d83f5a
- **Riconoscimento di regioni, segmentazione**
- **Compressione dell'immagine**
- **Image Inpainting**
- **Effetti speciali**

# IMMAGINI D|IGITALI
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

Le immagini normalmente vengono acquisite trmite la **fifrazione della luce**, ma esiston anche altre tipologie di acquisizione attraverso altri tipi di onde come:
- Immagini radar(onde radio e microonde)
- Risonanza magnetica (onde radio) 
- Imaging a microonde 
- Imaging a infrarossi 
- Fotografie 
- Telescopi per l'imaging ultravioletto 
- Raggi X e tomografia computerizzata 
- Tomografia a emissione di positroni (raggi gamma) 
- Ultrasuoni (onde sonore, non EM, con una frequenza maggiore di 20 kHz

## OCCHIO UMANO
![[Pasted image 20261127192732.png]]
L'occhio umano è formato da:
- **Cristallino/lente**: proietta la luce degli oggetti sulla retina
- **Retina**: Ricoperta di cellule nervose sensibili alla luce chiamate **fotoricettori**, che sono **coni** e **bastoncelli**
- **Coni**: si concentrano in una zone della retina chiamata **fovea**, sensibili al calore
- **Bastoncelli**: Son diffusi su tutta la retina, non sono sensibili al calore, ma sensibili alle diverse intensità di luce.
I muscoli dell'occhio possono cambiare la forma del cristallina, permettendo di **concentrarsi/focus** su oggetti vicini o lontani.

L'**immagine viene messa a fuoco dalla retina**, le **terminazione nervosi presenti vengono eccitate e mandano segnali al cervello**, l'occhio umano può percepire vino a $10^{10}$ intensità di luminosità

## ACQUISIZIONE DELLE IMMAGINI
Le immagini sono in genere acquisite illuminando una scena e catturando l’energia riflessa dagli oggetti della scena.

L'energia in ingresso (ad esempio la luce) colpisce un materiale reattivo a quel tipo di energia, generando una tensione.

Le risposte dei sensori determinano l’immagine finale
![[Pasted image 20260917114618.png]]

Impossibile acquisire le immagini in modo continuo, per questo si esegue un tipo di **campionamento spaziale**, che permette di avere un'immagine discreta in corrispondenza in base alle coordinate discrete (u,v).

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

Gli istogrammi **non mantengono** i dati di disposizione dei pixel, perde l'informazione riguardo alla **distibuzione spaziale** dell'immagine.

## L'UMINOSITÀ DELL'IMMAGINE
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
Gli istogrammi permettono di rilevare dei difetti dell'immagine grazie alla loro forma per esempio:
- Problemi di **esposizione** $\to$ valori di illuminazione sono fuori dall'intervallo percepibile del sensore
- **Manipolazioni** $\to$ Picchi e lacune presenti nell'istogramma

Gli istogrammi possono **mostrare**, l**a modifca dell'immagine,** ma nel caso contrario non garantisce che non si stata manipolata.

Anche le **compressione** e **codifiche** possono influenzare l'istogramma.
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
Per immagini a più colori, quind a 3 canali,  i loro istogrammi possono essere calcolati:
- Convertendo l'immagine a un solo canale
- Calcolare un istogramma per ogni canale dell'immagine
Ma in entrambe le soluzione perdo informazioni.
Per rappresentare tutti i colori devono quindi essere rappresentati tramite un **istogramma tridimensionale**, dove tutti i colori vengono congiunti dove **ogni bin è associato ad una possibile terna di valori RGB**.
In tal caso, per rappresentare l’istogramma tridimensionale, ho bisogno di un tensore di dimensioni K x K x K.
![[Pasted image 20260922153114.png]]

Anche in questo caso è possibile effettuare **binning**.

# OPERATORI PUNTUALI
Gli operatori puntuali **cambiano l'intensità di un pixel** in base ad una funzione che dipende solo da quel pixel.

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
	Modifica le intensità dei pixel in modo tale che l'intervallo di valori sia usato completamente, si può usare anche per diminuire il contrasto, viene definito matematicamente qui $\to$ [[04_Operatori puntuali.pdf#page=14|04_Operatori puntuali, pagina 14]]

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

Quando si incontrano i borididi un'immagine si può fare:
- **Cropping**
	Ritaglio un’immagine più piccola escludendo i bordi
- **Padding**
	Aggiungo una cornice all’immagine di larghezza K e altezza L prima di applicare il filtro

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
Il rumore può essere causato da:
- Focus Blurring
- Blurring due to camera motion
- Analog to digital convertions errors
- Transimission errors
- etc...

## IMAGE RESTORATION
È la pratica di **rimozione del rumore** da un'immagine.

Può essere fatta:
- Nel dominio **spaziale**
- Nel dominio delle **frequenza**

## TIPI DI RUMORE
- **SALT AND PEPPER NOISE**
	Causato da transmission errors, interferenze elettromagnetiche,...
- **Gaussian Noise**
	è un tipo di rumore bianco aggiunto ad un’immagine e distribuito seguendo una distribuzione Gaussiana con media .
	Ogni pixel dell'immagine è soggetto ad una perturnazione *additiva n*:
	$$
	l'(u,v) = l(u,v)+n 
	$$
	Dove *n* è un rumore casuale i cui valori possibili sono distibuiti in maniera *Gaussaiana*![[Pasted image 20261110224105.png]]
-  **Speckle Noise**
	Simile al rumore Gaussiano, con pixel perturbati in maniera casuale.
	Il rumore in questo caso non è additivo ma moltiplicativo.
	$$
	l'(u,v) = l(u,v)\cdot n 
	$$
	con n variabile da pixel a pixel.
- **Periodic noise**
	Causato da disturbi hardware di natura periodica 

Salt and pepper, Gaussian e speckle possono essere **eliminati o ridotti tramite i filtri spaziali.**
Periodic invece può essere eliminato **usando** i **filtri nel frequency domain**.

Di solito per fare un Image restoration si preferisce utilizzare un filtro **non lineare**.

## Filtri non lineari
I pixel contenuti nella finestra R del filtro sono combinati utilizzando una funzione non lineare.
![[Pasted image 20261110224809.png]]

### MIN e MAX
$$
I'(u,v) = f(R_{u,v})=min\{ I(u+i,v+j)|-k\leq i\leq k,-k\leq j\leq k \} \\
I'(u,v) = f(R_{u,v})=max\{ I(u+i,v+j)|-k\leq i\leq k,-k\leq j\leq k \} 
$$
[[06_Rumore e filtri non lineari.pdf#page=13|06_Rumore e filtri non lineari, pagina 13]]

### Median filter
Riesce a rimuovere meglio il rumore mantendendo gran parte della struttura dell’immagine.
$$
I'(u,v) = f(R_{u,v})=median\{ I(u+i,v+j)|-k\leq i\leq k,-k\leq j\leq k \} 
$$
![[Pasted image 20261110225358.png]]
[[06_Rumore e filtri non lineari.pdf#page=15|06_Rumore e filtri non lineari, pagina 15]]

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
Le differenze possono essere: ^7031da
- **Destra**
	$\Delta+f(x)=f(x+1)-f(x)$
- **Sinistra**
	$\Delta -f(x) = f(x)-f(x-1)$
- **Centrale**
	$\Delta f(x) = \frac{1}{2}(f(x+1)-f(x-1))$

Però un'immagine è formata da 2 dimensioni, per cui dobbiamo estendere questo approccio nelle funzioni a 2 variabili, questo si può fare grazie al **gradiente**(derivate parziali).

Per utilizzare il gradiente su un'immagine si deve calcolare le derivate parziali sia per la direzione verticale, sia per quella orizzontale.
$$\frac{\partial l}{ \partial u} \space e \space \frac{\partial l}{ \partial v}$$
Il gradiente dell'immagine sarà:
$$
\nabla l(u,v) =\left[   \begin{matrix}
\frac{\partial l}{\partial u}(u,v) \\
\frac{\partial l}{\partial v}(u,v)
\end{matrix}  \right]
$$
**Proprietà del gradiente**
- Il gradiente calcolato in *p* corrisponde ad un **vettore** che punta nella direzione di *massima crescita locale* di f in p, e ha un modulo proporzionale alla quantità di crescita in quella direzione.
- I valori delle derivate parziali in p rappresentano le componenti di questo vettore rispetto ad ogni dimensione del dominio di f()

![[Pasted image 20261113232506.png]]

Nel caso delle immagini, il gradiente è **perpendicolare** ad un eventuale edge, per questo si utilizza il gradiente per **inidividuare** gli edge.

## GRADIENTE DI UN'IMMAGINE
Per calcolare il gradiente di un'immagine si deve calcolare le derivate parziali **rispetto alle direzioni**, *orizzontali*(u) e *verticali*(v).
$$
\frac{\partial I}{\partial u}(u,v) \space and \space \frac{\partial I}{\partial v}(u,v)
$$
Per fare quest si devono utilizzare le **[[IMAGE PROCESSING#^7031|differenze]]**, rispetto alle 2 direzioni.

Il gradiente di un'immagine alla posizione (u,v) è:
$$
\nabla l(u,v) =\left[   \begin{matrix}
\frac{\partial l}{\partial u}(u,v) \\
\frac{\partial l}{\partial v}(u,v)
\end{matrix}  \right]
$$

Il **modulo** del gradiente è:
$$
M(u,v) = |\nabla I|(u,v) = \sqrt{  \left( \frac{\partial l}{\partial u}(u,v) \right)^2 + \left( \frac{\partial l}{\partial v}(u,v) \right)^2}
$$
Il modulo non varia rispetto alla direzione dell'immagine ed è usato per l'edge detection.

In alcuni casi è utile anche calcolare la direzione del gradiente:
$$
\phi(u,v) = \arctan\left( \frac{\frac{\partial l}{\partial u}(u,v)}{ \frac{\partial l}{\partial v}(u,v)}  \right)
$$
![[Pasted image 20261113233929.png]]

Per calcolare il gradiente per ogni coordinata si deve fare:
$$
\frac{\partial I}{\partial u} = \lim_{ h \to 0 } \frac{I(u+h,v) - I(u,v)}{h} \\
\frac{\partial I}{\partial v} = \lim_{ h \to 0 } \frac{I(u,v+h) - I(u,v)}{h} \\
$$
Per farlo posso utilizzare anche le differenze.
Per esempio nella **differenza cebtrata**:
$$
\frac{\partial I}{\partial u} = \frac{1}{2}(I(u+1,v)-I(u-1,v)) \\
\frac{\partial I}{\partial u} = \frac{1}{2}(I(u,v+1)-I(u,v-1))
$$
Queste derivate devono essere calcolate per **ogni pixel** dell'immagine.

La derivate parziale sono formate anche da delle funzioni lineari, che prendono in considerazione anche i pixel vicini a quello preso in esame, questo significa che èer calcolare il gradiente possiamo utilizzare anche **dei filtri lineari**(possono essere diversi per direzione),  questi filtri vengno poi applicati grazie alla *convoluzione*.

Nel caso della prima derivata parziale(*orizzontale*) si utilizzerà un **filto orizzontale**, e il kernel di questo filtro sarà:
$$
H_{u} = [-0,5 \space 0 \space 0.5] \\
\frac{\partial I}{\partial u}(u,v) =(I*H_{u})(u,v) 
$$
FILTRO per il calcolo delle derivate: [[08_Edge detection.pdf#page=30|08_Edge detection, pagina 30]]

In questo caso però il filtro sarà sensibile anche a **basse variazione di luminosità**(edge piccoli) che però vorremmo ignorare, questo si può fare grazie a filtri 2D(**UTILIZZATI SOLITAMENTE**), in modo che il risultato tenga conto di una differenza di luminosità calcolata in un’area più ampia.

Per questo si utilizzano filtri a 2 dimensioni di size 3x3.
![[Pasted image 20261113235438.png]]

**ESEMPIO SOBEL**: [[08_Edge detection.pdf#page=32|08_Edge detection, pagina 32]]

# Il Colore

Il colore nasce dalla combinazione di due fattori:
1. **Principio fisico**: propagazione, riflessione e assorbimento di onde elettromagnetiche di lunghezza d'onda variabile.
2. **Meccanismo biologico**: rilevazione da parte della retina e interpretazione del segnale da parte del cervello.

## Definizione fisica del colore

- Lo **spettro visibile** è la porzione di spettro elettromagnetico percepibile dall'occhio umano, approssimativamente fra $380\,\text{nm}$ e $720\,\text{nm}$.
- Un oggetto non possiede un colore isolato: la sua composizione chimica stabilisce quali lunghezze d'onda della luce incidente assorbe e quali riflette verso l'occhio.
- Lo **spettro di riflettanza** descrive, per ogni lunghezza d'onda, quanta luce viene riflessa da un oggetto. Può avere anche più picchi.
- Un oggetto che riflette soprattutto una banda di frequenze appare colorato; le frequenze riflesse solo in parte hanno ampiezza attenuata.
- Se tutte le lunghezze d'onda visibili sono riflesse in modo uniforme, l'oggetto appare **bianco**; se sono tutte assorbite, appare **nero**. Riflettanze uniformi ma minori producono tonalità di grigio.

## Definizione percettiva del colore

Il colore percepito dipende dai fotorecettori della retina e dall'interpretazione dei segnali che raggiungono il cervello attraverso il nervo ottico.

- **Bastoncelli**: più numerosi e diffusi; rilevano soprattutto l'intensità luminosa e permettono la visione in condizioni di bassa illuminazione, senza informazione cromatica.
- **Coni**: concentrati nella fovea; sono responsabili della visione dei colori e dei dettagli in condizioni di illuminazione elevata.

### Teoria tristimolo

I coni sono di tre tipi e hanno curve di sensibilità sovrapposte:
- **S** (*short*): maggiore sensibilità alle lunghezze d'onda corte;
- **M** (*medium*): maggiore sensibilità alle lunghezze d'onda medie;
- **L** (*long*): maggiore sensibilità alle lunghezze d'onda lunghe.

Il cervello ricava la sensazione di colore dalla combinazione delle tre risposte. Per questo L, M e S non sono tre rivelatori di rosso, verde e blu puri: ogni tipo di cono risponde a un intervallo di lunghezze d'onda.

## Proprietà del colore percepito

Un colore viene descritto mediante tre proprietà principali:
1. **Tinta** (*Hue*): identifica la sensazione cromatica dominante, ad esempio rosso o verde.
2. **Saturazione** (*Saturation*): indica quanto il colore è puro; diminuisce quando il colore si avvicina al grigio.
3. **Luminosità** (*Brightness/Lightness*): indica quanto il colore appare chiaro o scuro; dipende sia dall'energia riflessa sia dalla sensibilità spettrale dell'occhio.

## Rappresentazione digitale e conversione

Un'immagine a colori associa a ogni pixel un vettore a tre componenti, per esempio $I(u,v)=[R,G,B]$. I tre canali sono quindi una rappresentazione tridimensionale del colore, scelta per approssimare la visione tristimolo umana.

Per convertire un'immagine RGB in scala di grigio, non si usa una media semplice se si vuole preservare la percezione della luminosità. Si utilizza una **media pesata**:
$$Gray = 0.299 \cdot R + 0.587 \cdot G + 0.114 \cdot B$$
Il peso del verde è maggiore di quello del blu perché l'occhio umano è più sensibile alle lunghezze d'onda verdi.

## SPAZI DI COLORE

La percezione tristimolo suggerisce di rappresentare ogni colore con **tre componenti**. Uno spazio di colore è un sistema di coordinate tridimensionale: ogni asse rappresenta una componente e ogni punto corrisponde a un colore.

Gli spazi differiscono per il modo in cui definiscono queste componenti e per l'applicazione a cui sono destinati. In generale, gli spazi **additivi** sono usati per dispositivi che emettono luce, mentre quelli **sottrattivi** sono usati per la stampa.

## Spazio RGB

RGB (*Red, Green, Blue*) è uno spazio **additivo**, usato da schermi e display. Ogni pixel combina le intensità di luce rossa, verde e blu.

- I valori sono spesso codificati tra 0 e 255; in forma normalizzata appartengono a $[0,1]$.
- $(0,0,0)$ rappresenta il nero, mentre $(1,1,1)$ rappresenta il bianco.
- Valori uguali nei tre canali producono grigi: questi colori si trovano sulla diagonale del cubo RGB che unisce nero e bianco.
- La combinazione dei massimi di due canali produce i colori secondari: rosso + verde = giallo, verde + blu = ciano, blu + rosso = magenta.

Le componenti possono essere elaborate separatamente, per esempio applicando un operatore puntuale a ciascun canale. Per rilevare gli edge si converte spesso l'immagine in scala di grigio, perché gli edge sono associati a variazioni della luminosità complessiva.

## Spazio CMY

CMY (*Cyan, Magenta, Yellow*) è uno spazio **sottrattivo**, usato soprattutto per la stampa. I valori indicano la quantità di pigmento da depositare: i pigmenti assorbono parte della luce incidente e riflettono il resto.

Con valori RGB e CMY normalizzati in $[0,1]$, la conversione è:
$$
C=1-R,\qquad M=1-G,\qquad Y=1-B
$$
Per esempio, il blu RGB $(0,0,1)$ corrisponde a CMY $(1,1,0)$: ciano e magenta assorbono rispettivamente rosso e verde, lasciando riflettere il blu. Nella stampa si aggiunge spesso il nero come quarto inchiostro, ottenendo CMYK.

## Spazi HSL e HSV

HSL (*Hue, Saturation, Lightness*) e HSV (*Hue, Saturation, Value*) descrivono il colore con parametri più vicini al modo in cui lo nominiamo e lo regoliamo:

- **H (Hue, tinta)**: posizione angolare della tinta; $0^\circ$ corrisponde al rosso.
- **S (Saturation, saturazione)**: distanza dall'asse dei grigi; $0$ indica un colore acromatico, mentre valori maggiori indicano una tinta più satura.
- **L (Lightness)** in HSL oppure **V (Value)** in HSV: coordinata che descrive la componente chiara/scura.

Si possono visualizzare come trasformazioni geometriche del cubo RGB. In HSL la diagonale nero-bianco diventa l'asse della luminosità e le tinte si dispongono attorno a esso; HSV ne rappresenta la metà superiore, con il nero al vertice inferiore. HSL e HSV sono ancora spazi derivati da RGB e non sono uniformemente percettivi.

## Conversioni con OpenCV

OpenCV usa normalmente l'ordine dei canali **BGR** per le immagini a colori. Le conversioni in HLS/HSV richiedono quindi di specificare il codice corretto:

```python
import cv2

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

## Uniformità percettiva

In uno spazio **uniformemente percettivo**, la distanza tra due punti dovrebbe essere proporzionale alla differenza di colore percepita. RGB, CMY, HSL e HSV non soddisfano bene questa proprietà: la stessa distanza numerica può corrispondere a differenze visive diverse. CIELAB è uno spazio approssimativamente uniforme percettivamente e permette di confrontare i colori usando la distanza tra i punti.

[[09_Colore.pdf#page=18|09_Colore, spazi di colore]]

# TRASFORMATA DI FOURIER
Le immagine fino ad ora le abbiamo viste come matrici, definite dal valore di 2 funzioni, dove vengono contenuti i valori del pixel, queso tipo di rappresentazione viene nominata nel **dominio spaziale** a 2 dimensioni.

Però le immagini possono essere rappresentate anche nel **dominio delle frequenze**, dove alcune operazioni di manipolazione dell immagini diventano più semplici, da effetture.

## Idea base
La trasformata di fourier permette di esprimere una qualsiasi funzione $f()$ come combinazione lienare di una **base di funzioni**.

Le funzioni base sono delle **sinusoidi**, e l'output della trasfromata sono i *coefficienti* della combinazione lineare.

[[11_Trasformata di fourie_I.pdf#page=11|11_Trasformata di fourie_I, pagina 11]]

---
## Tecniche spettrali
Per trasformare segnali audio, immagini, video ecc... dal dominio temporale al dominio delle frequenze è possibile utilizzare diverse trasformazioni, tra loro simili:

- **Fourier Tarsform**
- **Discrete Fourier Transform (DFT),**
- **Discrete Cosine Transform (DCT)**

Una sinusoide viene definita da **tre grandezze principali**:
- **Lunghezza d'onda** $\to$ inversa della frequenza
- **Ampiezza**
- **Fase**

### Concetti matematici
Formula di eulero:
$$
e^{i\rho} = \cos \rho + i \sin \rho
$$
Numeri complessi espressi in coordinate polari:
$$
z = re^{i\rho} = r(\cos \rho + i \sin \rho)
$$
Dove $r$ è il modulo:

$$
r = |z| = \sqrt{ x^2 +y^2}
$$

[[11_Trasformata di fourie_I.pdf#page=21|11_Trasformata di fourie_I, pagina 21]]

## Serie di Fourier
Quasi tutte le funzioni periodiche possono essere rappresentate come una sommatoria infinita di sinusoidi, detta **serie di Fourier**:

$$
serie di fourie
$$

Però se una funzione non è periodica si può prendere in esame un periodo finito, e replicare questo periodo all'infinito.

## Trasformata di Fourier
La trasformata di fourier **estende la serie di fourier a qualsiasi funzione**, comprese anche quelle definifite in un intervallo finito di tempo, questo si può fare anche utilizzando la formula di eulero.

(Formule latex della trasformata di fourier, anche con la formula di eulero data dalle slide)

In entrami i casi $F()$ è definita per $\mu appartiente R$.
La variabile $\mu$ indica una **frequenza continua**.

(Formula di F in funzione di mu)

La funzione $F(\mu)$ solitamente è una **funzione complessa**, **periodica**, dove il suo modulo $|F(\mu)|$ **è il suo spettro**.

Se si ha solo la funzione $F(\mu)$ si può ricavare la funzione $f(t)$ tramite la **trasformata inversa**.

(Formule trasformata inversa, anche eulero)


## Discrete Fourier Transform



## Teorema della convulozione
Siano $f()$ ed $h$ 2 funzioni ed $F$ ed $H$ le corrispondenti **Trasformate di Fourier** con:
$$
F= \mathcal{F}(f),H=\mathcal{F}(h)
$$
Allora la Trasformata di Fourier della convoluzione tra f ed h è uguale al prodotto elemento per elemento tra F ed H (Convolution Theorem:
(corrispondente formula)


## Convuluzione tramite DFT


### Filtro passa basso
Mantiene tutte le frequenze al di sotto di una data frequenza, per eliminare le frequenza più alte, producendo un effetto simile al **blurring**.

Un filtro passa basso ideale è una **maschera** binaria NxM:
![[Pasted image 20261126114348.png]]
La maschera è applicata su F e non sull'immagine di partenza.

### Filtro passa alto
Filtro che mantiene tutte le frequenze più alte di una certa frequenza, questo è l'**inverso del fitro passa-basso**.


### Filtro gaussiano
Filtro che permette un graduale passaggio da un valore basso ad un valore alto, spesso utilizzato per smussare i questo tipi di passaggi per essere applicato assieme ad altri filtri.
Utilizzato anche per comprimere il segnale.


### Filtro Butterworth

### Filtri selettivi
Utilizzati per mascherare solo alcune frequenze specifiche, questi filtri sono:
- **bandpass e bandreject filter** 
- **notch reject e notch pass filter**


## Vantaggi dei filtri tramite frequenze
IL [[IMAGE PROCESSING#Teorema della convulozione|Teorema della convulozione]] dice che esiste un **filtro spaziale, il quale dà come risultato lo stesso di un filtro nel dominio delle frequenze**, però questo solo **teoricamente**, però  non è semplice trovare un filtro spaziale tale che dia lo stesso risultato di un filtro in frequenza, un esempio di questi filtri sono quelli **selettivi**.
