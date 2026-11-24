# Programmazione parallela

> Nota derivata da [[Informatica industriale]] — macro-argomento: **Parallel computing, architetture, modelli di threading, work partitioning**.

---

## Parallel vs Distributed Computing

| Tipo | Descrizione |
|------|-------------|
| **Parallel Computing** | Stesso computer, più processi/thread |
| **Distributed Computing** | Più computer collegati in rete |

---

## Obiettivi del parallelismo

- **Speed-up**: risolvere lo **stesso** algoritmo in meno tempo
- **Scale-up**: risolvere problemi **più grandi** dividendoli in sottoproblemi

---

## Perché si preferisce il parallelo

1. **Economico**  
   Il costo di un processore single-core più veloce cresce esponenzialmente; i multi-core offrono migliore rapporto prezzo/prestazioni.

2. **Fisico (leggi di Moore e Dennard)**  
   - **Legge di Moore**: densità transistor raddoppia ~ogni 2 anni  
   - **Legge di Dennard** (scaling): riducendo dimensioni, potenza per transistor scala ~costante → **non più vera** dal ~2005 (power wall, frequency wall)  
   → Aumentare clock non scala più; serve parallelismo.

> **Conseguenza:** le architetture cambiano e **il programma deve sfruttarle esplicitamente**. Il programmatore **deve conoscere l'architettura target**.

---

## Legge di Amdahl

> Per quanto un programma sia parallelizzabile, esisterà sempre una **porzione seriale fissa** che limita lo speed-up massimo.

$$S_{\text{max}} = \frac{1}{(1 - p) + \frac{p}{N}}$$
- $p$ = frazione parallelizzabile  
- $N$ = numero di processori  
- $(1-p)$ = porzione seriale (collo di bottiglia)

---

## Tipi di multiprocessore

| Architettura            | Descrizione                                                                              | Schema                               |
| ----------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------ |
| **Simmetrico (SMP)**    | Tutti i core uguali, connessi via bus condiviso                                          | ![[Pasted image 20261005151438.png]] |
| **Asimmetrico (AMP)**   | Core divisi in sottosistemi (es. big.LITTLE ARM), velocità/architetture diverse          | ![[Pasted image 20261005151457.png]] |
| **Memoria distribuita** | Ogni core ha cache locale; gerarchia: L1/L2 (veloci, piccole) → L3 → RAM (lenta, grande) | —                                    |

> **Riferimento slide:** [[07 - Parallel programming.pdf#page=20|07 - Parallel programming, pagina 20]]

---

## Definizioni fondamentali

| Termine | Definizione |
|---------|-------------|
| **Core** | Unità di calcolo con ALU, registri, cache locale |
| **Programma** | Implementazione statica di un algoritmo |
| **Processo** | Istanza in esecuzione di un programma (spazio indirizzi proprio) |
| **Thread** | Unità di esecuzione leggera dentro un processo (condivide memoria) |
| **Task** | Sottoinsieme di istruzioni / unità di lavoro assegnabile |

---

## Threading Model: Fork-Join

- Thread **master** genera thread **slave** via `fork`
- `join` sincronizza e raccoglie i risultati (attende terminazione slave)
- Modello naturale per ricorsione parallela (es. divide-et-impera)

---

## Divisione del lavoro (Work Partitioning)

Tre strategie principali:

1. **Data Parallelism** — Stesso codice su porzioni diverse dei dati  
2. **Task Parallelism** — Codici diversi su dati diversi/in dipendenza  
3. **Offloading** — Delegare calcolo a acceleratore (GPU, FPGA, ecc.)

---

### Data Parallelism (dettaglio)

- Dati divisi in **chunk** uguali: $chunk = \frac{N}{T}$  
  - $N$ = elementi totali  
  - $T$ = thread
- Ogni thread deve conoscere il proprio **ID** per calcolare offset inizio/fine
- **Problema:** *load imbalance* → alcuni chunk richiedono più tempo → thread finiti prima restano inattivi  
  ![[Pasted image 20261020104024.png|427]]

#### Soluzione: Work Queue dinamica
- Lavoro visto come **unità atomiche** in coda thread-safe
- Primitive: `q_push` (producer), `q_pop` (consumer)
- Nessun thread sta fermo finché c'è lavoro  
  ![[Pasted image 20261020104300.png|339]]

---

## Tassonomia modelli di threading e sincronizzazione

| Creational Threading | Synchronization |
|----------------------|-----------------|
| Fork-join | Barrier |
| Master-slave | Critical-section / Atomic |
| Team of threads | Locks, Semaphores, Mutexes |

| Work Partitioning | Behavioral |
|-------------------|------------|
| Data-parallelism | Producer-Consumer |
| Reduction | Collaborative |
| Tasking / Queue | Competitive |
| Offloading | |

---

## Collegamenti
- [[Informatica industriale]] — Indice generale
- [[Concorrenza e sincronizzazione]] — Primitive di sincronizzazione, mutex, semafori, pattern
- [[GPGPU e calcolo su GPU]] — Offloading su GPU