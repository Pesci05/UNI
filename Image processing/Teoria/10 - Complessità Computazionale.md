# Cenni di Complessità Computazionale

> **Slide:** [[10_Introduzione_complessita_computazionale.pdf]]
> **Indice:** [[IMAGE PROCESSING]]

La **complessità computazionale** misura quanto è efficiente un algoritmo, ovvero come varia il consumo di risorse temporali e di memoria in funzione della dimensione dell'input, **senza dipendere dallo specifico computer utilizzato**.

## Cosa si misura?
- **Complessità temporale**: numero di operazioni elementari eseguite.
- **Complessità spaziale**: quantità di memoria utilizzata.

Indichiamo con $n$ la dimensione dell'input (ad esempio, il numero di elementi di un array o il numero di pixel).

### A che cosa serve?
- Prevedere il consumo di risorse temporali e di memoria in funzione di $n$ (capire come "rallenta" un algoritmo al crescere dell'input).
- Confrontare algoritmi alternativi per lo stesso problema (es. convoluzione spaziale vs FFT in [[11 - Trasformata di Fourier#Vantaggi dei filtri tramite frequenze]]).
- Individuare le parti che dominano il costo computazionale (ad esempio i cicli).

## Costo computazionale $T(n)$
Per avere una stima **indipendente dalla specifica macchina**, non si misurano i secondi, ma il numero di operazioni atomiche:
- Si assume che ogni operazione *atomica* abbia **costo costante** uguale a $1$.
- $T(n)$ esprime il costo computazionale contando il numero di operazioni atomiche eseguite.

### Esempi pratici (Complessità Temporale)
1. **Un ciclo `for`:**
   ```python
   somma = 0
   for i in range(n):
       somma += A[i]
   ```
   Il corpo del ciclo viene eseguito $n$ volte $\to$ $T(n) = an + b$ (**crescita lineare**).

2. **Due cicli consecutivi:**
   Ogni ciclo esegue $n$ iterazioni $\to$ $T(n) = cn + d$ (**ancora lineare**: i costi dei blocchi consecutivi si **sommano**).

3. **Due cicli annidati:**
   Per ogni iterazione esterna, il ciclo interno esegue $n$ iterazioni $\to$ $n \times n = n^2$ (**crescita quadratica**: i costi dei cicli annidati si **moltiplicano**).

### Come si calcola in pratica
1. Definire $n$, la dimensione dell'input.
2. Contare quante volte vengono eseguite le operazioni principali.
3. **Sommare** i costi dei blocchi consecutivi.
4. **Moltiplicare** i costi dei cicli annidati.

## Notazione O grande (Big O)
$O(g(n))$ indica un **limite superiore asintotico** alla crescita del costo. Per calcolarlo si trascurano le **costanti moltiplicative** e i **termini di ordine inferiore** contenuti in $T(n)$:
- $T(n) = an + b \in O(n)$
- $T(n) = an^2 + bn + c \in O(n^2)$

Confronto asintotico (per $n$ sufficientemente grande):
$$
O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2)
$$

## Esempi di Complessità Spaziale
- `np.arange(n)` $\to$ costo spaziale $O(n)$
- `np.zeros((n, n), dtype=np.int32)` $\to$ costo spaziale $O(n^2)$
