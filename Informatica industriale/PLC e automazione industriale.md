# PLC e automazione industriale

> Nota derivata da [[Informatica industriale]] — macro-argomento: **Programmable Logic Controllers, architettura, I/O, sensori/attuatori, alimentazione**.

---

## Cosa è un PLC

**PLC** = *Programmable Logic Controller* (nati fine anni '60).  
Controllori progettati per **stretta interazione con dispositivi elettrici**: sensori, attuatori, interruttori, relè.

### Differenze vs Microcontrollori / Microprocessori (MC/MPU)

| Aspetto | PLC | MCU/MPU |
|---------|-----|---------|
| **Target utente** | Non informatici (elettricisti, manutentori) | Sviluppatori software |
| **Linguaggi** | Grafici (Ladder, FBD, SFC), tabelle — standard IEC 61131-3 | C, C++, Rust, Python… |
| **Operazioni** | Semplici: aritmetica, logica, timer, contatori | Complesse, generiche |
| **Riprogrammabilità** | Online, senza strumenti HW dedicati | Richiede toolchain, flash |
| **Architettura** | Semplice, **no OS**, deterministica | RTOS / Linux / bare-metal |
| **Affidabilità** | **Più affidabili** (meno crash, watchdog HW, ridondanza) | Dipende da design SW |
| **Ambiente** | **Robusti**: vibrazioni, -40÷70°C, umidità, EMI | Commerciale/industriale (serve protezione) |
| **I/O nativi** | **Ricchi**: digitali, analogici, relay, contatori ad alta velocità | Limitati, serve shield/expansion |

> **Riferimento slide:** [[05 - Programmable logic controllers.pdf]]

---

## Struttura hardware PLC

```
┌─────────────────────────────────────┐
│            CPU MODULE               │
│  ┌─────────┐  ┌─────────────────┐  │
│  │ Processor│  │   Memory        │  │
│  │ (MPU)   │  │  (RAM, Flash,   │  │
│  │         │  │   EEPROM)       │  │
│  └────┬────┘  └────────┬────────┘  │
│       │                │           │
│       └──────┬─────────┘           │
│              ▼                     │
│       ┌─────────────┐              │
│       │  Backplane  │◄── Bus dati/indirizzi/controllo
│       │   Bus       │
│       └──────┬──────┘
└──────────────┼──────────────────────┘
               │
     ┌─────────┼─────────┐
     ▼         ▼         ▼
┌────────┐ ┌────────┐ ┌────────┐
│ I/O    │ │ I/O    │ │ Comm   │
│ Digital│ │ Analog │ │ Module │
└────────┘ └────────┘ └────────┘
```

> **Schema slide:** ![[Pasted image 20261117102522.png]]

---

## Sistema I/O

### Input — Isolamento e condizionamento
> **Critico:** segnali di campo possono avere tensioni > alimentazione PLC (es. 24 Vdc su ingresso 5 V).  
> **Soluzione:** **optoisolatori** / trasformatori / barriere galvaniche per proteggere CPU e referenziare a ground PLC.

> **Schema slide:** ![[Pasted image 20261117102704.png]]

### Sensori — Parametri di qualità
| Parametro | Significato |
|-----------|-------------|
| **Accuratezza** | Scarto max tra valore misurato e reale |
| **Range** | Min/max misurabile |
| **Tempo di risposta** | Ritardo tra variazione reale e segnale out |
| **Sensibilità** | Δoutput / Δinput (guadagno) |
| **Stabilità** | Deriva nel tempo/temperatura |
| **Ripetibilità** | Coerenza misure ripetute stesse condizioni |
| **Reliability** | MTTF, resistenza a guasti |

### Smart Sensor (tendenza recente)
- **Elaborazione on-board**: compensazione temperatura, linearizzazione, diagnostica
- Output **già ingegnerizzato** (es. 4–20 mA scalato, Modbus, IO-Link)
- PLC riceve **dato pronto**, niente conversioni SW

---

## Output — Latch e stadi di potenza

Il canale di uscita memorizza lo stato in un **latch** (flip-flop) pilotato da CPU, poi stadio di potenza:

| Tipo | Caratteristiche | Applicazioni tipiche |
|------|-----------------|----------------------|
| **Relè** (elettromeccanico) | Isolamento galvanico nativo, AC/DC, bassa velocità (~10 Hz), usura meccanica | Carichi AC, sicurezza, bassa frequenza |
| **Transistor** (BJT/MOSFET) | Solo DC, switching veloce (kHz–MHz), nessuna usura, serve protezione induttiva (flyback) | PWM, stepper, DC load veloci |
| **Triac** | Solo AC, switching a zero-crossing, niente parti mobili | Resistenze, lampade, motori AC monofase |
| **Attuatori** | Dispositivi finali: valvole, motori, cilindri, indicatori | — |

> **Schema slide:** ![[Pasted image 20261117103250.png]]

---

## Alimentazione I/O — Sourcing vs Sinking

| Modalità | Descrizione | Schema tipico |
|----------|-------------|---------------|
| **Sourcing (PNP)** | PLC **fornisce** corrente al carico (output = +Vdc). Carico collegato a GND. | `PLC OUT ───[LOAD]─── GND` |
| **Sinking (NPN)** | PLC **assorbe** corrente dal carico (output = GND). Carico collegato a +Vdc (esterno o PLC). | `+Vdc ───[LOAD]─── PLC OUT` |

> **Nota:** input seguono stessa logica (PNP = sensor sourcia in ingresso, NPN = sensor sinka da ingresso).  
> **Compatibilità:** PLC e sensori/attuatori devono concordare (PNP-PNP o NPN-NPN).

---

## Collegamenti
- [[Informatica industriale]] — Indice generale
- [[Ingegneria software embedded]] — PLC come embedded specializzato; HAL per astrazione I/O
- [[Concorrenza e sincronizzazione]] — Ciclo scan PLC = loop deterministico (simile a super-loop embedded)