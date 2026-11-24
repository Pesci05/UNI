# Componenti passivi – R, C, L e impedenza

> Nota derivata da [[Fondamenti di Elettronica]] — macro-argomento: **Resistori, Condensatori, Induttori, Impedenza complessa, Fasori, Risposta AC**.

---

## Resistori

### Legge di Ohm
$$V = R I$$

### Collegamenti
- **Serie**: $R_{eq} = \sum R_i$, partitore di tensione
- **Parallelo**: $\frac{1}{R_{eq}} = \sum \frac{1}{R_i}$, partitore di corrente

> **Simboli:** ![[Pasted image 20251124122228.png]] ![[Pasted image 20251124181522.png]]

---

## Condensatori

### Equazione costitutiva
$$I = C \frac{dV}{dt}$$
$$Q = C V$$

- $C$: capacità [Farad = Coulomb/Volt]
- La carica varia **solo se** la tensione varia nel tempo

> **Simbolo:** ![[Pasted image 20251220004408.png]]  
> **Struttura fisica:** ![[Pasted image 20251220002533.png]]

### Carica / scarica (circuito RC)
Vedi [[Esempi circuiti risolti#ES. carica scarica di un condensatore|Esempio dettagliato]]:
- $V_c(t) = V_b [1 - e^{-t/RC}]$ (carica)
- $\tau = RC$ costante di tempo
- A $t = \tau$: 63% carica; a $t = 3\tau$: 95%

---

## Induttori

### Equazione costitutiva
$$V = L \frac{dI}{dt}$$

- $L$: induttanza [Henry = Volt·secondo/Ampere]
- Immagazzina **energia magnetica**

> **Simbolo:** ![[Pasted image 20251221225027.png]]

---

## Segnali AC e Impedenza

### Segnali
| Tipo | Descrizione |
|------|-------------|
| **DC** (Direct Current) | Tensione e corrente costanti — **retta** |
| **AC** (Alternating Current) | Variano nel tempo, forma sinusoidale — sovrapposizione di **onde sinusoidali** (analisi di Fourier) |

> **Riferimento:** [[01 - Nuts and Bolts of Electronics.pdf#page=23|pagina 23]]  
> **Spettro Fourier:** ![[Pasted image 20260119223546.png]]  
> **Onda sinusoidale:** ![[Pasted image 20260119183941.png]]

---

### Risposta in frequenza dei componenti

| Componente | Relazione $V/I$ | Sfasamento | Nota |
|------------|-----------------|------------|------|
| **Resistore** | $R$ (reale) | $0^\circ$ | Ampiezza $I \propto 1/R$, stessa frequenza |
| **Condensatore** | $\frac{1}{j\omega C} = -j\frac{1}{\omega C}$ | Corrente **anticipa** tensione di $90^\circ$ | $|I| = \omega C |V|$ |
| **Induttore** | $j\omega L$ | Tensione **anticipa** corrente di $90^\circ$ | $|V| = \omega L |I|$ |

> **Grafici confronto:** ![[Pasted image 20260120175933.png|361]] ![[Pasted image 20260120214010.png]]

---

### Impedenza complessa (notazione fasoriale)

$$\begin{aligned}
Z_R &= R \\
Z_C &= -j\frac{1}{\omega C} = \frac{1}{j\omega C} \\
Z_L &= j\omega L \\
\omega &= 2\pi f \quad \text{(pulsazione)}
\end{aligned}$$

> **Riferimento slide:** [[01 - Nuts and Bolts of Electronics.pdf#page=27|pagina 27]], [[01 - Nuts and Bolts of Electronics.pdf#page=28|pagina 28]]

### Rappresentazione piano complesso
- Resistori → asse reale
- Condensatori → asse immaginario negativo ($-j$)
- Induttori → asse immaginario positivo ($+j$)

> **Diagramma impedenze:** ![[Pasted image 20260120223658.png]] ![[Pasted image 20260126225844.png]] ![[Pasted image 20260127163232.png]]

---

### Legge di Ohm estesa (dominio fasoriale)
$$\tilde{V} = \tilde{Z} \tilde{I}$$

Tutte le regole per resistenze (serie, parallelo, partitori, Thevenin/Norton) si applicano **identicamente** usando $\tilde{Z}$ al posto di $R$.

---

## Collegamenti
- [[Fondamenti di Elettronica]] — Indice generale
- [[Analisi dei circuiti - Leggi fondamentali]] — KCL, KVL, superposizione, Thevenin/Norton
- [[Dispositivi a semiconduttore - Diodi e Transistor]] — Modelli dinamici (capacità parassite)
- [[Esempi circuiti risolti]] — Circuito RC nel dominio temporale