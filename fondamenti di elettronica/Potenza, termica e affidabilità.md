# Potenza, termica e affidabilità

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Dissipazione, Heat sink, SOA, Thermal runaway, Derating, MTBF**.

---

## Potenza elettrica

### Definizione
$$P = V I \quad [\text{Watt}]$$

### Convenzioni segno
| Tipo componente | Potenza | Segno convenzionale |
|-----------------|---------|---------------------|
| **Dissipativo** (R, D, BJT, MOSFET in on-state, regolatori lineari) | Assorbe potenza → calore | $P > 0$ |
| **Erogativo** (Generatori, batterie, pannelli fotovoltaici, alternatori) | Fornisce potenza | $P < 0$ (o $|P|$ erogata) |

> **Riferimento:** [[Analisi dei circuiti - Leggi fondamentali#Convenzioni di potenza|Convenzioni di potenza]]

---

## Dissipazione nei componenti principali

### Resistore
$$P = I^2 R = \frac{V^2}{R} = V I$$
Tutta l'energia → **calore** (effetto Joule)

### Diodo
$$P \approx V_F \cdot I_F \quad (V_F \approx 0.7\text{V per Si}, 0.3\text{V Schottky})$$
In reverse: $P \approx V_R \cdot I_R$ (trascurabile salvo breakdown)

### BJT (in saturazione / attiva)
$$P = V_{CE} \cdot I_C + V_{BE} \cdot I_B \approx V_{CE} \cdot I_C$$
- **Switch**: $V_{CE,sat} \approx 0.1\text{–}0.3\text{V}$ → bassa dissipazione
- **Attiva/lineare**: $V_{CE}$ alto → **alta dissipazione** (es. regolatori lineari, stadi audio)

### MOSFET
$$P = I_D^2 \cdot R_{DS(on)} \quad \text{(on-state)}$$
$$P = V_{DS} \cdot I_D \quad \text{(lineare)}$$
- **Switch**: $R_{DS(on)}$ molto basso (m$\Omega$) → dissipazione minima
- **Commutazione**: perdite switching $\propto f_{sw} \cdot (E_{on} + E_{off})$

---

## Dissipatori di calore (Heat Sink)

> **Scopo**: trasferire calore da giunzione dispositivo ($T_j$) ad ambiente ($T_a$) mantenendo $T_j < T_{j,max}$.

### Modello termico (rete resistiva)
```
T_j ── R_th_jc ──▶ T_case ── R_th_cs ──▶ T_sink ── R_th_sa ──▶ T_amb
```
| Resistenza termica | Simbolo | Tipico | Note |
|--------------------|---------|--------|------|
| Giunzione–case | $R_{th(j-c)}$ | 0.5–5 °C/W | Dal datasheet |
| Case–sink | $R_{th(c-s)}$ | 0.1–1 °C/W | Pasta termica, pad, isolatore (mica, Sil-pad) |
| Sink–ambiente | $R_{th(s-a)}$ | 1–50 °C/W | **Dipende da dissipatore + airflow** |

### Calcolo dissipatore richiesto
$$R_{th(s-a)} \le \frac{T_{j,max} - T_a}{P_{diss}} - R_{th(j-c)} - R_{th(c-s)}$$

### Scelta dissipatore
- **Materiale**: Alluminio (leggero, economico), Rame (conduttività 2×, pesante)
- **Geometria**: Alette (fin) → massimizza area superficiale $A_s$
- **Airflow**: Naturale (convezione) vs Forzato (ventola) → $R_{th}$ scende 5–10×
- **Montaggio**: Orizzontale (aletta verticale) per convezione naturale

> **Concetto:** ![[Pasted image 20260130001914.png]] (es. SOA BJT con derating termico)

---

## Safe Operating Area (SOA)

> Insieme di coppie $(V, I)$ per cui il dispositivo opera **senza danni** (istantaneo o cumulativo).

### Limiti SOA (tipici su datasheet)
| Limite | Origine | Forma sul piano $I$–$V$ |
|--------|---------|-------------------------|
| **Corrente max** $I_{max}$ | Bond wire, metallizzazione | Verticale $I = I_{max}$ |
| **Tensione max** $V_{max}$ | Breakdown giunzione | Orizzontale $V = V_{CEO}/V_{DSS}$ |
| **Potenza max** $P_{max}$ (DC) | Termico stazionario | Iperbole $V \cdot I = P_{max}$ |
| **Pulsata** ($t_p = 1\mu s, 1ms, 10ms$) | Termico transitorio | Iperbole più ampia |
| **Second Breakdown** (solo BJT) | Instabilità termica locale ad alta $V$, bassa $I$ | Curva discendente ripida a $V$ alto |

### BJT vs MOSFET – Comportamento termico

| Fenomeno | **BJT** | **MOSFET** |
|----------|---------|------------|
| Coeff. temp. guadagno | $\beta \uparrow$ con $T$ | — |
| Coeff. temp. $V_{BE}/V_{TH}$ | $V_{BE} \downarrow -2\text{mV/°C}$ | $V_{TH} \downarrow -4\text{mV/°C}$ |
| Coeff. temp. corrente (a $V$ costante) | **Positivo** ($I_C \uparrow$ con $T$) → **Thermal runaway** | **Negativo** ($I_D \downarrow$ con $T$ per $R_{DS(on)} \uparrow$) → **Autolimitante** |
| Second Breakdown | **Sì** (pericoloso ad alta $V$) | No (ma *spiral* a $V_{DS}$ alto + $T$ alto) |
| Parallelo | Difficile (current hogging) | Facile (current sharing per $R_{DS(on)} \uparrow$ con $T$) |

> **Rischio BJT**: $P \uparrow \to T_j \uparrow \to I_C \uparrow \to P \uparrow$ → **runaway distruttivo**  
> **MOSFET**: $T_j \uparrow \to R_{DS(on)} \uparrow \to I_D \downarrow$ (a $V_{GS}$ costante) → **auto-protezione**

> **Confronto SOA:** ![[Pasted image 20260130001914.png]] (BJT con second breakdown evidenziato)

---

## Derating (Declassamento)

> Operare il componente **sotto** i limiti nominali per aumentare affidabilità e margine.

| Parametro | Regola tipica derating |
|-----------|------------------------|
| **Tensione** | $V_{op} \le 0.7 \times V_{max}$ (80% per affidabilità alta) |
| **Corrente** | $I_{op} \le 0.5 \times I_{max}$ (50%) |
| **Potenza** | $P_{op} \le 0.5 \times P_{max}$ @ $T_a = 25^\circ\text{C}$; deratare linearmente a 0 @ $T_{j,max}$ |
| **Temperatura giunzione** | $T_j \le T_{j,max} - 20\text{–}30^\circ\text{C}$ |

### Curve derating tipiche (datasheet)
- $P_{max}$ @ $T_c = 25^\circ\text{C}$ → 0 @ $T_c = T_{j,max}$
- Lineare o curva (per second breakdown)

---

## Affidabilità – Metriche base

| Metrica | Definizione | Unità |
|---------|-------------|-------|
| **MTBF** (Mean Time Between Failures) | Tempo medio tra guasti (sistema riparabile) | Ore |
| **MTTF** (Mean Time To Failure) | Tempo medio al guasto (non riparabile, es. componenti) | Ore |
| **FIT** (Failure In Time) | $10^{-9}$ guasti/ora = 1 FIT | FIT |
| **Bathtub curve** | Tasso guasti: *infant mortality* → *useful life* (costante) → *wear-out* | — |

### Modelli accelerati (Arrhenius)
$$\lambda(T) = \lambda_0 \exp\left(\frac{E_a}{k}\left(\frac{1}{T_0} - \frac{1}{T}\right)\right)$$
- $E_a$: energia attivazione (es. 0.7 eV per diffusione, 1.1 eV per ossidazione)
- **Regola del pollice**: ogni $+10^\circ\text{C}$ → tasso guasti $\times 2$

---

## Protezioni pratiche

| Protezione | Implementazione |
|------------|-----------------|
| **Overcurrent** | Shunt + comparator / ADC + firmware / fuse / eFuse / hot-swap controller |
| **Overtemperature** | NTC su heatsink / sensore integrato MCU / thermal shutdown IC |
| **Overvoltage** | TVS diode, MOV, GDT, crowbar, clamp attivo |
| **Reverse polarity** | Diodo serie / MOSFET ideal diode / controller protezione |
| **ESD** | TVS / clamp su I/O, layout guard rings |
| **Watchdog** | IWDW (indipendente clock) + WWDG (window) → reset su fault SW |

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Dispositivi a semiconduttore - Diodi e Transistor]] — SOA BJT/MOSFET, thermal runaway, $R_{DS(on)}(T)$
- [[Amplificatori operazionali]] — Dissipazione stadio uscita, thermal shutdown, current limit
- [[Sistemi embedded e microcontrollori]] — $P = C V^2 f$, low-power modes, IWDG/WWDG
- [[Sensori e trasduttori]] — Autothermal heating (RTD, strain gauge), derating sensori
- [[Esempi circuiti risolti]] — Potenza su BJT switch, regolatore Zener