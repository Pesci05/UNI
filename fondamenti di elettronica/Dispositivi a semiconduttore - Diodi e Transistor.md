# Dispositivi a semiconduttore – Diodi e Transistor

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Diodi PN, Zener, LED, Fotodiodo; BJT, MOSFET, SOA, termica**.

---

## Diodi

### Diodo PN (standard)
- Componente **non lineare**, **non simmetrico**, 2 terminali: **Anodo** (+) / **Catodo** (−)
- Semiconduttore (Silicio) → **drogaggio** (impurità controllate)
- Relazione corrente-tensione (Shockley):
  $$I = I_0 \left[ e^{\frac{qV}{kT}} - 1 \right]$$
  - $I_0$: corrente di saturazione inversa
  - $q$: carica elementare, $k$: Boltzmann, $T$: temperatura [K]
  - Per $V \gg V_T = kT/q \approx 26\text{mV}$: $I \approx I_0 e^{V/V_T}$

> **Riferimento slide:** [[01 - Nuts and Bolts of Electronics.pdf#page=30|pagina 30]]  
> **Curva I-V:** ![[Screenshot From 2025-10-03 10-40-57.png]]  
> **Simbolo:** ![[Screenshot From 2025-10-03 10-23-39.png]]

#### Regioni di funzionamento
| Regione | Condizione | Comportamento |
|---------|------------|---------------|
| **Forward Bias** | $V > V_\gamma \approx 0.7\text{V}$ (Si) | ~cortocircuito, corrente esponenziale |
| **Reverse Bias** | $V < 0$ | ~circuito aperto, corrente $\approx -I_0$ |
| **Breakdown** | $V < -V_{BR}$ | Rottura irreversibile (salvo Zener) |

---

### Diodo Zener
Progettato per lavorare in **regione di breakdown** controllata ($V_Z$ costante).

#### Esempio calcolo range ingresso (da [[Esempi circuiti risolti]])
- $V_Z = 3\text{V}$, $V_{in} = 12\text{V}$, $R_s = 1\text{k}\Omega$, $I_{Zmin}=1\text{mA}$, $I_{Zmax}=10\text{mA}$
- **Senza carico** ($R_L = \infty$):
  - $I_s = (12-3)/1\text{k} = 9\text{mA}$ ✓ (in range)
  - $V_{in,max} = V_Z + R_s I_{Zmax} = 13\text{V}$
  - $V_{in,min} = V_Z + R_s I_{Zmin} = 4\text{V}$
- **Con carico** $R_L = 1\text{k}\Omega$:
  - $I_L = 3\text{mA}$, $I_Z = 6\text{mA}$
  - $I_{s,min} = I_{Zmin} + V_Z/R_L = 4\text{mA} \to V_{in,min} = 7\text{V}$
  - $I_{s,max} = I_{Zmax} + V_Z/R_L = 13\text{mA} \to V_{in,max} = 16\text{V}$
  - $I_{L,max} = (V_{in}-V_Z)/R_s - I_{Zmin} = 8\text{mA}$
  - $R_{L,min} = V_Z / I_{L,max} = 375\Omega$

> **Schema:** ![[Pasted image 20260325180916.png]]

---

### Alti tipi di diodi
| Tipo | Caratteristica | Applicazione |
|------|----------------|--------------|
| **LED** | Emette luce se forward-biased; $\lambda$ dipende da banda proibita | Indicatori, illuminazione |
| **Fotodiodo** | Genera corrente se illuminato (reverse bias) | Sensori luce, comunicazione ottica |
| **Schottky** | Giunzione metallo-semiconduttore, $V_\gamma \approx 0.3\text{V}$, veloce | Raddrizzatori switching, protezione |

> **Curve I-V vari tipi:** ![[Pasted image 20260127213150.png]] ![[Pasted image 20260127214452.png]] ![[Pasted image 20260127212231.png]]

---

## Transistor BJT (Bipolar Junction Transistor)

### Struttura
- 3 regioni drogate: **NPN** o **PNP**
- Terminali: **Base (B)**, **Collettore (C)**, **Emettitore (E)**
- $I_B$ controlla $I_C$ e $I_E$

> **Simbolo/struttura:** ![[Screenshot From 2025-10-03 12-24-22.png]]  
> **Riferimento slide:** [[01 - Nuts and Bolts of Electronics.pdf#page=37|pagina 37]]

### Regioni di funzionamento
| Regione | $V_{BE}$ | $V_{CE}$ | Comportamento |
|---------|----------|----------|---------------|
| **Cut-off** | $V_{BE} \ll 0.7\text{V}$ | Qualsiasi | $I_B \approx 0 \Rightarrow I_C \approx 0$ (aperto) |
| **Saturazione** | $V_{BE} \gtrsim 0.7\text{V}$ | $V_{CE} < V_{CE,sat}$ | $I_C \approx \beta I_B$ (chiuso, $V_{CE} \approx 0.2\text{V}$) |
| **Attiva** | $V_{BE} \gtrsim 0.7\text{V}$ | $V_{CE} > V_{CE,sat}$ | Amplificatore: $I_C = \beta I_B$ |

> **Curve caratteristiche:** ![[Pasted image 20260128181635.png]]

### Relazioni fondamentali
$$I_E = I_B + I_C$$
$$I_{C,max} = \beta \cdot I_B$$
$\beta$ (hFE) = guadagno di corrente (tipico 50–300)

### BJT come **Switch**
- Pilotato da onda quadra su Base
- $V_B$ bassa → **cut-off** → carico spento
- $V_B$ alta → **saturazione** → carico alimentato ($I_C = (V_{CC} - V_{CE,sat})/R_{load}$)

> **Circuito switch:** ![[Pasted image 20260128182407.png]]  
> **Corrente carico:** ![[Pasted image 20260129155834.png]]  
> **Tensione carico:** ![[Pasted image 20260129214840.png]]  
> **Potenza carico:** ![[Pasted image 20260129215310.png]]  
> **Potenza BJT:** ![[Pasted image 20260129215519.png]]

> **Nota reale:** $V_{CE,sat} \neq 0$ → dissipazione su BJT > 0

### Frequenza commutazione vs Tensione
- Più alta la tensione di sostegno → più bassa $f_{max}$
- Trade-off tensione/velocità

> **Grafico:** ![[Screenshot From 2025-10-06 10-15-21.png]]

---

## Transistor MOSFET (Metal-Oxide-Semiconductor FET)

### Struttura
- 4 terminali: **Gate (G)**, **Drain (D)**, **Source (S)**, **Body/Bulk (B)**
- B cortocircuitato a S se non usato
- **Gate isolato** (ossido) → $I_G \approx 0$, controllo per **tensione** $V_{GS}$

> **Simbolo:** ![[Pasted image 20260129221953.png]]  
> **Struttura:** ![[Screenshot From 2025-10-06 10-48-52.png]]  
> **Riferimento slide:** [[01 - Nuts and Bolts of Electronics.pdf#page=45|pagina 45]]

### Parametri chiave
- $V_{TH}$: tensione di soglia (tip. 1–4 V)
- $V_{OD} = V_{GS} - V_{TH}$: tensione di overdrive

### Regioni di funzionamento
| Regione | Condizione | $I_D$ | Comportamento |
|---------|------------|-------|---------------|
| **Cut-off** | $V_{GS} < V_{TH}$ | 0 | Interruttore aperto |
| **Triode (lineare)** | $V_{GS} \ge V_{TH}$, $V_{DS} < V_{OD}$ | $\propto V_{DS}$ | Resistenza variabile, switch chiuso |
| **Saturazione** | $V_{GS} \ge V_{TH}$, $V_{DS} \ge V_{OD}$ | $\propto (V_{GS}-V_{TH})^2$ | Sorgente di corrente, amplificatore |

> **Curve $I_D-V_{DS}$:** ![[Pasted image 20260130000347.png]]

---

## Dissipazione, SOA e Affidabilità termica

### Dissipatori di calore
- Pezzi metallici ad **area massimizzata** per scambio termico con ambiente
- Necessari per tenere $T_j$ (giunzione) sotto limite

> **Concetto:** ![[Pasted image 20260130001914.png]] (es. SOA BJT)

### Safe Operating Area (SOA)
Insieme di punti $(V_{CE}, I_C)$ o $(V_{DS}, I_D)$ sicuri per il dispositivo.

| Limite | Origine |
|--------|---------|
| $I_{max}$ | Corrente massima (bond wire, metallizzazione) |
| $V_{max}$ | Tensione di breakdown |
| $P_{max}$ | Potenza termica ($T_j < T_{j,max}$) |
| **Second breakdown** (BJT) | Instabilità termica localizzata ad alta $V$, bassa $I$ |

### BJT vs MOSFET: comportamento termico
| Aspetto | BJT | MOSFET |
|---------|-----|--------|
| Coeff. temp. $I_C/I_D$ | **Positivo** ($T\uparrow \to I\uparrow \to P\uparrow \to T\uparrow$) → **Thermal runaway** | **Negativo** ($T\uparrow \to I_D\downarrow \to P\downarrow$) → **Autolimitante** |
| SOA ad alta $V$ | Ristretta (second breakdown) | Più ampia |
| Parallelo | Difficile (current hogging) | Facile (current sharing naturale) |

> **Confronto SOA:** ![[Pasted image 20260130001914.png]] (BJT), descrizione testuale MOSFET

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Componenti passivi - R, C, L e impedenza]] — Capacità parassite $C_{gs}$, $C_{gd}$, $C_{ds}$
- [[Amplificatori operazionali]] — Stadi d'ingresso BJT/MOSFET
- [[Elettronica digitale]] — Switch logici, driver potenza
- [[Potenza, termica e affidabilità]] — Heat sink, derating, MTBF
- [[Esempi circuiti risolti]] — Zener con carico (regolazione tensione)