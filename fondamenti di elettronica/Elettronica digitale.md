# Elettronica digitale

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Porte logiche, ALU, Encoder/Decoder, MUX/DEMUX, Logica combinatoria/sequenziale, Clock, Flip-flop, Registri, FSM, Microprocessori**.

---

## Fondamenti

- **Codifica binaria**: 1 = tensione alta (tip. 5V, 3.3V, 1.8V), 0 = tensione bassa (GND)
- **Porte logiche** base: NOT, AND, OR, NAND, NOR, XOR, XNOR
- Tutto si costruisce da **NAND** o **NOR** (funzionalmente complete)

---

## ALU – Unità Logico Aritmetica

Componente che esegue **operazioni aritmetiche e logiche** su **2 input** (numeri binari interi).

| Segnale | Ruolo |
|---------|-------|
| **Input A, B** | Operandi (es. 8/16/32/64 bit) |
| **Opcode** | Codice operazione (ADD, SUB, AND, OR, XOR, SHIFT, COMPARE…) |
| **Carry-in / Flag-in** | Riporto/flag da ALU precedente (cascata) |
| **Output** | Risultato operazione |
| **Flag out** | Carry, Zero, Negative, Overflow, Parity… |

> **Schema:** ![[Pasted image 20260130174742.png]]

---

## Encoder / Decoder

### Encoder
- Input: $2^n$ linee (**one-hot**: una sola a 1)
- Output: $n$ bit = posizione del bit a 1
- Input non one-hot → output scartato

> **Schema:** ![[Pasted image 20260130180617.png]]

### Decoder
- Input: $n$ bit (binario)
- Output: $2^n$ linee **one-hot** (sola linea = input attiva)

> **Schema:** ![[Pasted image 20260130215448.png]]

---

## Multiplexer / Demultiplexer

### MUX (Multiplexer)
- $2^n$ ingressi dati
- $n$ ingressi **selezione**
- **1 uscita** = ingresso selezionato
- Permette: **1 linea condivisa → $2^n$ dispositivi** (con DEMUX simmetrico)

### DEMUX (Demultiplexer)
- 1 ingresso dati
- $n$ ingressi **controllo**
- $2^n$ uscite → dato indirizzato a una sola uscita

> **Schema MUX:** ![[Pasted image 20260130220308.png]]

---

## Logica combinatoria vs sequenziale

| Tipo | Descrizione | Memoria |
|------|-------------|---------|
| **Combinatoria** | Output = $f(\text{input})$ al tempo $t$ | No |
| **Sequenziale** | Output = $f(\text{input}_t, \text{stato}_{t-1})$ | **Sì** (flip-flop, registri) |

---

## Clock – Sincronizzazione

Segnale periodico (quadrato) per **sincronizzare** la logica sequenziale.

### Generazione
| Metodo | Descrizione |
|--------|-------------|
| **Cristallo di quarzo** | Oscillatore piezoelettrico, frequenza stabile/precisa (MHz–GHz) |
| **Ring Oscillator** | Catena dispari di porte NOT → ritardo propagazione → auto-oscillazione | 
| **RC / LC** | Meno precisi, per basse frequenze |

> **Ring oscillator:** ![[Pasted image 20260130222624.png]]
> Frequenza $\propto 1 / (N \cdot t_{pd})$ — $N$ = #porte (dispari)

---

## Flip-flop

Elementi di memoria **edge-triggered** (cambiano su fronte salita/discesa clock).

### JK Flip-flop
| Ingressi | Uscite |
|----------|--------|
| **J** (set), **K** (reset) | **Q**, $\overline{Q}$ |
| Clock (fronte ↑ o ↓) | Cambio stato su fronte |

> **Tabella verità JK:**
| J | K | Q(t+1) |
|---|---|--------|
| 0 | 0 | Q(t) (hold) |
| 0 | 1 | 0 (reset) |
| 1 | 0 | 1 (set) |
| 1 | 1 | $\overline{Q(t)}$ (toggle) |

> **Simboli/timing:** ![[Pasted image 20260130231529.png]] ![[Pasted image 20260130231550.png]]

---

## Registri a scorrimento (Shift Registers)

Insieme di flip-flop **D** che condividono **stesso clock**; uscita di uno → ingresso del successivo.

| Tipo | Input | Output | Note |
|------|-------|--------|------|
| **SISO** | Seriale | Seriale | Distruttivo: dopo $N$ cicli dati persi |
| **SIPO** | Seriale | Parallelo | Conversione seriale→parallelo |
| **PISO** | Parallelo | Seriale | Richiede bit **LOAD/SHIFT** (AND gate su ingressi) |
| **PIPO** | Parallelo | Parallelo | Memoria parallela; si comporta come PISO/SIPO secondo LOAD/SHIFT |

> **Schemi:**
> SISO: ![[Pasted image 20260130232302.png]]
> SIPO: ![[Pasted image 20260130232355.png]]
> PISO: ![[Pasted image 20260130232507.png]]
> PIPO: ![[Pasted image 20260130233942.png]]

### Bidirezionali
Architettura **PISO** con collegamento uscita→ingresso successivo **in entrambe le direzioni**; bit **DIR** (shift left/right) sostituisce LOAD/SHIFT.

> **Schema:** ![[Pasted image 20260130234633.png]]

---

## Macchine a stati finiti (FSM)

- **Stati** codificati in binario ($N$ stati → $\lceil \log_2 N \rceil$ flip-flop)
- **Transizioni**: prossimo stato = $f(\text{stato attuale}, \text{input})$
- **Output**: Mealy (dipende da input+stato) o Moore (solo stato)
- Implementazione: **registro stato** + **logica combinatoria** next-state/output

> **Concetto:** stato+input → next state (+output)

---

## Microprocessori / Microcontrollori

| Aspetto | Microprocessore (MPU) | Microcontrollore (MCU) |
|---------|----------------------|------------------------|
| **Core** | CPU sola | CPU + periferiche + memorie |
| **Memoria** | Esterna (DRAM, Flash) | **SRAM** (dati, volatile) + **FLASH** (codice, non-volatile) on-chip |
| **I/O** | Via bus esterno | **Periferiche integrate** (GPIO, UART, SPI, I²C, ADC, PWM, timer…) |
| **Architettura** | Von Neumann / Harvard | Spesso **Harvard modificato** (bus separati codice/dati) |
| **ISA** | CISC (x86) o RISC (ARM, RISC-V) | **RISC ridotto** (ARM Cortex-M, RISC-V, AVR, PIC…) → basso costo/energia |
| **Applicazioni** | Computer, server, smartphone | **Embedded**, IoT, automotive, industrial, wearable |

> **Schema MCU:** ![[Pasted image 20260131155901.png]]

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Dispositivi a semiconduttore - Diodi e Transistor]] — Implementazione porte (CMOS, TTL), driver potenza
- [[Amplificatori operazionali]] — Comparatori per ADC, clock recovery
- [[Sistemi embedded e microcontrollori]] — Architettura MCU, periferiche, programmazione, low-power
- [[Sensori e trasduttori]] — Interfaccia digitale sensori (I²C, SPI, 1-Wire)