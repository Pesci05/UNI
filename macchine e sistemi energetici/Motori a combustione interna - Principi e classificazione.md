# Motori a combustione interna – Principi e classificazione

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Definizione, classificazione, grandezze geometriche, diagramma indicatore, fasi reali**.

---

## Definizione e principio di funzionamento

**Motore a combustione interna (MCI)** / **motore endotermico** = macchina termica **volumetrica a flusso periodico** che converte energia chimica combustibile → energia meccanica.

| Aspetto | Descrizione |
|---------|-------------|
| **Sorgente calore** | Generata **all'interno del fluido** per combustione combustibile + aria (comburente) |
| **Trasformazione energia** | Combustione → ↑ $p,T$ fluido → espansione in cilindro → pistone → biella-manovella → albero motore |
| **Variazione fluido** | **Massa** varia (aspirazione/scarico), **composizione chimica** varia (reagenti → prodotti) |

> **Schema principio:** ![[Pasted image 20261024183634.png|488]] ![[Pasted image 20261024184044.png]]

---

## Classificazione principale

| Criterio | Categorie |
|----------|-----------|
| **Numero tempi** | **4 Tempi** (2 giri albero: aspirazione, compressione, espansione/combustione, scarico) — **2 Tempi** (1 giro, lavaggio/scarico integrati) |
| **Accensione** | **AS** = Accensione per Scintilla (Otto/benzina) — **AC** = Accensione per Compressione (Diesel) |
| **Ciclo termodinamico** | **Otto** (miscela premiscelata omogenea, fronte fiamma, numero ottano) — **Diesel** (solo aria compressa, iniezione diretta, carica disomogenea, autoaccensione, numero cetano) — **Sabathé** (misto) |
| **Architettura** | In linea, V, W, boxer (cilindri contrapposti) |

---

## Grandezze geometriche fondamentali

| Simbolo | Nome | Definizione / Formula |
|---------|------|----------------------|
| **PMS** | Punto Morto Superiore | Pistone più vicino alla testa |
| **PMI** | Punto Morto Inferiore | Pistone più lontano dalla testa |
| $D$ | **Alesaggio** | Diametro interno cilindro |
| $C$ | **Corsa** | Distanza PMS–PMI |
| $V_c$ | **Cilindrata unitaria** | $V_c = \frac{\pi D^2}{4} \cdot C$ |
| $V_0$ | **Volume camera combustione** (nocivo) | Volume residuo a PMS |
| $\beta$ (o $r$) | **Rapporto volumetrico compressione** | $\beta = \frac{V_0+V_c}{V_0} = \frac{V_1}{V_2}$ |

---

## Diagramma di indicatore (4 tempi)

Grafico **$p-V$** per un ciclo completo (2 giri = 720°).

> **Schema confronto ideale/teorico/reale:** ![[diagramma_indicatore_4tempi_confronto-v2.png]]

### Differenza: Ciclo termodinamico vs Diagramma indicatore
Il diagramma **NON è un ciclo termodinamico puro** perché:
- Fluido varia in **massa** (aspirazione/scarico)
- Fluido varia in **composizione** (combustione)
- Trasformazioni **lontano dall'equilibrio**, scambio termico reale con pareti

**Lavoro indicato** = area racchiusa:
$$L_i = \oint p\,dV$$

---

### Due cappi (anelli)

| Cappo | Lavoro | Descrizione |
|-------|--------|-------------|
| **Utile (Superiore)** | Positivo | Combustione + espansione |
| **Pompaggio (Inferiore)** | Negativo | Aspirazione + scarico (rinnovo carica) |

---

### Le 4 fasi reali

#### 1. Aspirazione (PMS → PMI)
- Pistone scende, pressione cilindro **< $p_a$** (depressione)
- Vince perdite carico condotti aspirazione

#### 2. Compressione (PMI → PMS)
- Valvola aspirazione chiusa, pistone risale → lavoro sul fluido
- ↑ $p$, ↑ $T$ (trasf. reale compressione)
- **Accensione/Iniezione prima PMS** (anticipo: compensa tempi chimico-fisici)

#### 3. Combustione ed Espansione (PMS → PMI)
- Liberazione calore rapida → $p_{max}$
- Gas ad alta $p,T$ si espandono → spingono pistone → **lavoro utile**
- Durante espansione: ↓ $p$, ↓ $T$ cedono lavoro

#### 4. Scarico (PMI → PMS)
- **AAS** (anticipo apertura scarico): valvola apre prima PMI → pressione crolla a $p_a$
- Pistone risale spinge gas residui → pressione cilindro **> $p_a$** (sovrappressione scarico)

---

## Diagramma Ideale vs Teorico vs Reale

| Livello | Ipotesi | Differenze chiave |
|---------|---------|-------------------|
| **Ideale** | Gas perfetto, $c_p,c_v$ costanti, isoentropiche compressione/espansione, combustione isocora/isobara, aspirazione/scarico a $p_a$ esatta, **no lavoro pompaggio** | Modello base per formule rendimento |
| **Teorico / Limite** | Fluido **reale** ($c_p,c_v=f(T)$), dissociazioni chimiche ad alta $T$ | ↓ $p_{max},T_{max}$ vs ideale |
| **Reale (Effettivo)** | **Arrotondamento curve** (combustione non istantanea, valvole non immediate), **fasatura valvole reali** (AAA, RCS, RCA, AAS), **lavoro pompaggio $P$** (perdite carico, farfalla) | $L_{netto} = A - P$ |

> **Angolo incrocio** (AAA + RCS): sfrutta inerzia gas per ↑ lavaggio, ↑ richiamo aria fresca, ↓ lavoro pompaggio

> **RCA**: inerzia masse → ↑ riempimento  
> **AAS**: ↓ pressione prima PMI → ↓ lavoro pompaggio (costo: piccola perdita lavoro espansione)

---

## Pressione media indicata

Per confrontare motori diverse cilindrate:
$$P_{mi} = \frac{L_i}{V_c} = \frac{1}{V_c}\oint p\,dV$$

Pressione costante ipotetica che, agendo su una corsa espansione, dà stesso lavoro netto del ciclo reale.

---

## Collegamenti
- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Cicli termodinamici MCI (Otto, Diesel, Sabathé) e rendimenti]] — Modelli ideali per calcolo rendimenti
- [[Combustione, emissioni e post-trattamento MCI]] — Processi combustione reale, anomalie, inquinanti
- [[Termodinamica di base]] — 1°/2° principio, funzioni stato, lavoro espansione/compressione
- [[Layout cogenerativi dettagliati (TG, TV, CCGT, MCI)]] — MCI in cogenerazione (recupero fumi + acqua camicia)