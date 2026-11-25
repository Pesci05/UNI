# Cicli termodinamici MCI (Otto, Diesel, Sabathé) e rendimenti

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Cicli ideali, parametri Sabathé, formule rendimento, confronto Otto/Diesel, grandezze prestazionali, curve caratteristiche**.

---

## Cicli termodinamici ideali di riferimento

| Ciclo | Somministrazione calore $q_1$ | Modello |
|-------|-------------------------------|---------|
| **Otto (teorico)** | **Isocora** (volume costante) | Benzina/AS |
| **Diesel (teorico)** | **Isobara** (pressione costante) | Diesel/AC |
| **Sabathé (Misto/Dual)** | **Parzialmente isocora + parzialmente isobara** | Approssima meglio motori moderni |

> **Schema cicli ideali:** ![[Pasted image 20261025164235.png]]

### Fasi termodinamiche (comuni)
1. **Stato 1**: fluido dopo aspirazione
2. **1→2**: Compressione **isoentropica** (adiabatica reversibile) $pv^k=cost$, $k=c_p/c_v$
   - $p_2 = p_1 \beta^k$ con $\beta = V_1/V_2$
3. **2→3**: Somministrazione calore $q_1$ (da scambiatore ideale, no reazioni chimiche)
   - Otto: isocora ($V=cost$)
   - Diesel: isobara ($p=cost$)
   - Sabathé: 2→3′ isocora + 3′→3 isobara
4. **3→4**: Espansione **isoentropica** (lavoro utile)
5. **4→1**: Cessione calore $q_2$ all'esterno a volume costante (isocora) → ritorno stato 1

> **Piani $p-v$ e $T-s$:** ![[confronto_cicli_otto_diesel_sabathe_pv-v2.png]]

---

## Ciclo Sabathé – Parametri caratteristici

| Parametro | Formula | Significato |
|-----------|---------|-------------|
| **Rapporto compressione** | $\beta = \frac{V_1}{V_2}$ | Volumetrico |
| **Rapporto combustione volume costante** | $a = \frac{p_{3'}}{p_2} = \frac{T_{3'}}{T_2}$ | Quanto sale $p$ in fase isocora |
| **Rapporto combustione pressione costante** | $b = \frac{V_3}{V_{3'}} = \frac{T_3}{T_{3'}}$ | Quanto si espande in fase isobara |

> **Casi limite:** $b\to1$ → **Ciclo Otto**; $a\to1$ → **Ciclo Diesel**

---

## Calore introdotto e ceduto

| Ciclo | $q_1$ (calore introdotto) | $q_2$ (calore ceduto, tutti) |
|-------|---------------------------|------------------------------|
| **Otto** | $q_1 = c_v(T_3-T_2)$ | $q_2 = c_v(T_4-T_1)$ |
| **Diesel** | $q_1 = c_p(T_3-T_2)$ | $q_2 = c_v(T_4-T_1)$ |
| **Sabathé** | $q_1 = c_v(T_{3'}-T_2) + c_p(T_3-T_{3'})$ | $q_2 = c_v(T_4-T_1)$ |

---

## Rendimenti termodinamici

**Generale:** $\eta_{th} = \frac{L_{th}}{q_1} = 1 - \frac{q_2}{q_1}$

### Ciclo Sabathé
$$\eta_{th,S} = 1 - \frac{1}{\beta^{k-1}} \left[ \frac{a\cdot b^k - 1}{(a-1) + k\cdot a\cdot(b-1)} \right]$$

### Casi limite
- **Otto** ($b\to1$):
  $$\eta_{th,O} = 1 - \frac{1}{\beta^{k-1}}$$

- **Diesel** ($a\to1$):
  $$\eta_{th,D} = 1 - \frac{1}{\beta^{k-1}} \left[ \frac{b^k - 1}{k(b-1)} \right]$$

> **Proprietà matematica:** $\left[ \frac{b^k-1}{k(b-1)} \right] > 1$ per $b>1$  
> **Conseguenza:** A parità di $\beta$:
> $$\eta_{th,O} > \eta_{th,S} > \eta_{th,D}$$

---

## Confronto Benzina vs Diesel – La realtà inverte la teoria

> **Grafici confronto:** ![[confronto_rendimento_otto_diesel_beta.png]] ![[confronto_otto_diesel_ts_beta.png]] ![[confronto_otto_diesel_ts_completo-v3.png]]

### A parità di $\beta$ e $q_1$ (condizione teorica)
- $\eta_{th,O} > \eta_{th,D}$
- **Motivo (piano $T-s$)**: $T_{4D} > T_{4O}$ → $q_{2,D} > q_{2,O}$ → $\eta_D < \eta_O$

### A parità di $p_{max}$ e $q_1$ (**caso reale**, limite strutturale)
- **Condizione**: $p_{3,O}=p_{3,D}=p_{max}$, $q_{1,O}=q_{1,D}$
- **Esito**: $\eta_{th,D} > \eta_{th,O}$ (Diesel più efficiente nella pratica!)
- **Motivo**: 
  - Otto limitato da **detonazione** → $\beta$ basso (≈8÷12)
  - Diesel **senza carica premiscelata** → $\beta$ alto (≈14÷22)
  - A parità $p_{max}$: $T_{4D} < T_{4O}$ → $q_{2D} < q_{2O}$ → $\eta_D > \eta_O$

---

## Tabella comparativa cicli

| Caratteristica | **Ciclo Otto** | **Ciclo Sabathé** | **Ciclo Diesel** |
|----------------|----------------|-------------------|------------------|
| **Somministrazione $q_1$** | Isocora ($V=cost$) | Isocora + Isobara | Isobara ($p=cost$) |
| **Accensione** | Comandata (Scintilla/AS) | Com. o Comp. | Compressione (AC) |
| **Miscela** | Premiscelata / Omogenea | Variabile | Non premiscelata / Disomogenea |
| **Rapporto compressione $\beta$** | Basso (8÷12) | Intermedio (12÷16) | Elevato (14÷22) |
| **Rendimento a parità $\beta$** | **Massimo** ($\eta_{th,O}$) | Intermedio ($\eta_{th,S}$) | Minimo ($\eta_{th,D}$) |
| **Rendimento a parità $p_{max}$ (reale)** | Minore | Intermedio | **Maggiore** |

---

## Grandezze caratteristiche motore 4 tempi

### Geometriche e Cinematiche
| Simbolo | Nome | Formula |
|---------|------|---------|
| $D$ | Alesaggio | $[mm]$ |
| $C$ | Corsa | $C=2R_m$ ($R_m$=raggio manovella) |
| $V_c$ | Cilindrata unitaria | $V_c = \frac{\pi D^2}{4}C$ |
| $V_0$ | Volume camera combustione | (nocivo) |
| $V_t$ | Volume totale cilindro | $V_t = V_0+V_c$ |
| $\beta$ | Rapporto compressione | $\beta = \frac{V_t}{V_0} = 1+\frac{V_c}{V_0}$ |
| $C/D$ | Rapporto corsa/alesaggio | <1 superquadro (alti regimi), =1 quadro, >1 sottoquadro |
| $v_p$ | Velocità istantanea pistone | $v_p \approx R_m\omega(\sin\theta+\frac{\Phi}{2}\sin2\theta)$ |

---

### Dosatura reagenti e indice aria
- **Rapporto miscela (A/F)**: $\frac{A}{F} = \frac{m_a}{m_c}$
- **Stechiometrico**: $\left(\frac{A}{F}\right)_s = \frac{1}{0.23}\left(\frac{8}{3}c + 8h + s - o\right)$
- **Indice d'aria (eccesso)**: $\lambda = \frac{(A/F)}{(A/F)_s}$
  - $\lambda=1$: stechiometrica
  - $\lambda<1$: grassa (Otto alte prestazioni)
  - $\lambda>1$: magra (Diesel)

---

### Catena dei rendimenti

| Rendimento | Formula | Significato |
|------------|---------|-------------|
| **Termodinamico** $\eta_{th}$ | $\frac{L_{th}}{Q_1}$ | Ciclo ideale |
| **Indicato** $\eta_i$ | $\frac{L_i}{L_{th}}$ | Scostamenti ciclo reale vs teorico (fluidi reali, scambio termico, combustione non istantanea, pompaggio) |
| **Meccanico** $\eta_m$ | $\frac{L_e}{L_i}$ | Attriti parti in moto + ausiliari (pompe, alternatore) |
| **Globale/Totale** $\eta_{tot}$ | $\frac{L_e}{Q_1} = \eta_{th}\cdot\eta_i\cdot\eta_m$ | Lavoro albero / energia chimica combustibile |
| **Volumetrico** $\eta_v$ | $\frac{m_a}{m_{a,t}} = \frac{m_a}{\rho_a V_c}$ | Capacità riempimento cilindro (perdite carico, scambio termico pareti, effetti dinamici) |

---

### Grandezze prestazionali operative

| Simbolo | Nome | Formula |
|---------|------|---------|
| $P_{mi}$ | Pressione media indicata | $P_{mi} = \frac{L_i}{V_c}$ |
| $P_{me}$ | Pressione media effettiva | $P_{me} = \frac{L_e}{V_c} = P_{mi}\cdot\eta_m$ |
| $P_e$ | Potenza effettiva | $P_e = \frac{L_e\cdot n}{\tau/2} = P_{me}\cdot V_c\cdot\frac{n}{\tau/2} = 2\pi M_e$ (4 tempi: $\tau=4$, $\tau/2=2$) |
| $M_e$ | Coppia motrice | $M_e = \frac{P_e}{\omega} = \frac{P_e}{2\pi n} = \frac{P_{me}\cdot V_c}{2\pi(\tau/2)}$ |
| $c_s$ | Consumo specifico combustibile | $c_s = \frac{\dot{m}_c}{P_e} = \frac{1}{\eta_{tot}\cdot K_i}$ $[g/kWh]$ |

---

## Curve caratteristiche (pieno carico)

Grafico parametri vs regime rotazione $n$ [rpm].

> **Schema:** ![[curve_caratteristiche_slide008-v2.png]]

### Intervallo $n$
- $n_{min}$: **autosostentamento** (coppia motrice > coppia resistente)
- $n_{max}$: **carico massimo** (limiti strutturali/meccanici)

> $P_e$ ed $M_e$ dipendono da $\eta_{tot}(n)$ e $\eta_v(n)$
> - $\eta_{tot} \downarrow$ quando $n \uparrow$
> - $\eta_v$: andamento a campana (max a regime intermedio)

---

### Curva Coppia $M(n)$
- **Crescente** ($n_{min}\to n_M$): $\eta_v \uparrow$ (effetti dinamici aspirazione migliorano)
- **Massimo** $n_M$: $\eta_v$ max, rendimento globale max
- **Decrescente** ($n>n_M$): 
  1. $\eta_v \downarrow$ (perdite carico $\propto v^2$)
  2. Attriti/pompaggio $\uparrow$ → $\eta_{tot} \downarrow$

> **Diesel**: curva coppia più **piatta** (regolazione per *qualità* variando combustibile, no farfalla; $\eta_v$ meno variabile)

---

### Curva Potenza $P_e(n)$
$P_e = 2\pi n M_e$
- $n < n_M$: $n\uparrow$, $M\uparrow$ → $P\uparrow$ rapido
- $n_M < n < n_P$: $M\downarrow$ ma $n\uparrow$ prevale → $P\uparrow$ fino a picco $n_P > n_M$
- $n > n_P$: calo $M$ supera aumento $n$ → $P\downarrow$ repentino

---

### Curva Consumo specifico $c_s(n)$
$c_s = \frac{1}{\eta_{tot}K_i}$ → andamento **a "U"** speculare a $\eta_{tot}$
- **Decrescente** ($n_{min}\to n_M$): $\eta_v\uparrow$, ↓ perdite termiche pareti/ciclo
- **Minimo** a $n \approx n_M$ (max $\eta_{tot}$)
- **Crescente** ($n>n_M$): $\eta_v\downarrow$ (perdite carico), attriti $\uparrow \propto n^2$

---

## Collegamenti
- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Motori a combustione interna – Principi e classificazione]] — Definizioni, diagramma indicatore, fasi reali
- [[Combustione, emissioni e post-trattamento MCI]] — Combustione reale, anomalie (knocking), inquinanti
- [[Termodinamica di base]] — Cicli termodinamici, Carnot, lavoro isoentropico, rendimento
- [[Layout cogenerativi dettagliati (TG, TV, CCGT, MCI)]] — MCI in cogenerazione