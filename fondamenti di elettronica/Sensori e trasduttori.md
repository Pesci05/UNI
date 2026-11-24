# Sensori e trasduttori

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Temperatura, Forza/Coppia, Posizione, Accelerazione, Magnetici, Corrente — principi, modelli, tipologie, condizionamento**.

---

## Definizioni

| Termine | Significato |
|---------|-------------|
| **Trasduttore** | Dispositivo che converte energia da una forma a un'altra |
| **Sensore** | Trasduttore che converte **grandezza fisica** → **segnale elettrico** |
| **Attuatore** | Trasduttore che converte **segnale elettrico** → **azione fisica** |

> **Riferimento lab:** [[Lezione_Lab_1.pdf#page=14|Lezione_Lab_1, page 14]]

---

## Caratteristiche dei trasduttori

### Statiche
| Parametro | Descrizione |
|-----------|-------------|
| **SPAN** | Intervallo grandezza ingresso con comportamento nominale |
| **FONDO SCALA (FS)** | Escursione uscita per span ingresso |
| **SENSIBILITÀ** | $\Delta U_{out} / \Delta X_{in}$ (pendenza curva taratura) |
| **RISOLUZIONE** | Minima variazione ingresso rilevabile |
| **LINEARITÀ** | Scarto max da retta ideale (es. % FS) |
| **OFFSET** | Uscita a ingresso = 0 |
| **STABILITÀ** | Deriva parametri nel tempo/temperatura |
| **ISTERESI** | Differenza uscita per stesso ingresso (salita vs discesa) |
| **SELETTIVITÀ** | Reiezione grandezze parassite |
| **EFFETTI DI CARICO** | Influenza impedenza ingresso su sorgente |

### Dinamiche
| Parametro | Descrizione |
|-----------|-------------|
| **Funzione di trasferimento** | $H(s) = U_{out}(s) / X_{in}(s)$ |
| **Risposta al gradino** | Tempo salita, assestamento, overshoot |
| **Risposta in frequenza** | Banda passante ($-3\text{dB}$), risonanze |

### Affidabilità
| Parametro | Descrizione |
|-----------|-------------|
| **Durata nominale** | Ore/cicli attesi |
| **Cicli fondo scala** | Cicli a range max |
| **Tolleranza guasti** | Degradazione graduale vs catastrofica |

---

## Sensori di temperatura

| Tipo | Principio | Range tipico | Note |
|------|-----------|--------------|------|
| **Termocoppie** | Effetto Seebeck (giunzione 2 metalli) | $-200\dots+1800^\circ\text{C}$ | $V = S \Delta T$, serve giunzione fredda di riferimento |
| **RTD** (Pt100, Pt1000) | $R(T) = R_0[1 + \alpha(T-T_0)]$ | $-200\dots+850^\circ\text{C}$ | Precisione $\pm0.1^\circ\text{C}$, **autoriscaldamento** ($I^2R$) |
| **Termistori NTC/PTC** | Semiconduttore, $R \propto e^{\beta/T}$ | $-50\dots+150^\circ\text{C}$ | Alta sensibilità, non lineari |
| **Sensori integrati** (LM35, TMP36, DS18B20) | Banda proibita / $\Delta V_{BE}$ | $-55\dots+150^\circ\text{C}$ | Uscita analogica/digitale, calibrati, basso costo |
| **Pirometri** | Radiazione IR (Planck) | $>500^\circ\text{C}$ | Senza contatto, emissività critica |

### Termocoppie – Tipi comuni
| Tipo | Materiali | Sensibilità | Applicazione |
|------|-----------|-------------|--------------|
| **E** | Chromel–Costantana | $\approx 68\mu\text{V/}^\circ\text{C}$ | Criogenico, alta sensibilità |
| **J** | Ferro–Costantana | $\approx 52\mu\text{V/}^\circ\text{C}$ | Generico, range limitato ($\le 750^\circ\text{C}$) |
| **K** | Chromel–Allumel | $\approx 41\mu\text{V/}^\circ\text{C}$ | **Più usato**, economico, ampio range ($-200\dots+1260^\circ\text{C}$) |

> **Riferimento:** $V = S \Delta T$ (Seebeck coefficient $S$)

---

## Sensori di forza e coppia

### Estensimetri (Strain Gauge)
- **Principio**: deformazione metallo → $\Delta R/R = G_f \cdot \varepsilon$
  - $G_f$ = gauge factor (tip. 2 per metallo, 100+ per semiconduttore)
  - $\varepsilon = \Delta L / L$ = deformazione unitaria
- **Configurazione**: **ponte di Wheatstone** (1/2/4 attivi) per compensazione temperatura e amplificazione
- **Applicazione**: celle di carico, pressione, coppia, accelerometri piezoresistivi

> **Schema deformazione:** ![[Pasted image 20260201214206.png]]  
> **$\Delta R$ vs deformazione:** ![[Pasted image 20260201214423.png]]

### Piezoelettrici (forza)
- Carica generata $\propto$ forza applicata ($Q = d_{33} F$)
- **Solo dinamico** (alta impedenza → scarica per leakage)
- Alta frequenza, no DC

### Coppia su albero rotante
| Soluzione | Principio | Problema | Soluzione |
|-----------|-----------|----------|-----------|
| **Estensimetri** | $\Delta R$ su albero | Fili si aggrovigliano | Telemetria induttiva / slip ring / wireless |
| **Ottici** | Disco led/fotodiodi | Costo, fragilità | — |
| **Magnetostrittivi** | $\Delta \mu$ vs tensione | — | Robusti |

---

## Sensori di posizione

### Potenziometri
- Resistore 3 terminali, cursore scorrevole/rotante
- $V_{out} = \frac{x}{L} V_{in}$ (ideale)
- **Limiti**: usura meccanica, risoluzione limitata, rumore contatto, potenza dissipata

> **Schema:** ![[Pasted image 20260315214602.png]]

### Encoder

#### Incrementale
- Disco opaco con $n$ fori + LED + fotodiodo
- $n$ impulsi/giro → risoluzione $r = 360^\circ/n$
- **Richiede**: contatore + **starter** (riferimento zero) + **direzione** (2 canali in quadratura A/B 90°)

> **Schema:** ![[Pasted image 20260315224549.png]]

#### Assoluto
- $k$ anelli concentrici, fori con codice **binario / Gray / ASCII**
- $k$ coppie LED/fotodiodo → parola $k$ bit = posizione **assoluta** (no contatore, no starter)
- Gray code: 1 bit cambia per passo → no errori transitori

> **Schema:** ![[Pasted image 20260315230549.png]]
> **Confronto:** assoluto costa più, range temp. limitato (80–100°C), montaggio delicato
> **Variante magnetica**: più robusta, durata >, range temp. >, uscita analogica/digitale

### Resolver
- **Trasduttore angolare ad induzione magnetica** (robusto, automotive, EV/HEV)
- **Rotore**: bobina eccitazione AC → campo magnetico rotante
- **Statore**: 2 bobine ortogonali (sin/cos) → tensioni indotte
  $$V_{gen}(t) = E_0 \sin(\omega t + \rho)$$
  $$V_{ind}(t) = E_0 \cos(\alpha) \sin(\omega t + \rho)$$
- Angolo $\alpha$ recuperato da rapporto ampiezze sin/cos (RDC: Resolver-to-Digital Converter)

> **Schema:** ![[Pasted image 20260316235422.png]]

---

## Sensori di accelerazione

| Tipo | Principio | DC? | Note |
|------|-----------|-----|------|
| **Piezoelettrico** | Carica vs forza inerziale | **No** (alta $f_{min}$) | Alta sensibilità, ampio range T, serve cablaggio speciale |
| **Piezoresistivo** | $\Delta R$ su membrana | **Sì** | Immunità campi E, sensibilità a T |
| **Capacitivo (MEMS)** | $\Delta C$ massa-molla | **Sì** | **Standard** (airbag, phone, IoT), integrato CMOS |
| **Termico** | Convezione gas vs accelerazione | Sì | Basso costo, bassa banda |
| **Ottico/Fibra** | Interferometria | Sì | Alta precisione, immune EMI |

### MEMS Accelerometro (capacitivo)
- **Massa mobile** con dita interdigitate + **dita fisse** → condensatori differenziali
- $C = \frac{A \epsilon_0}{t}$ → accelerazione $\to$ spostamento massa $\to$ $\Delta t$ $\to$ $\Delta C$
- **Condizionamento**: misura impedenza / $\Sigma\Delta$ / switched-cap → digitale
- **Molte lamelle** in parallelo → massimizza $A_{eq}$ e sensibilità
- Progettato per minimizzare forze elettrostatiche parassite

> **Struttura:** ![[Pasted image 20260318002549.png]]  
> **Applicazioni MEMS:** airbag, ESC, droni, smartphone, wearable, medicale, energy harvesting, ultrasuoni, microfoni, altoparlanti

---

## Sensori magnetici

### Hall
- **Forza di Lorentz**: $\vec{F} = q \vec{v} \times \vec{B}$
- Film conduttivo spessore $s$, corrente $I$ (fronte-retro), campo $B$ (⊥) → tensione Hall laterale
  $$V_H = K B I = \frac{\mu_q \rho}{s} B I$$
  $$R_H = \frac{V_H}{I} = \frac{\mu_q \rho}{s} B$$
- **Usi**: current sensing (contactless), position, speed, inverter motori
- **Limite**: deriva per campi forti/prolungati → **feedback compensation**

> **Geometria:** ![[Pasted image 20260319231200.png]]  
> **Current sensor con feedback:** ![[Pasted image 20260319234333.png]]
> $$I = V_{out} \frac{N}{R_L}$$ (dopo compensazione)

### Magnetoresistivi (AMR, GMR, TMR)
- **Disco di Corbino**: anelli conduttivi + materiale magnetoresistivo
- Senza $B$: corrente radiale ($R = R_0$)
- Con $B$: deviazione Lorentz → percorso più lungo → $R > R_0$ (quadratico in $B$)
- **Non danno direzione** (salvo configurazione bridge/push-pull)
- Sensibili a temperatura

> **Schema:** ![[Pasted image 20260322001246.png]]

### Magnetostrittivi
- $\Delta$ forma/dimensioni vs magnetizzazione
- Usati per posizione lineare (guided wave), corrente (giungla)

---

## Sensori di corrente

### Shunt (resistore Kelvin 4 terminali)
- $R \ll 1\Omega$ (es. $100\mu\Omega$–$10\text{m}\Omega$)
- $V_{drop} = I R$ → amplificato (instrumentation amp)
- **Problema**: resistenze contatti ($r$) paragonabili a $R$
  $$I = \frac{V}{R + 2r}$$
- **Soluzione**: **resistore Kelvin** — 2 terminali **corrente** (portano $I$), 2 terminali **tensione** (misurano $V$ su $R$ solo, materiali bassa $\rho$)

> **Equazione corretta:** $I = V_{sense} / R_{shunt}$ (esclude $r$)

### Trasformatori di corrente (CT)
- **Solo AC** (no DC)
- Primario = cavo passante (1 spira), secondario = $N$ spire → $I_{sec} = I_{prim} / N$
- **Burden resistor** su secondario → tensione misurata
- Isolamento galvanico intrinseco, banda limitata (niente DC, saturazione core)

### Rogowski Coil
- Bobina aria (no core) → $V_{out} \propto dI/dt$ → **integratore** per $I(t)$
- Solo AC, flessibile, nessun saturazione, banda ampia

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Componenti passivi - R, C, L e impedenza]] — Ponte Wheatstone, condizionamento RC, integratori
- [[Amplificatori operazionali]] — Amplificatori strumentazione (shunt, bridge), filtri anti-aliasing, condizionamento piezo/termocoppia
- [[Dispositivi a semiconduttore - Diodi e Transistor]] — Driver LED/laser, protezione ingressi, switch sensori
- [[Elettronica digitale]] — Interfacce I²C, SPI, 1-Wire, UART, Manchester, SENT
- [[Sistemi embedded e microcontrollori]] — ADC (SAR, $\Sigma\Delta$), DMA, timer capture, comparator, PGA interno
- [[Potenza, termica e affidabilità]] — Autothermal heating (RTD, strain gauge), derating, MTBF sensori