# Layout cogenerativi dettagliati (TG, TV, CCGT, MCI)

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Schemi impiantistici completi, bilanci energetici, formule potenze, modulazione bypass fumi, spillamento vapore, recupero duale MCI**.

---

## 1. Gruppo Cogenerativo con Turbina a Gas (TG + HRSG)

> **Layout:** ![[gruppo_cogenerativo_tg_hrsg_layout-v2.png]] ![[Pasted image 20261019003741.png]]

### Componenti e flusso

| Sezione | Descrizione |
|---------|-------------|
| **Turbina a Gas (TG)** | Compressore → Camera Combustione (gas naturale, forte eccesso aria) → Turbina espansione → Alternatore ($P_{el}$) |
| **Fumi scarico** | $T_{4'} = 500\text{–}600^\circ\text{C}$, $O_2$ residuo $12\text{–}15\%$ vol |
| **HRSG** | Surriscaldatore + Evaporatore + Economizzatore (Pinch Point); produce vapore/acqua calda per utenza ($\dot{Q}_{th}$) |
| **Utenza Termica** | Processi industriali / teleriscaldamento |

---

### Efficienza recuperatore termico ($\sigma$)

$$\sigma = \frac{P_{T,reale}}{P_{t,ideale}} = \frac{\dot{m}_{v}(h_{a}-h_{o})}{\dot{m}_{a}c_{p}(T_{4'}-T_{o})} = \frac{T_{4'}-T_{5}}{T_{4'}-t_{0}}$$

$$\dot{Q}_{scambiato} = \dot{m}_{a}c_{p}(T_{4'}-T_{5})$$

| Simbolo | Significato |
|---------|-------------|
| $\dot{m}_v$ | Portata vapore generato |
| $h_a, h_o$ | Entalpia vapore uscita HRSG / acqua alimento ingresso |
| $\dot{m}_a$ | Portata aria/fumi lato gas |
| $T_{4'}$ | Temperatura fumi ingresso HRSG |
| $T_5$ | Temperatura fumi uscita HRSG (camino) |
| $t_0$ | Temperatura acqua alimento ingresso |

---

### Bilancio potenze TG + HRSG

#### Turbina a Gas (parte elettrica)

$$\begin{aligned}
P_{c} &= \dot{m}_{c} K_{i} = \frac{\dot{m}_{a}c_{p}(T_{3}-T_{2'})}{\eta_{cc}} \\
P_{e} &= \dot{m}_{a}c_{p}\left[ (T_{3}-T_{4})\eta_{i,T}- \frac{T_{2}-T_{1}}{\eta_{iC}} \right]\eta_{mTG}\cdot\eta_{auxTG}\cdot\eta_{altTG}
\end{aligned}$$

#### Utenza Termica (parte termica)

$$P_{t} = \dot{m}_{v}\cdot(h_{a}-h_{b})$$

---

### Modulazione $P_e / P_t$ — Bypass Fumi (Diverter Damper)

> **Layout bypass:** ![[gruppo_cogenerativo_tg_hrsg_bypass_layout-v2.png]]

| Posizione serranda $\alpha$ | Funzionamento |
|----------------------------|---------------|
| **$\alpha = 0$** (chiusa bypass) | 100% fumi in HRSG → **massima $\dot{Q}_{th}$**, assetto cogenerativo pieno |
| **$0 < \alpha < 1$** (parziale) | Frazione fumi a camino bypass → **riduce $\dot{Q}_{th}$ a piacimento**, $P_{el}$ costante (TG a pieno carico) |
| **$\alpha = 1$** (chiusa HRSG) | 100% fumi a bypass → **$\dot{Q}_{th} = 0$**, assetto **puramente elettrico**; permette manutenzione HRSG senza fermare TG |

---

## 2. Gruppo Cogenerativo con Turbina a Vapore (TV)

Basato su **ciclo Hirn-Rankine**. Due configurazioni principali.

> **Schema contropressione:** ![[Pasted image 20261019233357.png]] ![[Pasted image 20261019233449.png]]  
> **Schema derivazione:** ![[gruppo_cogenerativo_tv_derivazione_layout_ts.png]]

---

### A) Turbina in CONTROPRESSIONE

- $p_{uscita} \approx p_{utenza}$ (5–6 bar)
- **No condensatore** tradizionale
- Vapore scaricato **interamente** verso utenza termica
- Non funziona senza utenza termica
- **Utenza termica privilegiata** su elettrica

#### Potenze

$$\begin{aligned}
P_{c} &= \dot{m}_{c}\cdot k_{i} = \frac{\dot{m}_{v}\cdot(h_{a}-h_{o})}{\eta_{g}} \\
P_{e} &= \dot{m}_{T}\cdot(h_{a}-h_{bt})\cdot \eta_{i}\cdot \eta_{m}\cdot \eta_{aux}\cdot \eta_{alt} \\
P_{t} &= \dot{m}_{v}\cdot(h_{d}-h_{e})
\end{aligned}$$

| Stato | Descrizione |
|-------|-------------|
| $a$ | Vapore ingresso TV (HP) |
| $bt$ | Uscita TV reale |
| $d$ | Vapore saturo pressione utenza |
| $e$ | Condensato ritorno utenza |

#### Casi estremi

| Caso | Condizione | $P_e$ | $P_t$ |
|------|------------|-------|-------|
| **Potenza elettrica MAX** | $\dot{m}_T = \dot{m}_v$ | $\dot{m}_T(h_a-h_{bt})\eta_i\eta_m\eta_{aux}\eta_{alt}$ | $\dot{m}_v(h_b-h_e)$ |
| **Potenza termica MAX** | $\dot{m}_T = 0$ | $0$ | $\dot{m}_v(h_c-h_e)$ |

> $V_1$ parzializza portata vapore → laminazione isoentalpica; richiesta utenza incide su $\dot{m}_T$ e quindi $P_e$.

---

### B) Turbina in DERIVAZIONE / SPILLAMENTO

- Espansione fino **sotto pressione atm** ($p_{cond} \approx 0,04\text{–}0,08$ bar)
- **Utenza elettrica privilegiata**
- Spillamento a pressione intermedia $p_{spill}$ per utenza termica

#### Componenti

1. **Generatore Vapore** → $\dot{m}_v, p_{HP}, T_{HP}$
2. **TV AP** → espansione a $p_{spill}$
3. **Nodo Derivazione** → valvola regolazione:
   - $\dot{m}_{th}$ → **Utenza Termica** (condensatore utile, $Q_{th}$)
   - $\dot{m}_{cond} = \dot{m}_v - \dot{m}_{th}$ → **TV BP** → Condensatore Freddo
4. **Condensatore Freddo** → rigetto calore non recuperabile
5. **Ritorno condensa** → miscelazione → Pompa Alimento → Caldaia

#### Diagramma $T-s$ (stati riferimento)

| Tratto | Processo | Stati |
|--------|----------|-------|
| $1 \to 2 \to 3 \to 4$ | Riscaldamento, evaporazione, surriscaldamento | $p_{HP}=80$ bar, $T_4=500^\circ\text{C}$ |
| $4 \to M$ | Espansione TV AP | $p_{spill}=5$ bar, $T_{sat}\approx152^\circ\text{C}$ |
| $M \to 6_U$ (viola) | Spillamento $\dot{m}_{th}$ → condensazione utenza | $Q_{th}$ cogenerativo |
| $M \to 5_C$ (verde scuro) | Espansione TV BP | $p_{cond}=0,05$ bar |
| $5_C \to 6_C$ (azzurro) | Condensazione freddo | $T\approx33^\circ\text{C}$, $Q_{lost}$ |
| $6_C/6_U \to 1$ (blu) | Ricircolo + pompaggio | — |

#### Potenze

$$\begin{aligned}
h_{6c} &= \frac{(\dot{m}_{v}-\dot{m}_{TAP})\cdot h_{c}+\dot{m}_{TAP}\cdot h_{b}}{\dot{m}_{v}} \\
P_{c} &= \dot{m}_{c}\cdot k_{i} = \frac{\dot{m}_{v}\cdot(h_{a}-h_{o})}{\eta_g} \\
P_{e} &= [\dot{m}_{TAP}\cdot(h_{a}-h_{bt})\cdot \eta_{i,TAP}\cdot \eta_{m,TAP} + \dot{m}_{TBP} \cdot (h_{d}-h_{kt}) \cdot \eta_{i,TBP} \cdot \eta_{m,TBP}] \eta_{aux}\cdot \eta_{alt} \\
P_{t} &= \dot{m}_{UT}\cdot(h_{d}-h_{e})
\end{aligned}$$

#### Casi estremi

| Caso | Condizioni | $P_e$ | $P_t$ |
|------|------------|-------|-------|
| **Elettrica MAX** | $\dot{m}_{TAP}=\dot{m}_{TBP}=\dot{m}_v$ | Formula completa | $0$ |
| **Termica MAX** | $\dot{m}_{TAP}=\dot{m}_{TBP}=0,\ \dot{m}_{UT}=\dot{m}_v$ | $0$ | $\dot{m}_v(h_c-h_e)$ |
| **Portata distribuita** | $\dot{m}_{UT}=\dot{m}_{TBP},\ \dot{m}_{TAP}=\dot{m}_v$ | Formula con $\dot{m}_{TBP}$ | $\dot{m}_{UT}(h_b-h_e)$ |

---

## 3. Gruppo Combinato Cogenerativo – Vapore Cogenerativo (CCGT-CHP)

> **Layout:** ![[ciclo_combinato_cogenerativo_2lp_layout-v2.png]] ![[Pasted image 20261020235607.png]]

### Problema HRSG 1 livello
Evaporazione a $T_{sat}$ fissa → "divario" $T-Q$ fumi/acqua → **forte irreversibilità** (distruzione energia).

### Soluzione: HRSG 2 Livelli (2LP)

#### Sezione Turbina a Gas (TG)
- Brucia combustibile ($\dot{Q}_{in}$)
- Produce $P_{el,TG}$
- Fumi scarico $550\text{–}600^\circ\text{C}$

#### HRSG 2LP (6 banchi controcorrente)
| Sezione AP (Alta Pressione) | Sezione BP (Bassa Pressione) |
|----------------------------|------------------------------|
| Surriscaldatore AP ($SH_{AP}$) | Surriscaldatore BP ($SH_{BP}$) |
| Evaporatore AP + Drum ($EVA_{AP}+D_{AP}$) | Evaporatore BP + Drum ($EVA_{BP}+D_{BP}$) |
| Economizzatore AP ($ECO_{AP}$) | Economizzatore BP ($ECO_{BP}$) |

Fumi uscita camino $\sim 100^\circ\text{C}$.

#### Turbina a Vapore Spillamento + Utenza
- Vapore AP ($80\text{–}100$ bar, $520^\circ\text{C}$) → $TV_{AP}$
- Uscita $TV_{AP}$ + vapore BP ($6\text{–}10$ bar) → miscelazione → $TV_{BP}$
- **Spillamento cogenerativo**: estrazione sezione intermedia/BP → Utenza Termica ($\dot{Q}_{th}$)
- Resto → espansione vuoto Condensatore Freddo → max $P_{el,TV}$
- Condense → Pompe $P_{BP}, P_{AP}$ → ricircolo HRSG

#### Potenze

$$\begin{aligned}
\dot{Q}_{scambiato} &= \dot{m}_{a}\cdot c_{p} \cdot(T_{4'}-T_{5}) \\
P_{c} &= \dot{m}_{c}\cdot K_{i} = \frac{\dot{m}_{a}\cdot c_{p} \cdot (T_{3}-T_{4'})}{\eta_{cc}} \\
P_{e} &= P_{g} + P_{v} \\
P_{t} &= \dot{m}_{UT} \cdot (h_{d} - h_{e})
\end{aligned}$$

---

## 4. Gruppo Cogenerativo con Motore a Combustione Interna (MCI)

> **Layout:** ![[gruppo_cogenerativo_mci_layout.png]]

### Peculiarità: Recupero termico su **DUE LIVELLI** distinti

| Livello | Fonte | Temperatura | Scambiatore | Uscita vettore |
|---------|-------|-------------|-------------|----------------|
| **Alta Temperatura (AT)** | Fumi scarico cilindri | $400\text{–}500^\circ\text{C}$ | Scambiatore fumi (fascio tubiero) | Acqua/vapore BP $90\text{–}110^\circ\text{C}$ → camino $110\text{–}120^\circ\text{C}$ |
| **Media/Bassa (BT/MT)** | Acqua camicia (*jacket water*) | $80\text{–}90^\circ\text{C}$ | Scambiatore a piastre (HT) | Acqua utenza |
|  | Olio lubrificazione | — | (stesso circuito BT) | — |
|  | Intercooler turbocompressore | — | (stesso circuito BT) | — |

> Differenza vs TG: TG ha solo fumi AT; MCI offre **cogenerazione a cascata** (vapore/acqua calda AT + acqua calda BT/MT).

### Tipologia motori usati
- **4 tempi** ad accensione comandata (gas naturale) → taglia piccola/media, terziario/ospedali
- **4 tempi** ciclo Diesel → taglia media, industriale

### Applicazioni tipiche
Ospedali, centri commerciali, piccole/medie industrie, micro-cogenerazione terziaria ($<1$ MW$_e$ Otto, $<5$ MW$_e$ Diesel).

---

## Collegamenti

- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Cogenerazione – Indici e tipologie impianti]] — IUC, IRE, IREC, classificazione per taglia
- [[Sistemi a gas - Turbogas e ciclo Brayton]] — TG topping cycle, Brayton, recupero calore, 2 assi
- [[Sistemi a vapore - Cicli Rankine-Hirn, ORC]] — TV contropressione/derivazione = cicli Hirn modificati
- [[Cicli combinati gas-vapore (CCGT)]] — CCGT base, HRSG 1/2 livelli, post-combustione
- [[Generatori di vapore - Tipologie e componenti]] — HRSG = caldaia a recupero (E+V+S), Pinch Point
- [[Rendimento, rugiada acida e parametri combustione]] — Bilancio HRSG, $T_u$ limite rugiada acida
- [[Motori a combustione interna – Principi e classificazione]] — MCI 4 tempi, diagramma indicatore, recupero fumi+camicia