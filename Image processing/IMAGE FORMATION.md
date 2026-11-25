# IMAGE FORMATION

> **Corso:** Image Processing 2026 — UNIMORE  
> **Docente:** Francesco Solera (Deep Vision Consulting)  
> **Tag:** #image-processing #optics #computer-vision #opencv

---

## 📑 Indice
- [[#Rifrazione e lenti sottili]]
- [[#Aperture]]
- [[#Da immagine continua a digitale]]
- [[#Come acquisire un'immagine (OpenCV + UVC)]]
- [[#Looking for Objects]]

---

# Rifrazione e lenti sottili

La **rifrazione** avviene ogni volta che la luce attraversa il confine tra due mezzi con **indici di rifrazione** diversi.
- In una lente standard avviene **due volte**: quando il raggio entra nella lente e quando esce.
- Nel modello di **lente sottile** (*thin lens*), si approssima la deviazione complessiva come una **singola deviazione** al centro della lente.

![[Pasted image 20261119172637.png]]

## Convessità e densità
- Il caso più comune è una lente **biconvessa** immersa in un mezzo meno denso (es. aria): si osserva un comportamento **convergente** (i raggi paralleli all'asse ottico si incontrano dopo la lente).
- Una lente **biconcava** in aria ha invece un comportamento **divergente**.
- La convergenza dipende anche dalla **densità ottica** relativa: se il mezzo esterno è otticamente più denso della lente, si osserva il comportamento opposto.

![[Pasted image 20261119172825.png|342]]
![[Pasted image 20261119172841.png|380]]

## Legge di Snell
La legge di Snell descrive come si piega la luce:

$$
n_{\text{air}} \sin\theta_{\text{air}} = n_{\text{glass}} \sin\theta_{\text{glass}}
$$

dove gli angoli sono misurati rispetto alla **normale** alla superficie.
- Se il raggio entra in un mezzo otticamente più denso ($n_{\text{glass}} > n_{\text{air}}$), l'angolo diminuisce ($\theta_{\text{glass}} < \theta_{\text{air}}$), e viceversa.

![[Pasted image 20261119175157.png]]

### Su superfici sferiche (ipotesi: lente sferica, oggetto all'infinito, angoli piccoli)
Si ottiene il punto $x$ in cui il raggio incontra l'asse ottico:

$$
x = \frac{n_2}{n_2 - n_1} R
$$

Poiché $x$ **non dipende da $h$**, tutti i raggi paralleli convergono nello stesso punto.

![[Pasted image 20261119175313.png]]

## Equazione del costruttore di lenti (Lens maker equation)
Applicando la legge di Snell due volte (entrata e uscita):

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

> La distanza focale descrive come gli oggetti del **mondo reale** (sinistra della lente) vengono trasformati nel **mondo delle immagini** (destra della lente).

## Equazione delle lenti sottili (Thin lens equation)
I 3 raggi speciali si incontrano nello stesso punto a distanza $d_i$ dalla lente (**piano dell'immagine**):

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
La lunghezza focale vincola $d_o$ e $d_i$: con una lente biconvessa standard **non tutto può essere a fuoco contemporaneamente**:

- **Aumentiamo $d_i$** $\rightarrow$ $d_o$ diminuisce $\rightarrow$ si mette a fuoco **più vicino** alla lente.
- **Diminuiamo $d_i$** $\rightarrow$ $d_o$ aumenta $\rightarrow$ si mette a fuoco **più lontano** dalla lente.

![[Pasted image 20261120171134.png]]

## Maximum field angle
La lunghezza focale influenza anche il **maximum field angle** $\theta_{\max}$ (legato al cerchio d'immagine $D_{ic}$):

$$
\theta_{\max} = 2\arctan\left(\frac{D_{ic}}{2d_i}\right)
$$

- A parità di $D_{ic}$, **aumentare $f$** (quindi $d_i$) **restringe** il maximum field angle (zoom in, meno scena inquadrata), e viceversa.

![[Pasted image 20261120171929.png|301]]

---

# Aperture

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

---

# Da immagine continua a digitale

Per passare da un'immagine reale a una digitale serve un **sensore**. Un pixel è una misura **foton-to-charge** su un'area finita, in un tempo finito, pesata spettralmente, con capacità finita e rumore.

## Sensore (Spatial integration and sampling)
Il sensore è un **rettangolo** diviso in **pixel**, che definiscono tre grandezze:
- **Risoluzione** ($N_x / N_y$, numero di pixel)
- **Grandezza dei pixel** ($p_x / p_y$, di solito $p_x = p_y$)
- **Grandezza del sensore** ($W / H$)

Solo due sono indipendenti:

$$
W = N_x \cdot p_x \qquad H = N_y \cdot p_y
$$

Ogni pixel **media** (integra) l'irradianza che raccoglie sulla sua area. Avere più pixel può significare:
- un **sensore più grande** (cattura più scena a parità di dettaglio),
- **pixel più piccoli** (cattura la stessa scena con maggior dettaglio).

## Field of View
Il **[[#Maximum field angle|maximum field angle]]** è una proprietà della lente (cerchio d'immagine $D_{ic}$ e distanza $d_i$).  
Il **Field of View (FOV)** effettivo è determinato dalla combinazione **lente + sensore**, in base alla **diagonale** del sensore rispetto al cerchio d'immagine:

| Condizione | Effetto |
|---|---|
| **Diagonale < cerchio d'immagine** | Sensore tutto dentro $\rightarrow$ zona ideale |
| **Diagonale ≥ cerchio d'immagine** | Sensore sborda $\rightarrow$ **vignettamento** + spreco dimensioni |

Il FOV orizzontale si calcola come:

$$
\text{FOV}_W = 2\arctan\left( \frac{W}{2d_i} \right)
$$

*(In pratica si assume spesso messa a fuoco all'infinito, cioè $f = d_i$).*

![[Pasted image 20261122233413.png|213]]

## Pixel Density
Rapporto **mm/px** (o **px/mm**) per collegare dimensioni in pixel alle dimensioni reali. Due metodi:

1. **Magnification law**:
   $$
   |m| = \frac{d_i}{d_o} = \frac{h_i}{h_o} \qquad \text{mm/px} = \frac{\text{pixel size}}{|m|}
   $$
2. **Misura diretta**: contando i pixel di un oggetto di dimensioni note.

> La relazione **mm/px** vale solo alla distanza $d_o$ specifica (spesso fissa).

### Pixel density: più alta è meglio?

| Risposta                 | Quando                                                               | Perché                                                                                                                                             |
| ------------------------ | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NO** (*optic limited*) | Sfocatura ottica (CoC, Airy disk, aberrazioni) copre già molti pixel | Aumentare i pixel non aggiunge dettaglio utile                                                                                                     |
| **SÌ** (fino a un punto) | Dettagli periodici nella scena                                       | Teorema di **Nyquist**: serve ≥ 2× la frequenza (2 px/periodo è limite rischioso). Sotto $\rightarrow$ **aliasing** = dettagli falsi (es. *Moiré*) |
| **Bilancio ideale**      | Ottica e sensore corrispondono                                       | Abbastanza campioni per il dettaglio più piccolo utile, niente aliasing                                                                            |

## Integrazione temporale (Temporal integration and sampling)
Un pixel accumula luce durante il **tempo d'esposizione** (*exposure time*):

$$
N_{\text{photons}} \propto \text{irradiance} \cdot \text{pixel area} \cdot \text{exposure time}
$$

Per aumentare la luminosità:
- aumentare l'illuminazione,
- aumentare l'apertura (meno *depth of field*),
- usare sensore con pixel più grandi,
- aumentare **exposure time** (rischio **motion blur**).

### Exposure time vs Frame rate
- **Exposure time**: per **quanto tempo** si osserva l'oggetto in una misurazione.
- **Frame rate**: **quanto spesso** si effettua la misurazione.
- Vincolo: $\text{exposure time} < \frac{1}{\text{frame rate}}$.
- Scena ferma $\rightarrow$ frame rate non critico; oggetto in movimento $\rightarrow$ anche campionamento temporale può produrre **aliasing**.

## Shutter Type

| Tipo | Funzionamento | Artefatti |
|---|---|---|
| **Global shutter** | Tutte le righe condividono lo stesso intervallo di integrazione | Nessuno (snapshot istantaneo) |
| **Rolling shutter** | Righe integrate/lette sequenzialmente (più economico) | **Skew** (moto parallelo), **stretch/compress** (moto incidente), **wobble** (rotazione), **bande** (luce modulata) |

> [!warning] Accorciare l'esposizione riduce il motion blur *dentro* ogni riga, ma **non elimina** lo sfasamento temporale *tra* le righe (artefatti persistono).

## Radiometrica, Quantizzazione e Rumore

Non tutti i fotoni contribuiscono: **quantum efficiency** = probabilità che un fotone rilasci un **elettrone** (dipende da $\lambda$).

### Full well capacity
Pixel **non è contenitore infinito**: **full well capacity** = max elettroni accumulabili. Oltre $\rightarrow$ **saturazione** = perdita info alte luci.

### Catena CMOS (fotoni $\rightarrow$ numeri)
1. **Fotoni $\rightarrow$ Elettroni** (quantum efficiency)
2. **Elettroni $\rightarrow$ Tensione** (proporzionale via *sensing node*)
3. **Gain analogico** (amplificatore, equiv. **ISO** consumer)
4. **ADC** (quantizzazione per *bit depth*: 8/10/12/16 bit $\rightarrow$ 0–255 / 0–1023 / 0–4095 / 0–65535)

### Sorgenti di rumore

| Rumore                 | Causa                                      | Caratteristica                          |
| ---------------------- | ------------------------------------------ | --------------------------------------- |
| **Shot noise**         | Segnale fotonico (Poisson)                 | $\sigma = \sqrt{S}$, cresce col segnale |
| **Dark-current noise** | Elettroni termici                          | Cresce con tempo e temperatura          |
| **Read noise**         | Introdotta durante la lettura della carica | Rilevante a basso segnale               |
| **Quantization noise** | Introdotta dai passi finiti ADC            | Uniforme su $\pm 0.5$ LSB               |

$$
\text{SNR} = \frac{\text{mean signal}}{\text{noise standard deviation}}
$$

### Exposure vs Gain (a parità di luminosità finale)

| Strategia                          | Elettroni | SNR          | Note                                               |
| ---------------------------------- | --------- | ------------ | -------------------------------------------------- |
| **Esposizione corta + Gain alto**  | Pochi     | **Bassa**    | Domina *read noise* amplificato                    |
| **Esposizione lunga + Gain basso** | Molti     | **Migliore** | Preferibile (evitando saturazione e *motion blur*) |

> [!info] **Regola**: raccogliere più elettroni possibile (scena e applicazione permettendo).

## Selezione spettrale (Spectral selection)
- **Luce visibile**: 380–740 nm.
- **Sensori Si**: sensibili fino a 1000–1100 nm (near-IR) $\rightarrow$ serve filtro **IR-cut**.
- **Termocamere**: sensori/ottiche diverse per far-IR.

| Tipo              | Principio                                      | Trade-off                                      |
| ----------------- | ---------------------------------------------- | ---------------------------------------------- |
| **Monocromatica** | Tutte $\lambda$ mescolate in 1 luminanza       | Max fotoni, dettagli reali                     |
| **RGB (Bayer)**   | Filtri R,G,B prima del sensore; interpolazione | Verde 2× denso (luminanza); filtri riducono QE |

---

# Come acquisire un'immagine (OpenCV + UVC)

Per acquisire un'immagine il componente più importante è la **telecamera**; per elaborarla servono algoritmi: useremo **OpenCV**.

## Scelta della telecamera
Applicazioni diverse $\rightarrow$ setup diversi. Criteri principali:
- **Costo**
- **Robustezza** (*ruggedness*)
- **Qualità d'immagine**
- **Zoom & Focus** (fissi, manuali, autofocus)
- **Parametri impostabili** via software
- **Forma e dimensioni** (meccanica)

> Tutte condividono gli stessi principi di **image formation** e **image processing**.

## OpenCV: frame come array NumPy
OpenCV collega 3 moduli: **I/O** (file, camere), **Immagini/Frame** (array), **Algoritmi** (trasformano array). Disponibile in C++ e Python (prototipazione Python, deploy C++).

```python
ok, frame = cap.read()
print(frame.shape)   # (H, W, C)
print(frame.dtype)   # solito uint8
blue, green, red = frame[r, c]
```

> **Cose vitali dal giorno 1:**
> - **Origin**: top-left (x → destra, y → giù)
> - **Indexing**: `frame[r, c]` 0-based
> - **Channel order**: **BGR** (non RGB)
> - **Typical range**: 0–255 (uint8)

### Lavorare in float (operazioni custom)
```python
frame_float = frame.astype(np.float32) / 255
# ... operazioni ...
frame = np.clip(frame_float * 255, 0, 255).astype(np.uint8)
```

> [!warning] **Almeno il 50% dei bug** nasce da conversioni uint8/float sbagliate.

## UVC = USB Video Class (standard)

> **Problema**: ogni camera ha SDK proprietario $\rightarrow$ cambiare camera = cambiare codice.  
> **Soluzione UVC**: driver standard espongono capacità in modo uniforme.

| OS | Backend |
|---|---|
| Linux | **V4L2** |
| Windows | **Media Foundation / DirectShow** |

Una camera UVC descrive:
- Video stream disponibili
- Risoluzioni e frame rate
- Formati pixel (raw/compressi)
- Controlli supportati e come impostarli

*Ogni capacità resta opzionale e dipende dal produttore.*

### Ispezionare capacità UVC

**Linux (terminale):**
```bash
v4l2-ctl --device=/dev/video0 --list-formats-ext   # formati, risoluzioni, fps
v4l2-ctl --device=/dev/video0 --list-ctrls-menus   # controlli: focus/autofocus, exposure, gain, white balance
```

**GUI:** Linux → `GUVCView` | Windows → `VirtualDub2` → *Capture > Capture AVI…* → *Device > …* → *Video > Capture filter…*

## Controlli Camera (UVC / OpenCV)

Metodi core: `cap.set()`, `cap.get()`, `cv.imwrite()`.

> [!warning] **`set()` è una *richiesta*, non un ordine imperativo** $\rightarrow$ **verificare sempre** con `get()` dopo aver impostato.

### Proprietà principali (`cv.CAP_PROP_*`)

| Proprietà | Descrizione |
|---|---|
| `CAP_PROP_EXPOSURE` | Tempo esposizione (unità log/μs, dipende backend) |
| `CAP_PROP_AUTO_EXPOSURE` | 0=manuale, 1=auto, 3=apertura prioritaria (dipende backend) |
| `CAP_PROP_GAIN` | Gain analogico (ISO) |
| `CAP_PROP_FOCUS` | Focus assoluto (0–∞, dipende camera) |
| `CAP_PROP_AUTOFOCUS` | 0=spento, 1=acceso |
| `CAP_PROP_WHITE_BALANCE_BLUE_U` / `RED_V` | Bilanciamento bianco |
| `CAP_PROP_AUTO_WB` | Auto white balance on/off |
| `CAP_PROP_FRAME_WIDTH` / `HEIGHT` | Risoluzione richiesta |
| `CAP_PROP_FPS` | Frame rate richiesto |
| `CAP_PROP_FOURCC` | Codec (per video) |
| `CAP_PROP_POS_FRAMES` / `POS_MSEC` | Posizione playback (solo video file) |

## Salvataggio immagini (`imwrite`)
L'estensione sceglie l'encoder:

| Formato | Tipo | Note |
|---|---|---|
| **BMP** | Uncompressed lossless | Pesante: $W \times H \times 3$ byte |
| **PNG** | Compressed lossless | Meno pesante, qualità originale intatta |
| **JPG** | Compressed lossy | Trade-off qualità/dimensione; flag `cv.IMWRITE_JPEG_QUALITY` (0–100) |

> [!warning] Molte camere economiche inviano **già compresso** (MJPEG/H.264) $\rightarrow$ salvare in PNG non "decomprime" gli artefatti.

## Acquisizione Video (`VideoWriter`)

```python
ok, frame = cap.read()
h, w = frame.shape[:2]
fourcc = cv.VideoWriter_fourcc(*"MJPG")   # o "XVID", "DIVX", "X264"
writer = cv.VideoWriter("data/clip.avi", fourcc, 30.0, (w, h))
if not writer.isOpened():
    raise RuntimeError("Cannot open video writer")

while True:
    ok, frame = cap.read()
    if not ok: break
    writer.write(frame)
    # ... eventuale visualizzazione ...
writer.release()
```

- Tutti i frame **devono avere stessa size** `(w, h)`.
- **Niente audio** con OpenCV.

## Lettura Video (`VideoCapture` su file)

```python
video = cv.VideoCapture("data/clip.avi")
fps = video.get(cv.CAP_PROP_FPS)
count = video.get(cv.CAP_PROP_FRAME_COUNT)
w = video.get(cv.CAP_PROP_FRAME_WIDTH)
h = video.get(cv.CAP_PROP_FRAME_HEIGHT)
print(f"{w:.0f}×{h:.0f}")
print(f"{fps:.2f} FPS, {count:.0f} frames")
print(f"Durata nominale = {count / fps:.2f} s")

while True:
    ok, frame = video.read()
    if not ok: break
    # processa frame...
```

- Stessa API della camera (`read()`).
- Non tutte le proprietà settabili (es. risoluzione fissa).
- *Seek* possibile con `CAP_PROP_POS_FRAMES` o `POS_MSEC`.

## Stima parametri camera (FOV, focale) — Laboratorio

Obiettivo: stimare **FOV** e **focale** (pixel + mm) e confrontare con datasheet.

### Metodo (modello lente sottile + triangoli simili)
1. Target noto (es. metro a nastro) a distanza nota $d_o$ dalla camera.
2. Misura in pixel l'altezza $h_w$ del target nell'immagine (quando riempie esattamente altezza sensore $H$).
3. Triangoli simili:
   $$
   \frac{h_w}{H} = \frac{d_o}{d_i} \quad \Rightarrow \quad d_i = \frac{H \cdot d_o}{h_w}
   $$
   Poiché $d_o \gg d_i$, spesso **$f \approx d_i$**.
4. **Focale in pixel**: $f_{\text{px}} = d_i$ (unità pixel, perché $H$ in pixel).
5. **Focale in mm**: $f_{\text{mm}} = f_{\text{px}} \times p$, dove $p$ = *pixel pitch* (mm/px) dal datasheet.
6. **FOV**:
   $$
   \text{FOV}_H = 2\arctan\left(\frac{W}{2 f_{\text{px}}}\right), \quad
   \text{FOV}_V = 2\arctan\left(\frac{H}{2 f_{\text{px}}}\right)
   $$

### Fonti di errore tipiche (10–15% scostamento datasheet)
- Incertezza punto misura $d_o$ (pupilla d'ingresso vs frontale lente)
- *Focus breathing* e autofocus a distanze ravvicinate
- Distorsione radiale ai bordi
- Allineamento imperfetto target
- Soggettività "target riempie esattamente il frame"
- Approssimazione modello lente sottile

---

---
---
# Edges to countours
I bordi estraggono informazioni, da un'immagine, ma questi non sono molto interpretabili da un algoritmo.

Il risultato di questo tipo di algortmi viene detto **edge map**.

**[[IMAGE PROCESSING#EDGE DETECTION|Sobel edge detection]]**, Sobel dà un risultato per ogni pixel, questo compromette la rilevazione dei bordi, per questo si può introdurre un **treshold**(soglia), però questa soglia può produrre problemi:
- **Rumore produce gradienti**
- **Un bordo sfocato non produce un bordo formato da un unico pixel, ma un bordo più spesso**
- **le texture producono risposte irrilevanti**
- **Una soglia può perdere bordi validi o anche conservare troppo rumore.**
- **Risposta della soglia può essere frammentata.**

## CANNY edge detector: Pipeline
1. **Gaussian smoothing**:
    - **Cosa fa**: Applica una sfumatura gaussiana iniziale per sopprimere il rumore ad alta frequenza.
    - **Perché**: Le derivate amplificano i cambiamenti rapidi, incluso il rumore. Il Gaussian smoothing stabilisce la scala alla quale un bordo è considerato significativo. Se un dettaglio viene rimosso dallo smoothing, significa che non era un bordo che volevamo rilevare, ma un dettaglio/rumore da eliminare. Uno smoothing maggiore rimuove il rumore fine ma può anche rimuovere o spostare i piccoli dettagli.
	 [[4. from edges to contours intro to thresholding  morphology.pdf#page=13|4. from edges to contours intro to thresholding  morphology, pagina 13]]

2. **Gradient estimation**:
    - **Cosa fa**: Calcola la magnitudine e la direzione del gradiente (esattamente come Sobel).
    

3. **Non-maximum suppression (NMS)**:
    - **Cosa fa**: Serve ad **assottigliare ciascuna cresta del gradiente** per ottenere contorni spessi un solo pixel.
    - **Come funziona**:
        - Si segue la direzione del gradiente 𝜃 in un pixel candidato.
        - Si confronta la magnitudine del pixel con i due campioni vicini lungo quella direzione (_il confronto viene fatto attraverso il bordo, non lungo di esso_).
        - Si **ritiene il pixel solo se è un massimo locale**. Altrimenti, se il valore non è maggiore dei pixel vicini, il pixel non è un bordo e viene completamente soppresso.
    [[4. from edges to contours intro to thresholding  morphology.pdf#page=14|4. from edges to contours intro to thresholding  morphology, pagina 14]]

4. **Double threshold (Doppia soglia)**:
    - **Cosa fa**: Classifica le risposte impostando due soglie 𝑇𝐿 e 𝑇𝐻 (𝑇𝐿 <𝑇𝐻):
        - 𝑀 ≥𝑇𝐻 → candidato a **bordo forte** (strong edge candidate).
        - 𝑇𝐿 ≤𝑀 <𝑇𝐻 → candidato a **bordo debole** (weak edge candidate).
        - 𝑀 <𝑇𝐿 → **rigettato**.
    [[4. from edges to contours intro to thresholding  morphology.pdf#page=15|4. from edges to contours intro to thresholding  morphology, pagina 15]]

5. **Hysteresis (Isteresi)**:
    - **Cosa fa**: Serve a rimuovere i bordi deboli isolati e a **connettere i bordi spezzati**.
    - **Come funziona**: L'isteresi **ritiene un candidato debole solo quando è collegato a un percorso di bordi forti**. Di conseguenza, una continuazione debole (faint continuation) può sopravvivere se supportata da bordi forti, mentre una risposta debole e isolata scompare.

Per avere un certo numero di **bordi**, ci devono essere un certo numero di **regioni**, bordi e regioni devono essere rispettivamente $\text{bordi} \leq \text{regioni}$.

Una edge map può contenere:
- Curve aperte
- Bordi di texture irrilevanti
- Nessun etichetta esplicita.

Una **region mask** è un'immagine binaria che rappresenta un'area o un oggetto pieno, le proprietà di queste mask sono:
- Rimuovere piccole strutture in primo piano
- Riempire i buchi
- Combinare regioni
- Misurare l'area
>[!note] Da una regione possiamo sempre estrarre un bordo (che chiamiamo _contour_), ma da un bordo non sempre si può ricuperare una regione

### Canny in OpenCV

```python
edges = cv2.Canny(gray, low_threshold, high_threshold)
```

### Metodo più facile per avere una regione
Per oggetti scuri su sfondo chiaro:
$$
M(x,y) = \{255,  I(x,y) < T \\0,I(x,y) \geq T \}
$$
```python
_, mask = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY_INV)
```

## Tipi di Threshold
Per le immagini in scala di grigio, non è così facile trovare un treshold giusto, per questo esistono diversi tipi di threshold come:
- **Otsu's method**
	metodo automatico per trovare una soglia ottimale in un'immagine in scala di grigi.
	Trova la soglia (threshold) ottimale **minimizzando la varianza di intensità intra-classe** (intra-class intensity variance), oppure, in modo equivalente, **massimizzando la varianza inter-classe** (inter-class variance). 
	$𝑡∗=arg⁡max0<𝑡<255[𝜔0(𝑡)𝜎20(𝑡)+𝜔1(𝑡)𝜎21(𝑡)]$
```python
otsu_value, mask = cv2.threshold(
       gray, 0, 255, 
       cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
```
- **Adaptive threshold**
	Per sopraggiungere ai limiti di una soglia globale, si può calcolare una soglia che dipende da **statistiche locali** dell'immagine.
	Per scegliere i parametri di queste statistiche locali:
	- **Neighborhood piccoli (`block_size` ridotto):** Seguono molto bene i dettagli locali, ma rischiano di amplificare la texture e il rumore.
	- **Neighborhood grandi (`block_size` ampio):** Si comportano in modo simile a una soglia globale che varia lentamente nello spazio
	
$$
	t(x,y) = \mu_{N(x,y)} - C
$$
```python
mask = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    block_size, C
)
```

### Tabella di confronto dei metodi di Thresholding

|Metodo|Assunzioni principali|Parametri principali|Tipico fallimento / Problema|
|:--|:--|:--|:--|
|**Fixed (Globale)**|Intensità note e stabili|𝑇|Cambiamenti di esposizione o illuminazione (broken assumptions)|
|**Otsu**|Due classi globali separabili|Nessuno (automatico)|L'illuminazione varia spazialmente|
|**Adaptive**|Due classi locali separabili|`block_size`, 𝐶|Texture / rumore o scelta errata della scala|

>[!note] Scegliere sempre il metodo più semplice le cui assunzioni corrispondono alle condizioni di acquisizione dell'immagine

## Morphology
La **morphology** è un insieme di operazioni che processano un'immagine in modo tale di:
- **Ingrandire**
- **Restringere**
- **Pulire**
- **Unire strutture spaziali**

Un'immagine binaria si può vedere come un insieme di coordinate A(insieme dei pixel bianchi), e mentre i pixel neri appartengono al complemento AC.
Tramite la morfologia si può avere un terzo insieme $B$ chiamato **Structuring element**.
Si parte da una **sogliatura debole**, per poi applicare la morfologia per avere esattamente le regioni che appartengono agli **oggetti reali**.
## Structuring element
La structuring element è il **secondo insieme/kernel** utilizzato nelle operazioni morfologiche.

Una structuring element definisce:
- **Forma**
- **Dimensione**
- **Ancoraggio**
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
```

>[!warning] **lo structuring element non è ancora l'operazione in sé**, ma definisce il **supporto** (la regione di pixel) degli elementi coinvolti nell'operazione morfologica (come erosione, dilazione, apertura o chiusura).



 

---
# Looking for Objects

## Labeling
Input: immagine binaria $\rightarrow$ Output: immagine con **etichetta** per ogni pixel. Alternativa a *findContours* (che dà più info).

### Intorno di un pixel *foreground*
$$
N_{4} = \{(x-1,y),(x+1,y),(x,y-1),(x,y+1)\} \\
N_{8} = N_{4} \cup \{(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)\}
$$

### Algoritmo (two-pass)
1. **Scansione**: ispeziona vicini
   - Nuova label se vicini senza label
   - Riusa label se una sola presente
   - Segna equivalenza temporanea se 2 label diverse
2. **Risoluzione**: rimpiazza equivalenze con label unica

```python
count, labels, stats, centroids = cv2.connectedComponentsWithStats(
    mask, connectivity=4
)
```

- `labels[x,y]`: intero che **identifica ogni pixel**
- `stats[i]`: LEFT, TOP, WIDTH, HEIGHT, AREA per label $i$

### Requisiti per label valida
- **Area plausibile**
- **Centroide** dentro regione ispezionata

> Per risolvere problemi su immagini, usare **conoscenze a priori** sul problema.

## Template Matching
*(Sezione da completare)*

---

## 🔗 Link utili
- [OpenCV Docs](https://docs.opencv.org/)
- [v4l2-ctl man page](https://manpages.ubuntu.com/manpages/jammy/man1/v4l2-ctl.1.html)
- [USB Video Class Spec](https://www.usb.org/video)
- [Image Processing @ DeepVisionConsulting](https://image-processing.deepvisionconsulting.com/)