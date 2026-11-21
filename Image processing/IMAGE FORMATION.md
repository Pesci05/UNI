
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
Per passare da un'immagine reale ad una digitale serve un **sensore**.

## SENSORE
Il sensore viene raffigurato da un **rettangolo**, il quale viene diviso in **pixel**, questi permettoni di definire:
- **RISOLUZIONE**
- **La grandezza dei pixel**
- **Grandezza del sensore**
Ogni pixel contiene la media dell'informazione che riceve.

Il numero dei pixel può influire su:
- **FIELD OF VIEW**

## FIELD OF VIEW
Il FOV è collegato alla **maximum field view**, il quale è una proprietà della lente, e questo sarà un cerchio grazie alla forma della lente.
Invece il **Field of view** invece è definito si dalla lente ma anche dal **sensore**, infatti la sua grandezza sarà dettata dalla **diagonale** del sensore:
- **MINORE**
	Con la diagonale minore, significa che il sensore sarà del tutto all'interno del MAXIMUM FIELD VIEW, 
- **MAGGIORE O UGUALE**
	Invece in questo caso, il sensore starborderà dal MAXIMUM FIELD VIEW, questo comporta a degli effetti di **vigenttamento** e **spreco dimensioni del sensore**
Il FOV viene calcolato:
$$
FOV=\arctan\left( \frac{W}{2d} \right)
$$

## PIXEL DENSITY
Viene definita dal rapporto **mm/px**.
Questo rapporto può essere calcolata con:
1) **MAGNIFICATION LAW**
2) Misura contando i pixel di un oggetto in un'immaggine

## COME FUNZIONANO
Per avere un'immagine, bisogna che il sensore, il quale è un insieme di pixel, deve **essere colpita dalla luce**, questa, luce deve essere campionata ad una certa frequenza (**Nyquist**).
Il valore del pixele viene deciso tramite misurazione durante il **tempo d'esposizione**, poichè un pixel non raccoglie la luminosità instantaneamente, infatti durante questo lasso di tempo un pixel raccoglie un certo numero di **foroni**.
$$
N_{photon} = irradiance*pixelArea* exposureTime
$$
Per aumentare la luminosità si può:
- aumentare l'illuminazione
- incrementare l'apertura
- Sensore con una grandezza dei pixel più grandi
- Aumentare l'exposure time

L'**exposure time** defnisce per quanto tempo si osserva un certo oggetto durante una misurazione.

**Frame rate** definisce

## SHUTTER TYPE
Per un **global shutter**, ogni riga di pixel, condividono lo stesso intervallo d'integrazione.

Per il **rolling shutter**, ogni riga legge ogni linea una alla volta, spostando l'intervallo sempre più avanti, questo lo rende più economico ma produce degli **artefatti**, modificando l'immagine:
- oggetti dritti vengono catturati storti
- comprime e espande l'oggetto
- se l'oggetto è in rotazione può fondere l'oggetto insieme ad un altro oggetto
Questi effetti non sono riconducibile all'exposure time, ma sono errore chevengono generati dal sensore stesso.

# EFFICICIENZA
Non tutti i fotno contribuiscono allacquisizione dell'immagine, questo avviene perché essite una **probabilità** che un elettrone venga **rilasciato** come risultato.
Questa probabilità viene definita come **quantum efficiency**, e questa dipende dallla lunghezza d'onda della luce.

Un pixel **non è un contenitore infinito**, quando un sensore supera la sua massima capacità.



# COME ACQUISIRE UN'IMMAGINE
Per acquisire un'immagine il componenete più importante è la **telecamera**, però per elaborarla servono un certo tipo di algortmi, nel nostro caso utilizzaeremo **OPENCV**.

Per acquisire un frame tranite numpy si deve:
```
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

