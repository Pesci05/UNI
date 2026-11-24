# Analisi dei circuiti – Leggi fondamentali

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Kirchhoff, Ohm, serie/parallelo, superposizione, Thevenin/Norton**.

---

## Leggi di Kirchhoff

### Definizioni base
- **Nodo**: giunzione di 2 o più rami; in un nodo è presente un solo valore di tensione
- **Ramo**: percorso che collega 2 nodi; presenta un valore unico di corrente
- **Maglia**: percorso che parte da un nodo, passa per N nodi e torna al nodo di partenza

> **Riferimento slide:** [[01 - Nuts and Bolts of Electronics.pdf#page=8|01 - Nuts and Bolts of Electronics, pagina 8]]

### KCL – Legge di Kirchhoff alle correnti (nodi)
> La somma algebrica delle correnti in un nodo è nulla.

$$\sum_{\text{node}} I = 0$$

Correnti entranti = correnti uscenti (convenzione dei segni).

### KVL – Legge di Kirchhoff alle tensioni (maglie)
> La somma algebrica delle tensioni ai capi dei rami di una maglia è uguale a 0.

$$\sum_{\text{maglia}} V = 0$$

---

## Legge di Ohm

$$V = R I$$

- $V$: tensione ai capi del resistore [V]
- $I$: corrente che attraversa il componente [A]
- $R$: resistenza $[\Omega]$ — caratteristica principale del componente

> **Simbolo elettrico:** ![[Pasted image 20251124122228.png]]  
> **Simbolo alternativo:** ![[Pasted image 20251124181522.png]]

---

## Collegamenti serie / parallelo

### Serie (partitore di tensione)
- Stessa corrente in tutti gli elementi
- Tensioni diverse ai capi di ciascun elemento
- $R_{eq} = R_1 + R_2 + \dots$
- $V = R_{eq} \cdot I$

### Parallelo (partitore di corrente)
- Stessa tensione ai capi di tutti gli elementi
- Correnti diverse attraverso ciascun elemento
- $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$
- $R_{eq} = \frac{R_1 R_2}{R_1 + R_2}$ (per due resistenze)

> **Esempio visivo:** ![[Pasted image 20251220002240.png]]

> **Riferimento slide:** [[01 - Nuts and Bolts of Electronics.pdf#page=9|01 - Nuts and Bolts of Electronics, pagina 9]]

---

## Sovrapposizione degli effetti

Quando in un circuito sono presenti **più generatori** (tensione o corrente):
1. Si "spegnono" tutti i generatori tranne uno:
   - Generatore di tensione → cortocircuito (0 V)
   - Generatore di corrente → circuito aperto (0 A)
2. Si analizza il circuito semplificato
3. Si ripete per ogni generatore
4. Si sommano i risultati (attenzione a **polarità** di correnti e tensioni)

> Permette di studiare un **circuito complicato** dividendolo in **sottocircuiti semplici**.

---

## Circuiti equivalenti – Thevenin e Norton

### Teorema di Thevenin
> Un generico circuito lineare non dinamico osservato da due nodi può essere rappresentato da una **sorgente di tensione $V_{th}$ in serie con una resistenza $R_{th}$**.

### Teorema di Norton
> Lo stesso circuito può essere rappresentato da una **sorgente di corrente $I_{no}$ in parallelo con una resistenza $R_{no}$**.

$R_{th} = R_{no}$ (resistenza equivalente vista dai terminali con generatori spenti).

> **Schema riassuntivo:** ![[Pasted image 20251223183531.png]]

> **Riferimento slide:** [[01 - Nuts and Bolts of Electronics.pdf#page=22|01 - Nuts and Bolts of Electronics, pagina 22]]

---

## Convenzioni di potenza

$$P = V I$$ [Watt]

| Tipo | Descrizione |
|------|-------------|
| **Dissipativo** | Trasforma energia elettrica in altre forme (calore, luce, moto) — *assorbe potenza* |
| **Erogativo** | Trasforma altre forme di energia in elettrica — *fornisce potenza* |

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Componenti passivi - R, C, L e impedenza]] — R, C, L nel dominio AC
- [[Dispositivi a semiconduttore - Diodi e Transistor]] — Modelli non lineari
- [[Esempi circuiti risolti]] — Applicazioni pratiche (RC, Zener)