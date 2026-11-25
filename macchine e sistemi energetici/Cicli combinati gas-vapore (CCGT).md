# Cicli combinati gas-vapore (CCGT)

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Architettura CCGT, HRSG (E+V+S), Pinch Point, rendimento, post-combustione (duct burner), confronto con/senza post-combustione**.

---

## Principio di funzionamento

Il ciclo combinato nasce per recuperare l'energia termica che nei **turbogas semplici** verrebbe **espulsa in atmosfera** con i fumi a $550\text{–}600^\circ\text{C}$.

> **Schema impianto:** ![[Pasted image 20251029105627.png]] ![[Pasted image 20261011233256.png]]  
> **Riferimento slide:** [[005_SistemiCombinatiGasVapore_MN.pdf#page=2|005_SistemiCombinatiGasVapore_MN, pagina 2]]

### Composizione

| Ciclo | Ruolo | Componenti principali |
|-------|-------|----------------------|
| **Topping (Gas)** | Brucia combustibile, produce $P_{el,1}$, scarica fumi caldi | Compressore, Camera Combustione, Turbina Gas, Alternatore |
| **Bottoming (Vapore)** | Recupera calore fumi → vapore → $P_{el,2}$ | **HRSG** (Economizzatore + Vaporizzatore + Surriscaldatore), Turbina Vapore, Condensatore, Pompa Alimento |

---

## HRSG – Heat Recovery Steam Generator (Caldaia a Recupero)

Stesse **3 sezioni** dei generatori vapore convenzionali, ma **senza combustione diretta** (calore da fumi TG).

> **Schema HRSG 3 sezioni:** ![[Pasted image 20261012000635.png]]

| Sezione | Funzione | Lato fumi | Lato acqua/vapore |
|---------|----------|-----------|-------------------|
| **SURRISCALDATORE** | Vapore saturo → surriscaldato $T_{sh}$ | Fumi **massima $T$** (uscita TG) | Vapore saturo secco da Drum → $T_{sh}$ finale |
| **EVAPORIZZATORE** | Cambio fase liquido → vapore saturo | Fumi raffreddati | **Isobaro-isoterma** a $T_{sat}(p)$ → linea orizzontale $T-Q$ |
| **ECONOMIZZATORE** | Preriscaldo acqua liquida compressa | Fumi **più freddi** (uscita) | Acqua liquida $T_0 \to T_0' \approx T_{sat}$ |

---

## Pinch Point ($\Delta T_{pp}$)

**Differenza minima temperatura** tra fumi in raffreddamento e acqua in evaporazione. Si verifica all'**uscita evaporatore lato fumi**.

$$\Delta T_{pp} = T_{fumi, EVA, out} - T_{sat}(p)$$

- Parametro chiave progettazione HRSG
- ↓ $\Delta T_{pp}$ → ↑ recupero calore → ↑ $\dot{m}_v$ → ↑ $P_{el,TV}$ MA ↑ superficie scambio → ↑ costo
- Ottimizzazione economica: tipico $\Delta T_{pp} \approx 10\text{–}20^\circ\text{C}$

> **Diagramma $T-Q$ con Pinch Point:** ![[Pasted image 20261012000635.png]]

---

## Efficienza scambiatore HRSG ($\sigma$)

$$\sigma = \frac{T_{4'}-T_{5}}{T_{4'}-T_{a}}$$

| Simbolo | Significato |
|---------|-------------|
| $T_{4'}$ | Temperatura fumi ingresso HRSG (uscita TG) |
| $T_5$ | Temperatura fumi uscita HRSG (camino) |
| $T_a$ | Temperatura acqua alimento ingresso |

> **Riferimento slide:** [[005_SistemiCombinatiGasVapore_MN.pdf#page=...|pagina ...]]

---

## Bilancio potenze CCGT

### Potenza elettrica totale

$$\begin{aligned}
P_{e} &= P_{g} + P_{v} \\
P_{g} &= \dot{m}_{a}\cdot q_{1g}\cdot\eta_{thg}\cdot \eta_{iTG} \cdot\eta_{mTG}\cdot \eta_{aux} \cdot \eta_{altTG} \quad \text{(Parte Gas)} \\
P_{v} &= \dot{m}_{a}\cdot q_{1v}\cdot\eta_{thv}\cdot \eta_{iV}\cdot \eta_{mTV}\cdot \eta_{aux} \cdot\eta_{altTV} \quad \text{(Parte Vapore)}
\end{aligned}$$

### Rendimento complessivo impianto

$$\eta_{imp} = \frac{P_{e}}{\dot{m}_{c}\cdot k_{i}} = \frac{P_{g}+P_{v}}{\dot{m}_{c}\cdot k_{i}}$$

- Tipico **senza post-combustione**: $\eta_{cc} \approx 60\text{–}62\%$ (massimo teorico/pratico)
- Oltre il 60% grazie a $TIT > 1400^\circ\text{C}$ (calore somministrato a temperatura di picco)

---

## Post-combustione (Duct Burner / Ricombustione)

Bruciatori integrati nei condotti HRSG che sfruttano **$O_2$ residuo nei fumi** ($12\text{–}15\%$ vol) per innalzare $T$ fumi prima HRSG.

> **Schema:** ![[Pasted image 20261012001634.png|700]]  
> **Riferimento slide:** [[005_SistemiCombinatiGasVapore_MN.pdf#page=...|pagina ...]]

### Differenze: Senza vs Con Post-combustione

| Parametro | **Senza Post-combustione** | **Con Post-combustione** |
|-----------|----------------------------|--------------------------|
| **Apporto Combustibile** | Solo camera combustione TG | TG + **duct burners** HRSG |
| **$T$ fumi ingresso HRSG** | $550\text{–}600^\circ\text{C}$ (scarico TG) | **$700\text{–}900^\circ\text{C}$** (post-bruciatori) |
| **Potenza TV ($P_v$)** | Vincolata da carico TG | **Aumentabile +20% ÷ +50%** (↑ $\dot{m}_v$) |
| **Rendimento $\eta_{cc}$** | **Massimo (60–62%)** | **Leggermente inferiore (56–58%)** |
| **Flessibilità** | Meno flessibile (vapore segue TG) | **Molto elevata** (peak shaving, cogenerazione flessibile) |

---

### Perché funziona (2 fattori chiave)

1. **Sfruttamento $O_2$ residuo**: TG lavora con forte eccesso aria per limitare $TIT$ → fumi ricchi $O_2$ incombusto → post-combustione usa comburente **già caldo**, no aria ambiente.
2. **Compromesso Rendimento vs Potenza/Flessibilità**:
   - **Senza**: max efficienza regime, tutto calore a $TIT$ (alto grado termodinamico)
   - **Con**: accetta penalizzazione $\eta$ (calore extra convertito con solo $\eta_{vapore} \approx 30\text{–}35\%$) per **guadagno potenza e flessibilità**

---

### Effetto su diagramma $T-Q$ HRSG

Innalzando $T_{fumi,in}$ da $550^\circ\text{C}$ a $750\text{–}900^\circ\text{C}$:
- Si **amplia $\Delta T$** tra curva fumi e curve acqua/vapore
- ↑ **portata vapore $\dot{m}_v$** generata a parità di superficie radiante evaporatore
- Migliora adattamento termico (riduce irreversibilità scambio)

> **Diagramma $T-Q$ confronto:** ![[Pasted image 20261012001634.png|700]]

---

### Efficienza HRSG con post-combustione

La formula $\sigma$ si adatta: $T_{4'}$ diventa temperatura fumi **dopo** duct burner (più alta).

$$\sigma = \frac{T_{4'}-T_{5}}{T_{4'}-T_{a}}$$

---

## HRSG a più livelli di pressione

Per ↑ rendimento → **HRSG 2 o 3 pressioni** (HP, IP, LP) con 3 evaporatori a $T_{sat}$ diverse.

- Riduce "divario" $T-Q$ (irreversibilità) avendo più tratti orizzontali a $T$ diverse
- Ogni livello ha proprio $SH$, $EVA$+Drum, $ECO$
- Tipico CCGT moderno: **2 pressioni (HP + LP)** o **3 pressioni (HP + IP + LP)**

> **Schema HRSG 2LP in cogenerazione:** ![[ciclo_combinato_cogenerativo_2lp_layout-v2.png]] (vedi anche [[Layout cogenerativi dettagliati (TG, TV, CCGT, MCI)]])

---

## Collegamenti

- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Sistemi a gas - Turbogas e ciclo Brayton]] — TG = topping cycle (Brayton, $\eta_i$, recupero, 2 assi, post-combustione su TG)
- [[Sistemi a vapore - Cicli Rankine-Hirn, ORC]] — Ciclo vapore = bottoming (Hirn, rigenerativo, risurriscaldamento)
- [[Generatori di vapore - Tipologie e componenti]] — HRSG = caldaia a recupero (stesse 3 sezioni E+V+S, no focolare)
- [[Rendimento, rugiada acida e parametri combustione]] — Bilancio HRSG, $T_u$ camino, rugiada acida, diagramma $T-Q$
- [[Layout cogenerativi dettagliati (TG, TV, CCGT, MCI)]] — CCGT cogenerativo (HRSG 2LP, spillamento TV, bypass fumi)
- [[Cogenerazione – Indici e tipologie impianti]] — CCGT-CHP come tipologia grande taglia, IRE, CAR