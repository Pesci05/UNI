# Automi e macchine a stati finiti

> Nota derivata da [[Informatica industriale]] — macro-argomento: **Automi e processi sincroni/asincroni**.

---

## Macchine a sistemi finiti (Automi)
Hanno una struttura rigida e il loro funzionamento viene descritto tramite grafici.

> **Riferimento slide:** [[02 - Automata and machines.pdf#page=31|02 - Automata and machines, pagina 31]]

---

## Processi sincroni / asincroni

### Sincrono
- Estremamente veloce e reattivo
- **Svantaggio:** spreco di risorse (busy-wait / polling continuo)

### Asincrono
- Implementabile tramite **`yield`** e **`sleep`**
- Il thread cede volontariamente la CPU mentre attende un evento
- Più efficiente per I/O e attese lunghe

> **Riferimento slide:** [[02 - Automata and machines.pdf#page=31|02 - Automata and machines, pagina 31]]

---

## Collegamenti
- [[Informatica industriale]] — Indice generale
- [[Programmazione parallela]] — Parallelismo e concorrenza
- [[Concorrenza e sincronizzazione]] — Modelli di concorrenza, mutex, semafori