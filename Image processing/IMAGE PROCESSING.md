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