# Combustione, emissioni e post-trattamento MCI

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Combustione premiscelata vs diffusiva, anomalie, inquinanti, sistemi post-trattamento (catalizzatori, DPF, sonda lambda)**.

---

## Combustione premiscelata (Motori AS / Otto / Benzina / Gas)

La miscela aria-combustibile si forma **prima dell'innesco**.

### Caratteristiche principali
1. **Carica premiscelata** (omogenea)
   - Iniezione indiretta (condotti aspirazione) **o** diretta con forte anticipo
   - Miscelazione favorita da turbolenza camera
   - All'accensione: dosatura **stechiometrica** ($\lambda \approx 1$)
2. **Accensione comandata** (candela)
   - Scintilla = scarica elettrica → innalza $T$ locale > autoaccensione
3. **Propagazione fronte di fiamma**
   - Velocità propagazione = **velocità fronte fiamma**

### Fenomeni anomali indesiderati

| Fenomeno | Causa | Conseguenza |
|----------|-------|-------------|
| **Spegnimento fiamma** | Pareti troppo fredde, scarsa turbolenza, miscela magra ($\lambda>1$) | Fronte fiamma rallenta → si spegne prima di bruciare tutta la carica |
| **Accensione anticipata** | Alte $T$ carica/pareti → autoaccensione in punto ≠ candela, istante casuale | Fronte fiamma non desiderato; anche a bassi regimi (bassa vel. propagazione → tempo per autoaccensione) |
| **Detonazione (Knocking)** | Alte $T$ carica/pareti → **più punti** autoaccendono → **più fronti fiamma** | Onde d'urto alta frequenza, rumore forte, picchi pressione, **rottura/crollo prestazioni** |

**Rimedi detonazione:**
- ↑ **Numero di ottano (NO)**
- ↑ Turbolenza
- Camera combustione compatta
- Doppia candela
- Dosatura grassa ($\lambda<1$)

---

## Combustione diffusiva (Motori AC / Diesel)

Camera contiene inizialmente **solo aria** ad alta $p,T$. Combustibile iniettato direttamente poco prima PMS.

### Caratteristiche principali
1. **Carica disomogenea**
   - Iniezione **solo nell'istante** desiderato
   - Alta pressione → **atomizzazione** (gocce fini) → evaporazione → miscelazione
   - Solo zone stechiometriche reagiscono
2. **Accensione spontanea**
   - Innesco autonomo dove miscela locale raggiunge $p,T$ limite
3. **Nessun fronte fiamma propagante**
   - Fiamma **si diffonde lungo getto** combustibile man mano che si miscela
3. **Combustibile deve accendersi presto** → minimizza ritardo chimico
4. **Ritardo all'accensione** (intervallo inizio iniezione → innesco):
   - **Ritardo fisico** ($Rit_{fisico}$): penetrazione, atomizzazione, evaporazione, miscelazione
   - **Ritardo chimico** ($Rit_{chimico}$): reazioni pre-ossidazione → **NUMERO DI CETANO (NC)**

> **Qualità combustibile Diesel:** NC **elevato** → minimizza ritardo chimico → evita accumulo combustibile incombusto → accensione troppo violenta/rumorosa

---

## Tabella comparativa processi combustione

| Parametro | **Premiscelata (AS / Otto)** | **Diffusiva (AC / Diesel)** |
|-----------|------------------------------|-----------------------------|
| **Formazione miscela** | Esteriore / anticipata (omogenea) | Iniezione diretta in camera (disomogenea) |
| **Innesco** | Esterno comandato (candela) | Autoaccensione per alta $p,T$ |
| **Modalità fiamma** | Propagazione fronte fiamma | Fiamma diffusione lungo getto |
| **Dosatura globale $\lambda$** | Stechiometrica ($\approx1$) | Magra ($>1$) |
| **Proprietà combustibile** | Elevato **Numero Ottano** | Elevato **Numero Cetano** |
| **Anomalia principale** | Detonazione (Knocking) | Eccessivo ritardo accensione |

---

## Inquinanti emessi

### Gassosi

#### 1. Monossido di Carbonio ($CO$)
- **Origine**: ossidazione **incompleta** carbonio ($CO$ non completa a $CO_2$)
- **Causa principale**: repentina ↓ $T$ durante espansione
- **Influenza**: ↓ aria disponibile (↓ $\lambda$) → ↑ $CO$

#### 2. Idrocarburi incombusti ($HC$)
- **Cause**:
  1. **Flame quenching**: raffreddamento fiamma a contatto pareti
  2. Combustione incompleta
  3. **Adsorbimento film olio**: carburante assorbito da olio lubrificante → rilasciato incombusto
  4. **Crevices filling**: miscela in anfratti dove fiamma non arriva
- **Parametri**: $A/F$, anticipo accensione, rapporto superficie/volume camera, depositi, regime/carico, angolo incrocio valvole, contropressione scarico

#### 3. Ossidi di azoto ($NO_x$: $NO, NO_2, NO_3...$)
- **Origine**: ossidazione $N_2$ (principalmente da aria comburente)
- **Cause**:
  1. **Alte $T$ medie** zona fiamma
  2. Rapida ↓ $T$ espansione → "congelamento" reazioni riduzione $NO$
- **Parametri**: $A/F$, anticipo accensione, **EGR** (ricircolo gas scarico), regime/carico, rapporto compressione, sovralimentazione

---

### Solidi (Particolato)
- **Natura**: particelle solide/composite da ossidazione incompleta carburante + composti metallici/additivi; gas ad alta $T$ condensano/adsorbono raffreddandosi
- **Causa principale**: **scarso miscelamento locale** carburante-comburente
- **Parametri**: $A/F$, qualità sistema iniezione

---

### Altri
- **Ossidazione impurità**: $S$, $Pb$ nel carburante → $SO_x$, particolato piombo
- **$CO_2$**: ossidazione **completa** carbonio; non tossico ma **principale gas serra**

> **Diagramma emissioni vs dosatura:** ![[emissioni_inquinanti_dosatura.png]]

---

## Sistemi post-trattamento scarico (Euro 6d/7)

### 1. Catalizzatore trivalente (Motori AS / Benzina)
- **Solo con $\lambda=1$** (stechiometrico)
- Abbatte **simultaneamente 3 inquinanti**:
  - Riduce $NO_x \to N_2 + O_2$
  - Ossida $CO \to CO_2$
  - Ossida $HC \to CO_2 + H_2O$

### 2. Catalizzatore Selettivo SCR (Motori Diesel)
- Necessario per $\lambda>1$ (magra) dove trivalente non riduce $NO_x$
- Inietta **urea (AdBlue)** → idrolizza in fumi → **ammoniaca $NH_3$**
- $NH_3$ riduce $NO_x \to N_2 + H_2O$

### 3. Filtro antiparticolato (DPF / FAP)
- Matrice ceramica porosa ad alveoli → intrappola meccanicamente **PM10/PM2.5**
- **Rigenerazione periodica** $>550^\circ\text{C}$ (centralina comanda post-iniezioni per bruciare fuliggine)

### 4. Sonda lambda (controllo dosatura)
- Misura $O_2$ residuo scarico → segnale a centralina
- **Retroazione**: mantiene $\lambda \approx 1$ (necessario per trivalente)
- **Principio**: confronta $p_{O_2}$ aria riferimento vs gas scarico
  $$\Delta V \propto T \cdot \log\left(\frac{p_{O_2,\text{aria}}}{p_{O_2,\text{gas}}}\right)$$

> **Struttura sonda:** ![[Pasted image 20251112105843.png]] (contatto elettrico, supporto ceramica, elemento ceramico, tubo protettivo, molla a tazza, guaina, carcassa, elettrodi)

> **Riferimento slide:** [[008_MotoriACombustioneInterna_MN.pdf#page=60|pagina 60]]

---

## Collegamenti
- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Motori a combustione interna – Principi e classificazione]] — Classificazione AS/AC, diagramma indicatore
- [[Cicli termodinamici MCI (Otto, Diesel, Sabathé) e rendimenti]] — Parametri cicli, $\lambda$, rendimenti
- [[Termodinamica di base]] — 2° principio, entropia, irreversibilità combustione
- [[Layout cogenerativi dettagliati (TG, TV, CCGT, MCI)]] — MCI cogenerativo: recupero fumi (AT) + acqua camicia/olio (BT/MT)