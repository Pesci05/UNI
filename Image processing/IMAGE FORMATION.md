
# Rifrazione e lenti sottili

La **rifrazione** avviene ogni volta che la luce attraversa il confine tra due mezzi con **indici di rifrazione** diversi.
- In una lente standard avviene **due volte**: quando il raggio entra nella lente e quando esce.
- Nel modello di **lente sottile** (*thin lens*), si approssima la deviazione complessiva come una **singola deviazione** al centro della lente.
![[Pasted image 20261119172637.png]]
## Convessità e densità
- Il caso più comune è una lente **biconvessa** immersa in un mezzo meno denso (es. aria): si osserva un comportamento **convergente** (i raggi paralleli all'asse ottico si incontrano dopo la lente).
- Una lente **biconcava** in aria ha invece un comportamento **divergente**.
![[Pasted image 20261119172825.png|342]]
- La convergenza dipende anche dalla **densità ottica** relativa: se il mezzo esterno è otticamente più denso della lente, si osserva il comportamento opposto.
![[Pasted image 20261119172841.png|380]]

## Legge di Snell
La legge di Snell descrive come si piega la luce:
$$
n_{\text{air}} \sin\theta_{\text{air}} = n_{\text{glass}} \sin\theta_{\text{glass}}
$$
dove gli angoli sono misurati rispetto alla **normale** alla superficie.
- Se il raggio entra in un mezzo otticamente più denso ($n_{\text{glass}} > n_{\text{air}}$), l'angolo diminuisce ($\theta_{\text{glass}} < \theta_{\text{air}}$), e viceversa.
![[Pasted image 20261119175157.png]]

Su **superfici sferiche**, assumendo:
1. lente sferica,
2. oggetto a distanza infinita ($d \to \infty$, raggi paralleli),
3. angoli piccoli ($h$ piccolo, $\sin\theta \approx \tan\theta \approx \theta$),

si ottiene il punto $x$ in cui il raggio incontra l'asse ottico:
$$
x = \frac{n_2}{n_2 - n_1} R
$$
Poiché $x$ **non dipende da $h$**, tutti i raggi paralleli convergono nello stesso punto.
![[Pasted image 20261119175313.png]]
## Equazione del costruttore di lenti (Lens maker equation)
Applicando la legge di Snell due volte (entrata e uscita), si mette in relazione la forma della lente con il punto focale $f$:
$$
\frac{1}{f} = \left(\frac{n_{\text{glass}}}{n_{\text{air}}} - 1\right)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)
$$
- Cambiando la curvatura della lente ($R_1, R_2$) si cambia la lunghezza focale $f$.
![[Pasted image 20261119175413.png]]
## Distanza focale (Focal length)
Ogni lente convergente ha un **punto focale** $F$ su entrambi i lati, a distanza $f$ (**lunghezza focale**), dove convergono i raggi paralleli all'asse ottico.
Per tracciare l'immagine di un oggetto si usano **3 raggi speciali**:
1. Il raggio **parallelo** all'asse ottico $\rightarrow$ passa per il fuoco $F$ dopo la lente.
2. Il raggio che **passa per il fuoco** $F$ $\rightarrow$ esce parallelo all'asse ottico.
3. Il raggio che **passa per il centro** della lente $\rightarrow$ prosegue dritto senza deviazioni (approssimazione di lente sottile).
![[Pasted image 20261119175544.png]]
La distanza focale di una lente descrive come gli oggetti del **mondo reale**(sinistra della lente), vengono trasformati nel **mondo delle immagini**(destra della lente).
## Equazione delle lenti sottili (Thin lens equation)
I 3 raggi speciali si incontrano nello stesso punto a distanza $d_i$ dalla lente (**piano dell'immagine**). La distanza dell'oggetto $d_o$, la distanza dell'immagine $d_i$ e la lunghezza focale $f$ sono legate da:
$$
\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}
$$
Da questa equazione derivano due effetti: **zoom** e **focus**.

## Ingrandimento (Magnification) e Zoom
L'ingrandimento è dato da:
$$
m = -\frac{d_i}{d_o}
$$
- A parità di $d_o$, **aumentare $f$** fa aumentare $d_i$ $\rightarrow$ effetto **zoom in**.
- A parità di $d_o$, **diminuire $f$** fa diminuire $d_i$ $\rightarrow$ effetto **zoom out**.
- Nelle fotocamere consumer si cambia lo zoom modificando la configurazione relativa delle lenti; nei setup industriali si sceglie invece direttamente la lente con la focale adatta.
![[Pasted image 20261120163218.png]]
## Messa a fuoco (Focusing)
La lunghezza focale vincola $d_o$ e $d_i$: con una lente biconvessa standard **non tutto può essere a fuoco contemporaneamente**, Se:
- **Aumentiamo $d_i$**, $d_o$ diminuisce $\rightarrow$ si mette a fuoco **più vicino** alla lente.
- **Diminuiamo $d_i$**, $d_o$ aumenta $\rightarrow$ si mette a fuoco **più lontano** dalla lente.
![[Pasted image 20261120171134.png]]
## Maximum field angle
La lunghezza focale influenza anche il **maximum field angle** $\theta_{\max}$ (legato al cerchio d'immagine $D_{ic}$):
$$
\theta_{\max} = 2\arctan\left(\frac{D_{ic}}{2d_i}\right)
$$
- A parità di $D_{ic}$, **aumentare $f$** (quindi $d_i$) **restringe** il maximum field angle (zoom in, meno scena inquadrata), e viceversa.
![[Pasted image 20261120171929.png|301]]
# APERTURE
L'apertura (o **diaframma**) **limita** il cono di luce che passa attraverso la lente e raggiunge il piano dell'immagine.
- **Primo effetto**: si può **controllare la luminosità** dell'immagine (meno raggi $\rightarrow$ immagine più scura).
- Nel modello ideale di lente sottile, l'apertura **non influenza** il maximum field angle.
- Viene espressa tramite l'**f-number**:
$$
N = \frac{f}{D}
$$
dove $D$ è il diametro della pupilla/apertura. Gli **f-stops** variano tipicamente a passi di $\sqrt{2}$: aumentare $N$ di un fattore $\sqrt{2}$ **dimezza** l'irradianza, diminuirlo di $\sqrt{2}$ la **raddoppia**.
![[Pasted image 20261120174617.png]]
![[Pasted image 20261120174628.png]]
## Depth of focus
- **Secondo effetto** di un'apertura più piccola: i raggi divergono più lentamente lontano dal piano dell'immagine ($d_i$).
- Quando un punto è fuori fuoco, la luce non converge in un punto ma in un disco chiamato **circle of confusion (CoC)**.
- La **depth of focus** è l'intervallo nello spazio immagine in cui il diametro della sfocatura rimane sotto una soglia accettabile di CoC.
- Aumenta con aperture più piccole e quando si mette a fuoco **più vicino** alla lente ($d_i$ più grande).
![[Pasted image 20261120230256.png|291]]

## Depth of field
- È l'intervallo attorno a $d_o$ nello spazio oggetto in cui la luce converge in un CoC accettabile.
- Aumenta con aperture più piccole e quando si mette a fuoco **più lontano** dalla lente ($d_o$ più grande).
- Depth of focus e depth of field sono due facce della stessa medaglia, legate dall'equazione delle lenti sottili.
![[Pasted image 20261120235136.png|277]]

## Diffrazione e Airy disk
- Ridurre l'apertura all'infinito non produce un'immagine perfetta a causa della **diffrazione** (diffusione dell'onda luminosa attraverso un'apertura finita).
- L'interferenza dei raggi crea l'**Airy disk**, che rappresenta il limite fisico di nitidezza del sistema ottico:
$$
d_{\text{Airy}} = 2.44\,\lambda\,N
$$
- Gli effetti della diffrazione e della depth of focus/field si combinano insieme.

# DA IMMAGINE CONTINUA A DIGITALE
Per passare da un'immagine reale ad una digitale serve un **sensore**. Un pixel è una misura **foton-to-charge** su un'area finita, in un tempo finito, pesata spettralmente, con capacità finita e rumore.

## SENSORE (Spatial integration and sampling)
Il sensore viene raffigurato da un **rettangolo**, diviso in **pixel**, che permettono di definire tre grandezze:
- **Risoluzione** ($N_x / N_y$, numero di pixel)
- **Grandezza dei pixel** ($p_x / p_y$, di solito $p_x = p_y$)
- **Grandezza del sensore** ($W / H$)

Solo due sono indipendenti:
$$
W = N_x \cdot p_x \quad H = N_y \cdot p_y
$$
Ogni pixel **media** (integra) l'irradianza che raccoglie sulla sua area. Avere più pixel può significare due cose:
- un **sensore più grande** (cattura più scena a parità di dettaglio),
- **pixel più piccoli** (cattura la stessa scena con maggior dettaglio).

## FIELD OF VIEW
Il **[[IMAGE FORMATION#maximum field angle|maximum field angle]]** è una proprietà della lente (cerchio d'immagine $D_{ic}$ e distanza $d_i$).
Il **Field of View (FOV)** effettivo è invece determinato dalla combinazione di **lente + sensore**, in base alla **diagonale** del sensore rispetto al cerchio d'immagine:
- **Minore del cerchio d'immagine**: il sensore è del tutto all'interno del cerchio $\rightarrow$ zona ideale.
- **Maggiore o uguale al cerchio d'immagine**: il sensore sborda $\rightarrow$ effetti di **vignettamento** e **spreco delle dimensioni del sensore**.

Il FOV orizzontale si calcola come:
$$
\text{FOV}_H = 2\arctan\left( \frac{W}{2d_i} \right)
$$
*(In pratica si assume spesso messa a fuoco all'infinito, cioè $f = d_i$).*
![[Pasted image 20261122233413.png]]
## PIXEL DENSITY
Viene definita dal rapporto **mm/px** (o **px/mm**) per collegare le dimensioni in pixel nell'immagine alle dimensioni reali. Si può stimare in due modi:
1. **Magnification law**:
$$
|m| = \frac{d_i}{d_o} = \frac{h_i}{h_o} \qquad \text{mm/px} = \frac{|m|}{\text{pixel size}}
$$
2. **Misura diretta**: contando i pixel di un oggetto di dimensioni reali note.

In entrambi i casi la relazione **mm/px** vale solo alla distanza $d_o$ specifica (spesso fissa).

### Pixel density: più alta è meglio?
- **NO**: se la sfocatura ottica (CoC, *Airy disk*, aberrazioni) copre già molti pixel (*optic limited*), aumentare i pixel non aggiunge dettaglio utile.
- **SÌ** (fino a un certo punto): per il **teorema di Nyquist**, i dettagli periodici vanno campionati ad almeno **2× la loro frequenza** (2 pixel per periodo è già un limite inferiore rischioso). Sotto questa soglia si verifica **aliasing** (*alias prone*): non si perdono solo dettagli, ma si generano **dettagli falsi** (es. effetto *Moiré*).
- **Bilancio ideale**: ottica e sensore devono corrispondere, in modo che più campioni rappresentino il dettaglio più piccolo utile.

## INTEGRAZIONE TEMPORALE (Temporal integration and sampling)
Un pixel non raccoglie la luminosità istantaneamente, ma la accumula durante il **tempo d'esposizione** (*exposure time*):
$$
N_{\text{photons}} \propto \text{irradiance} \cdot \text{pixel area} \cdot \text{exposure time}
$$
Per avere un'immagine più luminosa si può:
- aumentare l'illuminazione,
- aumentare l'apertura (meno *depth of field*),
- usare un sensore con pixel più grandi,
- aumentare l'**exposure time** (rischio di **motion blur**).

### Exposure time vs Frame rate
- L'**exposure time** definisce **per quanto tempo** si osserva l'oggetto durante una misurazione.
- Il **frame rate** definisce **quanto spesso** si effettua la misurazione.
- Poiché non si può iniziare una misura prima di aver finito la precedente:
$$
\text{exposure time} < \frac{1}{\text{frame rate}}
$$
- Se la scena è ferma il frame rate non è critico; se l'oggetto si muove, anche il campionamento temporale può produrre **aliasing**.

## SHUTTER TYPE
- **Global shutter**: tutte le righe di pixel condividono lo stesso intervallo di integrazione.
- **Rolling shutter**: le righe vengono integrate e lette sequenzialmente una alla volta. È più economico ma introduce **artefatti** (non risolvibili accorciando l'esposizione, perché resta lo sfasamento temporale tra righe):
  - strutture verticali storte (moto parallelo),
  - oggetti compressi o stirati (moto incidente),
  - effetto *wobble* durante la rotazione della camera,
  - **bande** sotto illuminazione modulata nel tempo.

## RADIOMETRICA, QUANTIZZAZIONE E RUMORE
Non tutti i fotoni contribuiscono all'immagine: esiste una probabilità, detta **quantum efficiency**, che un fotone rilasci un **elettrone** (dipende dalla lunghezza d'onda).

### Full well capacity
Un pixel **non è un contenitore infinito**: la **full well capacity** è il numero massimo di elettroni accumulabili. Superandola, il pixel **satura** e si perdono informazioni sulle alte luci (motivo per cui non si può alzare l'esposizione all'infinito anche su scene ferme).

### Da elettroni a numeri (catena CMOS)
1. **Fotoni $\rightarrow$ Elettroni** (quantum efficiency).
2. **Elettroni $\rightarrow$ Tensione** (proporzionale tramite *sensing node*).
3. **Gain analogico** (amplificatore, equivalente all'**ISO** nelle fotocamere consumer).
4. **ADC (Quantizzazione)**: discretizza la tensione in base alla *bit depth* del sensore (es. 0–255 a 8 bit, 0–1023 a 10 bit, 0–4095 a 12 bit, 0–65535 a 16 bit).

### Sorgenti di rumore
Il rumore impedisce di ottenere due immagini identiche:
- **Shot noise**: legato al segnale dei fotoni (distribuzione di Poisson, varianza cresce col segnale).
- **Dark-current noise**: elettroni generati termicamente (cresce con tempo e temperatura).
- **Read noise**: introdotto durante la lettura della carica (rilevante a basso segnale).
- **Quantization noise**: introdotto dai passi finiti dell'ADC.

$$
\text{SNR} = \frac{\text{mean signal}}{\text{noise standard deviation}}
$$

### Exposure vs Gain
A parità di luminosità finale:
- **Esposizione corta + Gain alto**: pochi elettroni e **SNR bassa** (domina il *read noise* amplificato).
- **Esposizione più lunga + Gain basso**: più elettroni raccolti e **SNR migliore** (preferibile, evitando saturazione e *motion blur*).

## SELEZIONE SPETTRALE (Spectral selection)
- La **luce visibile** è compresa tra **380 e 740 nm**.
- I sensori al silicio sono sensibili fino a **1000–1100 nm** (vicino infrarosso): si usa spesso un filtro **IR-cut** tra lente e sensore per evitare contaminazioni. (Le termocamere usano invece sensori e ottiche diverse per il lontano infrarosso).
- **Camera monocromatica**: mescola tutte le lunghezze d'onda in un'unica misura di luminosità.
- **Camera RGB (Bayer pattern)**: filtra le bande R, G, B prima del sensore; ogni pixel misura un solo colore e gli altri vengono **interpolati**. Il **verde** è campionato con densità doppia perché contribuisce molto alla luminanza percepita. I filtri riducono la *quantum efficiency*, quindi per massimo conteggio di fotoni e dettagli reali (non interpolati) si preferisce una camera monocromatica.



# COME ACQUISIRE UN'IMMAGINE
Per acquisire un'immagine il componenete più importante è la **telecamera**, però per elaborarla servono un certo tipo di algortmi, nel nostro caso utilizzaeremo **OPENCV**.

Per acquisire un frame tranite numpy si deve:
```Python
ok, frame = cap.read()

print(farme.shape)
print(frame.dtype)

blue, green, red = frame[r,c]
```

Very important things to know from day 1: 
- **Origin**: top left (pointing right and down) 
- **Indexing**: frame[r, c] 0-based 
- **Channel order**: BGR (not RGB) 
- **Typical range**: 0-255

Per lavorare in float per operazioni custom:

```python
rame_float = frame.astype(np.float32) / 255 
To go back to uint8 for opencv methods: 
frame = np.clip(frame_float * 255, 0, 255).astype(np.uint8)
```

Ogni telecamera può avere un SDK proprietario, molto spesso se si cambia telecamera si deve anche cambiare il codice.

**UVC = USB Video Class**

Una camera UVC può descrivere:
- Risoluzione e frame rates
- Pixel o formati compressi
- Comandi cdi controllo della camera e come impostarle
- available video streams;


# LOOKING FOR OBJECTS
## LABELING
Ha come input un'immagine binaria,e come output un'immagine **assegnando un'etichetta**, ad ogni pixel.

Alternativa al **find countours**.
La differenza più grande sono le informazioni date, Find countour ci dà più informazioni.

Per un pixel di **foreground**, possiamo definire i pixel che lo circondano.
$$
N_{4} = {(x-1,y),(x+1,y),(x,y-1),(x,y+1)} \\
N_{8} = N_{4} u
$$

Il suo algoritmo funziona:
1. **Passi l'immagine binaria e ispeziona tutti i pixel vicini**
	- Assegna una uova label quando i vicini non hanno ancora una label assegnata
	- Riusare una label quando è presenta solo una label
	- Segnare quando avviene un'equivalenza temporanea nel momento in cui si incontrano 2 label diverse
2. **Rimpiazzare le equivalenze temporanee** con una label che include tutti i pixel

```python
count, labels, stats, centroids =
	cv2.connectedComponentsWithStats(
	mask,
	connectivity = 4,
	)
```
- labels $[x,y]$: componente intero che **identifica ogni pixel**.
- stats $[i]$: LEFT,TOP,WIDTH, HEIGHT, and AREA, per la lable i.

Per aver assegnata una label la regione di pixel deve avere:
- Un'**area plausibile**
- Un centroid all'interno della regione ispezionata.
Per risolvere dei problemi su delle immagini, si può risolvere tramite le **conoscenze a priori** riguardo il problema stesso.
## TEMPLATE MATCHING

