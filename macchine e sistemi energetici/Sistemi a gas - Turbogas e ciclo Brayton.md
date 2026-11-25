# Sistemi a gas – Turbogas e ciclo Brayton

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Turbo-gas semplice, ciclo Brayton, lavoro utile, recupero calore, regolazione, 2 assi, post-combustione**.

---

## Gruppo turbo-gas semplice

> **Schema:** ![[Pasted image 20251022103036.png]]  
> **Riferimento slide:** [[004_SistemiAGas_MN.pdf#page=3|pagina 3]], [[004_SistemiAGas_MN.pdf#page=4|pagina 4]]

| Componente | Funzione |
|------------|----------|
| **C (Compressore)** | Dinamico assiale; aspira aria → comprime a **pressione esercizio**; $\beta = p_2/p_1$ = rapporto compressione; assorbe lavoro |
| **CC (Camera combustione)** | Aria compressa + combustibile → riscaldamento → ↑ volume; prodotti combustione = parte fluido operatore |
| **TG (Turbina a Gas)** | Fluido si espande (3→4) → lavoro meccanico; scarico fumi atmosfera (punto 4) |
| **M (Motore avviamento)** | Trascina turbina fino a portata aria sufficiente per innesco CC; poi disinnestato |
| **A (Alternatore)** | Meccanico → elettrico |

---

## Ciclo Brayton (ideale)

> **Schema $p-v$ / $T-s$:** ![[ciclo_brayton_pv_ts.png|660]]  
> **Riferimento slide:** [[004_SistemiAGas_MN.pdf#page=5|pagina 5]]

### Ipotesi
1. Ciclo chiuso
2. Fluido = solo aria
3. Trasformazioni lentissime (quasi-statiche)
4. No perdite carico
5. Cedimento calore atmosfera a $p=cost$
6. Compressione ed espansione **isoentropiche**

### Tratti ciclo

| Tratto | Processo | Equazioni |
|--------|----------|-----------|
| **1 → 2'** | Compressione (isoentropica ideale) | $l_{isC} = h_2-h_1$; $\eta_{iC} = \frac{l_{is}}{l_{reale}} = \frac{h_2-h_1}{h_{2'}-h_1} \Rightarrow l_{realeC} = \frac{l_{is}}{\eta_{iC}}$ |
| **2' → 3** | Combustione (isobara) | $q_1 = h_3-h_{2'}$ |
| **3 → 4'** | Espansione (isoentropica ideale) | $l_{isT} = h_3-h_4$; $\eta_{iT} = \frac{l_{reale}}{l_{is}} = \frac{h_3-h_{4'}}{h_3-h_4} \Rightarrow l_{realeT} = \eta_{iT} l_{is}$ |
| **4' → 1** | Raffreddamento (isobaro) | $q_2 = h_{4'}-h_1$ |

### Lavoro reale albero turbina
$$l_{is} = l_{is,T} - l_{is,C} \ge 0 \quad ; \quad l_{reale} = l_{reale,T} - l_{reale,C} \ge 0$$

**Condizione di autosufficienza:** $l_{reale} \ge 0$

$$l_{reale} = c_p(T_3-T_4)\eta_{iT} - \frac{c_p(T_2-T_1)}{\eta_{iC}} \ge 0$$

### Rendimento termodinamico reale
$$\eta_{th,r} = \frac{l_{reale}}{q_1} = \frac{c_p(T_3-T_4)\eta_{iT} - \frac{c_p(T_2-T_1)}{\eta_{iC}}}{c_p(T_3-T_{2'})}$$

### Calore fornito
$$q_1 = h_3-h_{2'} = c_p\left[ (T_3-T_1) - \frac{1}{\eta_{iC}}(T_2-T_1) \right]$$

---

## Lavoro utile e ottimi

### Lavoro utile specifico (adimensionale)
$$L_u = L_T - L_C = c_p(T_3-T_4)\eta_{iT} - \frac{c_p(T_2-T_1)}{\eta_{iC}}$$

$$\beta = \frac{T_2}{T_1} \text{ (rapporto compressione)} \quad ; \quad \theta = \frac{T_3}{T_1} \text{ (rapporto temperature estreme)}$$

$$L_U^* = \frac{L_U}{c_p T_1} = (\beta-1)\left( \frac{\theta}{\beta}\eta_{iT} - \frac{1}{\eta_{iC}} \right)$$

> **Riferimento:** [[004_SistemiAGas_MN.pdf#page=15|pagina 15]]

### Massimo lavoro utile
> **Grafico $L_U^*$ vs $\beta$:** ![[Pasted image 20251023101308.png]]

| Zona | Derivata | Significato |
|------|----------|-------------|
| **Tratto crescente** | $\frac{dL_U^*}{d\beta} > 0$ | ↑ $\beta$ vantaggioso: incremento lavoro turbina > costo compressore |
| **Punto massimo** | $\frac{dL_U^*}{d\beta} = 0$ | **Condizione ottimo**: guadagno marginale turbina = costo marginale compressore; **massimo lavoro netto per kg fluido** |
| **Tratto decrescente** | $\frac{dL_U^*}{d\beta} < 0$ | ↑ $\beta$ riduce potenza: lavoro parassita compressore cresce più veloce di turbina |

### Massimo rendimento
> **Grafico $\eta$ vs $\beta$:** ![[Pasted image 20251023101418.png]]

**Punto max rendimento ≠ punto max lavoro**:  
- Max lavoro = massima **quantità** lavoro prodotto  
- Max rendimento = massima **frazione** calore convertita in lavoro

---

## Gruppo turbo-gas con recupero calore (Rigenerativo)

> **Schema $T-s$:** ![[ciclo_brayton_recupero_ts-v2.png|700]]  
> **Riferimento:** [[004_SistemiAGas_MN.pdf#page=20|pagina 20]]

Usa fumi caldi uscita turbina (verrebbero scartati) per **preriscaldare fluido prima CC**.

$$\eta_{rig} = \frac{L_{netto}}{c_p(T_3-T_x)} > \eta_{semplice} = \frac{L_{netto}}{c_p(T_3-T_2)}$$

---

## Regolazione gruppi turbogas

Potenza elettrica:
$$P_e = \dot{m}_a \cdot l_{reale} \cdot \eta_m \cdot \eta_{aux} \cdot \eta_{alt} = \rho_a \cdot c_a \cdot \Omega \cdot l_{reale} \cdot \eta_m \cdot \eta_{aux} \cdot \eta_{alt}$$

> **Riferimento:** [[004_SistemiAGas_MN.pdf#page=22|pagina 22]]

### 3 metodi regolazione

| Metodo | Descrizione | Effetto |
|--------|-------------|---------|
| **1. Ciclo termodinamico** | ↓ $T_3$ (ingresso turbina) riducendo combustibile | ↓ lavoro, in genere ↓ rendimento |
| **2. Stato fisico fluido ingresso compressore** | Varia densità aria: aria fredda/densa → ↑ portata → ↑ potenza; aria calda/rarefatta → ↓ potenza | Stagionalità, altitudine |
| **3. Velocità rotazione** | Cambia portata aria → cambia potenza; **serve disaccoppiare alternatore** (frequenza costante) → **turbina di potenza** (sistema **2 assi**) | Flessibilità operativa |

> **Schemi regolazione:** ![[Pasted image 20251023110359.png]] ![[Pasted image 20251023110437.png]]

---

## Turbogas su 2 assi

> **Schema:** ![[Pasted image 20261009235436.png]]

### Architettura
| Asse | Componenti | Funzione |
|------|------------|----------|
| **1° ASSE (Generatore)** | CC + Compressore + **Turbina HP** | Espansione $p_2 \to p_{int}$; lavoro estratto = **esattamente lavoro compressore** (autosufficienza): $c_p(T_3-T_{4a}) = c_p(T_2-T_1)$ |
| **2° ASSE (Potenza)** | **Turbina LP** + Alternatore | Espansione $p_{int} \to p_1$; lavoro = **lavoro utile erogato impianto** |

### Diagramma termodinamico
| Tratto | Processo |
|--------|----------|
| 1 → 2 | Compressione $p_1 \to p_2$, $L_c = c_p(T_2-T_1)$ |
| 2 → 3 | Combustione isobara $p_2$, $T_3 = TIT$ |
| 3 → 4a | Espansione reale **Turbina HP** $p_2 \to p_{int}$, $L_{t,HP} = L_c$ |
| 4a → 4 | Espansione reale **Turbina LP** $p_{int} \to p_1$, $L_{netto} = L_{t,LP}$ |
| 4 → 1 | Scarico fumi $p_1$ |

**Disaccoppiamento**: asse potenza ruota a velocità costante/variabile per carico; asse generatore varia velocità per modulare portata aria.

---

## 2 Assi con Post-Combustione (Ricombustione)

> **Schema:** ![[Pasted image 20261010001552.png]]

Espansione e apporto termico **frazionati** per ↑ lavoro specifico.

### Componenti e flusso
1. **Compressore (C)**: $1 \to 2$ ($p_1 \to p_2$)
2. **CC1 (Combustione principale)**: $Q_{in1}$ → $TIT_1$ (stato 3)
3. **T1 (Turbina HP)**: Espansione $p_2 \to p_{int}$ (stato 4a)
4. **CC2 (Post-combustione / Ricombustione)**: Fumi parzialmente espansi (ancora O₂ incombusto) + $Q_{in2}$ → $TIT_2 \approx TIT_1$ (stato 3b)
5. **T2 (Turbina LP)**: Espansione $p_{int} \to p_1$ (stato 4) → aziona carico/alternatore
6. **Scarico**: $4 \to 1$

### Diagramma termodinamico
| Tratto | Processo |
|--------|----------|
| 1 → 2 | Compressione reale $p_1 \to p_2$ |
| 2 → 3 | 1ª Combustione isobara $p_2$ → $TIT_1$ (1400 K) |
| 3 → 4a | 1ª Espansione HP $p_2 \to p_{int}$ |
| 4a → 3b | **Post-combustione** isobara **a $p_{int}$** → $TIT_2$ (1400 K) |
| 3b → 4 | 2ª Espansione LP $p_{int} \to p_1$ |
| 4 → 1 | Scarico fumi $p_1$ |

### Potenza e rendimento
$$P_e = \dot{m}_a L_{netto} \eta_m \eta_{aux} \eta_{alt}$$
$$\eta_{th} = \frac{L_{netto}}{q_{in,1}+q_{in,2}}$$

Assi funzionano come **ciclo 2 assi base**.

---

## Collegamenti
- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Termodinamica di base]] — Ciclo Brayton, lavoro isoentropico, rendimento, autosufficienza
- [[Cicli combinati gas-vapore (CCGT)]] — Turbogas = topping cycle; fumi → HRSG
- [[Sistemi con impianti cogenerativi]] — TG + HRSG cogenerativo; bypass fumi
- [[Sistemi a vapore - Cicli Rankine-Hirn, ORC]] — Ciclo vapore bottoming in CCGT