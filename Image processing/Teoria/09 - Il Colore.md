# Il Colore

> **Slide:** [[09_Colore.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

Il colore nasce dalla combinazione di due fattori:
1. **Principio fisico**: propagazione, riflessione e assorbimento di onde elettromagnetiche di lunghezza d'onda variabile.
2. **Meccanismo biologico**: rilevazione da parte della retina e interpretazione del segnale da parte del cervello.

## Definizione fisica del colore

- Lo **spettro visibile** è la porzione di spettro elettromagnetico percepibile dall'occhio umano, approssimativamente fra $380\,\text{nm}$ e $720\,\text{nm}$ (vedi anche [[02 - Immagini Digitali]]).
- Un oggetto non possiede un colore isolato: la sua composizione chimica stabilisce quali lunghezze d'onda della luce incidente assorbe e quali riflette verso l'occhio.
- Lo **spettro di riflettanza** descrive, per ogni lunghezza d'onda, quanta luce viene riflessa da un oggetto. Può avere anche più picchi.
- Un oggetto che riflette soprattutto una banda di frequenze appare colorato; le frequenze riflesse solo in parte hanno ampiezza attenuata.
- Se tutte le lunghezze d'onda visibili sono riflesse in modo uniforme, l'oggetto appare **bianco**; se sono tutte assorbite, appare **nero**. Riflettanze uniformi ma minori producono tonalità di grigio.

## Definizione percettiva del colore

Il colore percepito dipende dai fotorecettori della retina e dall'interpretazione dei segnali che raggiungono il cervello attraverso il nervo ottico (vedi [[02 - Immagini Digitali#Occhio Umano]]).

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

Un'immagine a colori associa a ogni pixel un vettore a tre componenti, per esempio $I(u,v)=[R,G,B]$ (per l'acquisizione tramite sensore Bayer vedi [[IMAGE FORMATION#Selezione spettrale (Spectral selection)]]). I tre canali sono quindi una rappresentazione tridimensionale del colore, scelta per approssimare la visione tristimolo umana.

Per convertire un'immagine RGB in scala di grigio, non si usa una media semplice se si vuole preservare la percezione della luminosità. Si utilizza una **media pesata**:
$$Gray = 0.299 \cdot R + 0.587 \cdot G + 0.114 \cdot B$$
Il peso del verde è maggiore di quello del blu perché l'occhio umano è più sensibile alle lunghezze d'onda verdi.

## Spazi di Colore

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

OpenCV usa normalmente l'ordine dei canali **BGR** per le immagini a colori (vedi [[IMAGE FORMATION#OpenCV: frame come array NumPy]]). Le conversioni in HLS/HSV richiedono quindi di specificare il codice corretto:

```python
import cv2

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

## Uniformità percettiva

In uno spazio **uniformemente percettivo**, la distanza tra due punti dovrebbe essere proporzionale alla differenza di colore percepita. RGB, CMY, HSL e HSV non soddisfano bene questa proprietà: la stessa distanza numerica può corrispondere a differenze visive diverse. CIELAB è uno spazio approssimativamente uniforme percettivamente e permette di confrontare i colori usando la distanza tra i punti.

[[09_Colore.pdf#page=18|09_Colore, spazi di colore]]
