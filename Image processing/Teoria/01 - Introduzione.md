# Introduzione all'Image Processing

> **Slide:** [[01_Introduzione.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

Un'immagine è una **funzione multidimensionale** del tipo
$$
I(u,v)\in \mathbb{R}, \quad u,v\in \mathbb{N}
$$
Come una funzione a 2 variabili che restituisce **valori d'intensità**.

Questa funzione può avere un output dato da un unico valore (scalare) che viene detto **intensità o livello di grigio**.
Può dare anche **valori vettoriali**, come nel caso della terna **(RGB)**.

## Immagini a colori
![[Pasted image 20260917104646.png]]
- $A, L$ sono altezza e larghezza
- Per ogni pixel corrispondono 3 valori numerici
- In questo caso la funzione sarà:
$$
I \in \mathbb{R}^{3}, \quad u,v\in \mathbb{N}
$$
- Un'immagine di questo tipo è detta a **3 canali**
- Ogni canale è rappresentato da una matrice e l'insieme delle 3 matrici è detto "tensore"

## Immagini
Ogni immagine è composta da un numero finito di elementi detti **pixel**, i quali hanno una posizione finita e un **proprio valore**.
Quando sia le coordinate che i valori restituiti dalla funzione sono discreti e finiti diciamo che l'immagine è **digitale**.
Es. La funzione che rappresenta un'immagine in scala di grigi è data da:
$$
I:\{1\dots L\} \times \{1\dots A\} \to \{0\dots 255\}
$$

## Image Processing
Sono algoritmi che hanno in **input un'immagine** e ne **restituiscono un'altra**, questo si fa per:
- Image display and printing
- Image editing
- Image enhancement
- Image restoration
- Image compression
Oppure estrarre da queste immagini informazioni utili.
[[01_Introduzione.pdf#page=12|01_Introduzione, pagina 12]]

Anche se queste operazioni possono essere eseguite da un'IA, quest'ultima ha comunque bisogno di **grandi potenze di calcolo** e anche grossi insiemi di dati per l'addestramento.

Questo tipo di algoritmi vengono utilizzati in caso:
- Impossibilità di utilizzo della GPU
- Non si ha abbastanza dati per addestrare l'IA
- L'elaborazione deve avvenire in Real Time

### Per cosa si può usare?
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

---
> **Collegamenti Lab:** [[IMAGE FORMATION]]
