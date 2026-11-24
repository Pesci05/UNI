# Esempi circuiti risolti

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Esempi svolti completi: carica/scarica condensatore RC, regolatore Zener con/senza carico**.

---

## ES. 1 — Carica e scarica di un condensatore (circuito RC)

> **Schema:** ![[Pasted image 20260516162059.png]]

### Circuito
- Sorgente tensione $V_b$ (batteria)
- Resistore $R$ in serie
- Condensatore $C$ verso massa
- Interruttore $S$ tra $V_b$ e $R$

### Analisi per intervalli temporali

#### Per $t < 0$ — Interruttore **OFF** (aperto)
- Circuito aperto → nessuna corrente
- $$I = I_{switch} = I_R = I_C = 0$$
- $$I_C = C \frac{dV_C}{dt} = 0 \Rightarrow \frac{dV_C}{dt} = 0$$
- $$I_R = \frac{V_R}{R} = 0 \Rightarrow V_R = 0$$
- Condensatore **scarico**: $V_C(0^-) = 0$

#### Per $t = 0$ — Interruttore commutato **ON** (chiuso)
- Cortocircuito sull'interruttore → circuito serie $V_b - R - C$
- Equazione di maglia (KVL):
  $$V_b - R I_R(t) - V_C(t) = 0$$
- Corrente uguale su $R$ e $C$ ($I_R = I_C$):
  $$I_C = C \frac{dV_C}{dt}$$
- Equazione differenziale:
  $$V_b - R C \frac{dV_C}{dt} - V_C(t) = 0$$

#### Soluzione (condizione iniziale $V_C(0) = 0$)
$$V_C(t) = V_b \left[ 1 - e^{-t / RC} \right]$$

### Carica del condensatore
$$Q_C(t) = C V_C(t) = C V_b \left[ 1 - e^{-t / RC} \right]$$

### Comportamento temporale
- Tensione $V_C$ cresce **esponenzialmente** verso $V_b$
- **Costante di tempo**: $\tau = RC$
  - $t = \tau \quad\Rightarrow\quad V_C = 0.632 V_b$ (63%)
  - $t = 3\tau \quad\Rightarrow\quad V_C = 0.95 V_b$ (95%)
  - $t = 5\tau \quad\Rightarrow\quad V_C \approx 0.993 V_b$ (99.3%)

### Corrente nel circuito
$$I_C(t) = I_R(t) = C \frac{dV_C}{dt} = \frac{V_b}{R} e^{-t / RC}$$
- Picco a $t=0$: $I_{max} = V_b / R$ (condensatore = cortocircuito istantaneo)
- Decade esponenzialmente con stessa $\tau = RC$

### Scarica (interruttore riaperto a $t \gg \tau$)
Se $S$ si riapre dopo carica completa ($V_C = V_b$):
$$V_C(t) = V_b e^{-t / RC}$$
$$I_C(t) = -\frac{V_b}{R} e^{-t / RC} \quad \text{(corrente inversa)}$$

---

## ES. 2 — Regolatore di tensione con Diodo Zener

> **Schema:** ![[Pasted image 20260325180916.png]]

### Parametri dati
| Simbolo | Valore | Significato |
|---------|--------|-------------|
| $V_Z$ | 3 V | Tensione Zener (breakdown inverso) |
| $V_{in}$ | 12 V (nominale) | Tensione ingresso non regolata |
| $R_s$ | 1 k$\Omega$ | Resistenza serie (limitazione corrente) |
| $I_{Z,min}$ | 1 mA | Corrente Zener minima per regolazione |
| $I_{Z,max}$ | 10 mA | Corrente Zener massima (potenza/affidabilità) |

---

### Caso A — **Senza carico** ($R_L = \infty$, circuito aperto su uscita)

Tutta la corrente $I_s$ scorre nel diodo Zener:
$$I_s = \frac{V_{in} - V_Z}{R_s} = \frac{12 - 3}{1000} = 9 \text{ mA}$$

**Verifica range Zener:** $1 \text{ mA} \le 9 \text{ mA} \le 10 \text{ mA}$ ✓ → **Zener polarizzato correttamente**

#### Range tensione ingresso per regolazione valida
- **Max** (limite $I_{Z,max}$):
  $$V_{in,max} = V_Z + R_s \cdot I_{Z,max} = 3 + 1000 \cdot 0.01 = 13 \text{ V}$$
- **Min** (limite $I_{Z,min}$):
  $$V_{in,min} = V_Z + R_s \cdot I_{Z,min} = 3 + 1000 \cdot 0.001 = 4 \text{ V}$$

**Range $V_{in}$ senza carico: 4 V – 13 V** → uscita fissa 3 V

---

### Caso B — **Con carico** $R_L = 1 \text{ k}\Omega$

Ora la corrente si divide:
- $I_s$ = corrente su $R_s$ (totale)
- $I_L = V_Z / R_L = 3 / 1000 = 3 \text{ mA}$ (corrente carico, costante se Zener regola)
- $I_Z = I_s - I_L$ (corrente Zener)

Con $V_{in} = 12 \text{ V}$:
$$I_s = 9 \text{ mA} \quad \Rightarrow \quad I_Z = 9 - 3 = 6 \text{ mA} \quad (\text{in range})$$

#### Nuovo range $V_{in}$ con carico

**Minimo** ($I_Z = I_{Z,min} = 1 \text{ mA}$):
$$I_{s,min} = I_{Z,min} + I_L = 1 + 3 = 4 \text{ mA}$$
$$V_{in,min} = V_Z + R_s \cdot I_{s,min} = 3 + 1000 \cdot 0.004 = 7 \text{ V}$$

**Massimo** ($I_Z = I_{Z,max} = 10 \text{ mA}$):
$$I_{s,max} = I_{Z,max} + I_L = 10 + 3 = 13 \text{ mA}$$
$$V_{in,max} = V_Z + R_s \cdot I_{s,max} = 3 + 1000 \cdot 0.013 = 16 \text{ V}$$

**Range $V_{in}$ con $R_L=1\text{k}\Omega$: 7 V – 16 V**

> **Osservazione:** il carico **sposta** il range verso tensioni più alte (serve più corrente su $R_s$ per mantenere $I_{Z,min}$).

---

### Caso C — **Carico variabile**, $V_{in}$ fisso (12 V)

$I_s = 9 \text{ mA}$ costante (dipende solo da $V_{in}$, $V_Z$, $R_s$)

Vincolo: $I_{Z,min} \le I_Z \le I_{Z,max}$

$$I_Z = I_s - I_L = 9 - I_L$$

- **Max corrente carico** (quando $I_Z = I_{Z,min} = 1 \text{ mA}$):
  $$I_{L,max} = I_s - I_{Z,min} = 9 - 1 = 8 \text{ mA}$$
- **Min resistenza carico** (corrispondente a $I_{L,max}$):
  $$R_{L,min} = \frac{V_Z}{I_{L,max}} = \frac{3}{0.008} = 375 \Omega$$

**Condizione di funzionamento:** $R_L \ge 375 \Omega$ (altrimenti Zener esce da regolazione per mancanza $I_{Z,min}$)

Verifica anche $I_{Z,max}$: con $R_L \to \infty$, $I_Z = 9 \text{ mA} < 10 \text{ mA}$ ✓

---

### Sintesi parametri progetto Zener

| Parametro | Formula | Valore esempio |
|-----------|---------|----------------|
| $I_s$ | $\frac{V_{in} - V_Z}{R_s}$ | 9 mA @ 12 V |
| $I_L$ | $\frac{V_Z}{R_L}$ | 3 mA @ 1 k$\Omega$ |
| $I_Z$ | $I_s - I_L$ | 6 mA |
| $V_{in,min}$ (no load) | $V_Z + R_s I_{Z,min}$ | 4 V |
| $V_{in,max}$ (no load) | $V_Z + R_s I_{Z,max}$ | 13 V |
| $V_{in,min}$ (with $R_L$) | $V_Z + R_s (I_{Z,min} + V_Z/R_L)$ | 7 V |
| $V_{in,max}$ (with $R_L$) | $V_Z + R_s (I_{Z,max} + V_Z/R_L)$ | 16 V |
| $I_{L,max}$ (fixed $V_{in}$) | $\frac{V_{in}-V_Z}{R_s} - I_{Z,min}$ | 8 mA |
| $R_{L,min}$ | $\frac{V_Z}{I_{L,max}}$ | 375 $\Omega$ |
| Potenza Zener max | $V_Z \cdot I_{Z,max}$ | 30 mW |
| Potenza $R_s$ max | $(V_{in,max}-V_Z)^2 / R_s$ | 169 mW @ 16 V |

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Analisi dei circuiti - Leggi fondamentali]] — KVL, KCL, Thevenin (Zener + $R_s$ = sorgente Thevenin)
- [[Componenti passivi - R, C, L e impedenza]] — Circuito RC nel dominio temporale, $\tau = RC$
- [[Dispositivi a semiconduttore - Diodi e Transistor]] — Modello Zener, regioni diodo, breakdown
- [[Potenza, termica e affidabilità]] — Dissipazione su $R_s$ e Zener, derating, SOA