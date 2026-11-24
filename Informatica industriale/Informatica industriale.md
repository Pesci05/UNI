# Informatica industriale — Indice

Questa nota funge da **indice navigabile** agli argomenti principali del corso.  
Ogni voce linka una nota dedicata con una sintesi dell'argomento.

---

## [[Automi e macchine a stati finiti]]
> Macchine a sistemi finiti (automi), processi sincroni vs asincroni, `yield`/`sleep`, riferimenti a *Automata and machines*.

## [[Programmazione parallela]]
> Parallel vs distributed computing, speed-up vs scale-up, legge di Amdahl, architetture simmetriche/asimmetriche/distribuite, modelli di threading (fork-join, master-slave), data/task parallelism, work queue dinamica, strategie di partitioning.

## [[Concorrenza e sincronizzazione]]
> Concorrenza competitiva vs cooperativa, modelli a message-passing (send/receive, RPC) e a memoria condivisa, mutua esclusione, atomicità, critical section, **semafori** (wait/signal, binari), **mutex**, pattern **producer/consumer**, deadlock e prevenzione.

## [[Ingegneria software embedded]]
> Principi **SOLID** adattati all'embedd (Single Responsibility, Interface Segregation, Dependency Inversion), **Design Patterns** (vocabolario condiviso, granularità, interfacce/moduli), **State Pattern** per FSM, **HAL** (Hardware Abstraction Layer: Proxy + Adapter).

## [[PLC e automazione industriale]]
> **PLC** (Programmable Logic Controllers): architettura no-OS, robustezza, I/O ricco. Struttura hardware (CPU, memoria, I/O), **sistema I/O** (isolamento input, smart sensor), **output** (relay, transistor, triac, attuatori), **alimentazione** sourcing/sinking.

## [[GPGPU e calcolo su GPU]]
> GPU come coprocessori per parallelismo massivo (NVIDIA, AMD, Intel), **OpenGL** per rendering, **General-Purpose GPU** per calcolo scientifico/data-center. Pipeline GPU (Fetch, Decode, Load, Execute multicore, Store), limitazione SIMT, **SM** (Streaming Multiprocessors), modelli programmazione (CUDA, HIP, SYCL, Metal).

---

## Riferimenti bibliografici condivisi
- [[02 - Automata and machines.pdf]]
- [[05 - Programmable logic controllers.pdf]]
- [[07 - Parallel programming.pdf]]
- [[08 - Concurrency.pdf]]