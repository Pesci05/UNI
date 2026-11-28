# Immagini Digitali

> **Slide:** [[02_Immagini_Digitali.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

Le immagini sono formate dalla radiazione elettromagnetica (EM), come:
- Luce
- Raggi X
- Onde radio
- Etc...

Lo spettro EM è l'insieme di tutte le possibili frequenze della radiazione elettromagnetica.
Lo spettro è diviso in base alle lunghezze d'onda.
Nel caso della luce si può suddividere in base alla luce visibile dall'occhio umano:
![[Pasted image 20260917112926.png]]

La relazione tra la **lunghezza d'onda** della radiazione ($\lambda$) e la sua frequenza ($\nu$) è data da:
$$
\lambda=\frac{c}{\nu}
$$
$c$ = la velocità della luce.
La lunghezza d'onda si misura in metri.

I colori percepiti dagli esseri umani sono determinati dalla **lunghezza d'onda** della luce che viene riflessa da un oggetto.

Le immagini normalmente vengono acquisite tramite la **rifrazione della luce**, ma esistono anche altre tipologie di acquisizione attraverso altri tipi di onde come:
- Immagini radar (onde radio e microonde)
- Risonanza magnetica (onde radio)
- Imaging a microonde
- Imaging a infrarossi
- Fotografie
- Telescopi per l'imaging ultravioletto
- Raggi X e tomografia computerizzata
- Tomografia a emissione di positroni (raggi gamma)
- Ultrasuoni (onde sonore, non EM, con una frequenza maggiore di 20 kHz)

## Occhio Umano
![[Pasted image 20261127192732.png]]
L'occhio umano è formato da:
- **Cristallino/lente**: proietta la luce degli oggetti sulla retina
- **Retina**: ricoperta di cellule nervose sensibili alla luce chiamate **fotoricettori**, che sono **coni** e **bastoncelli**
- **Coni**: si concentrano in una zona della retina chiamata **fovea**, sensibili al colore
- **Bastoncelli**: sono diffusi su tutta la retina, non sono sensibili al colore, ma sensibili alle diverse intensità di luce.

I muscoli dell'occhio possono cambiare la forma del cristallino, permettendo di **concentrarsi/focus** su oggetti vicini o lontani.

L'**immagine viene messa a fuoco dalla retina**, le **terminazioni nervose presenti vengono eccitate e mandano segnali al cervello**; l'occhio umano può percepire fino a $10^{10}$ intensità di luminosità.

## Acquisizione delle Immagini
> Approfondimento lato hardware/ottica: [[IMAGE FORMATION#Da immagine continua a digitale]] e [[IMAGE FORMATION#Sensore (Spatial integration and sampling)]]

Le immagini sono in genere acquisite illuminando una scena e catturando l'energia riflessa dagli oggetti della scena.

L'energia in ingresso (ad esempio la luce) colpisce un materiale reattivo a quel tipo di energia, generando una tensione.

Le risposte dei sensori determinano l'immagine finale.
![[Pasted image 20260917114618.png]]

È impossibile acquisire le immagini in modo continuo, per questo si esegue un tipo di **campionamento spaziale**, che permette di avere un'immagine discreta in corrispondenza delle coordinate discrete $(u,v)$.

Questo vale anche per l'acquisizione dell'immagine nel tempo, per questo si esegue un **campionamento temporale**, a intervalli discreti (vedi anche [[IMAGE FORMATION#Integrazione temporale (Temporal integration and sampling)]]).

**CAMPIONARE UN SEGNALE** significa misurarlo in posizioni e tempi discreti.

Anche i valori d'**intensità** devono essere **discreti e limitati**: la **quantizzazione** è il processo di conversione di un segnale analogico continuo nella sua rappresentazione digitale. L'immagine è pertanto composta di valori quantizzati, e può assumere solo un numero finito di valori.
![[Pasted image 20260917115211.png]]

Un'immagine può essere rappresentata come funzione discreta, grazie ai meccanismi di quantizzazione e campionamento, e la funzione sarà:
$$
I:\{1\dots L\} \times \{1\dots A\} \to \{0\dots K-1\}
$$

## Rappresentazione delle Immagini
La struttura dati utilizzata per rappresentare le immagini a livello di grigio è una matrice 2D che contiene il valore dei pixel.
Il sistema di coordinate $(u,v)$ dei pixel normalmente parte dal primo pixel in alto a sinistra (vedi [[IMAGE FORMATION#OpenCV: frame come array NumPy]]).
I valori della matrice possono essere espressi in qualsiasi tipo di dati.
![[Pasted image 20260917115844.png]]

La **risoluzione spaziale** è determinata dal modo in cui è stato eseguito il campionamento: un campionamento fine produce una maggiore risoluzione spaziale.
La risoluzione spaziale è data dal più piccolo dettaglio dell'immagine distinguibile:
- Una telecamera digitale ha una "risoluzione" che dipende dal numero di pixel
- Nella stampa la risoluzione è espressa in punti per pollice (DPI)

**Saturazione**: dovuta al massimo livello di intensità rappresentabile (vedi [[IMAGE FORMATION#Full well capacity]]).
**Rumore**: dovuto al processo di acquisizione e/o di memorizzazione (vedi [[06 - Rumore e Filtri Non Lineari]] e [[IMAGE FORMATION#Sorgenti di rumore]]).
