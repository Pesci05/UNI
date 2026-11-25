# Cogenerazione – Indici e tipologie impianti

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Definizione CHP, indici prestazionali (IUC, Ie, IRE, IREC), classificazione impianti per taglia e tipologia (TG, TV, MCI, CCGT)**.

---

## Definizione e principio CHP

**Impianti cogenerativi** (CHP – *Combined Heat and Power*) = sistemi per la **produzione simultanea di energia elettrica (o meccanica) e calore utile** da un'unica fonte primaria (combustibile fossile o biomassa).

> **Riferimento slide:** [[006_SistemiCogenerativi_MN.pdf#page=1|pagina 1]]

### Classificazione HPC (4 tipologie funzionali)

| Tipo | Descrizione |
|------|-------------|
| **1. Generatori potenza con recupero termico** | Producono elettricità, recuperano calore fumi/scarico |
| **2. Energia primaria con recupero + energia supplementare** | Recupero calore + integrazione combustibile addizionale |
| **3. Recupero termico da generatori calore per potenza** | Calore primario → recupero per produrre elettricità |
| **4. Recupero calore per potenza + ulteriore recupero a valle** | Doppio livello di recupero termico |

---

## Indici prestazionali cogenerazione

### IUC – Coefficiente di Utilizzo (Indice Utilizzazione Cogenerativa)

Esprime la frazione di energia primaria **valorizzata** nell'impianto (elettrica + termica).

$$\begin{aligned}
\eta_{u} &= \frac{P_{e}+P_{t}}{P_{c}} = \frac{P_{e}}{P_{c}} + \frac{P_{t}}{P_{c}} = u_{e} + u_{t} < 1 \\
\eta_{e} &= \frac{P_{e}}{P_{c}} \quad \text{(rendimento elettrico)} \\
\eta_{t} &= \frac{P_{t}}{P_{c}} \quad \text{(rendimento termico)} \\
\eta_{u} &= \eta_{e} + \eta_{t}
\end{aligned}$$

| Simbolo | Significato |
|---------|-------------|
| $P_e$ | Potenza elettrica utile |
| $P_t$ | Potenza termica utile |
| $P_c$ | Potenza chimica combustibile ($\dot{m}_c \cdot K_i$) |

---

### $I_e$ – Indice Elettrico

Definisce la **propensione** dell'impianto per la produzione elettrica vs termica.

$$I_{e} = \frac{P_{e}}{P_{t}}$$

- $I_e > 1$: impianto "elettrico" (es. CCGT, TV derivazione)
- $I_e < 1$: impianto "termico" (es. TV contropressione, MCI piccoli)

---

### IRE – Indice di Risparmio Energetico

Confronta produzione **cogenerativa** vs **separata** (centrale termica + centrale elettrica) per stessa $P_e, P_t$.

$$IRE = \frac{P_{cs} - P_{c}}{P_{cs}} = 1-\frac{P_{c}}{P_{cs}} = 1 - \frac{1}{\frac{\eta_{e}}{\eta_{es}} + \frac{\eta_{t}}{\eta_{ts}}}$$

| Simbolo | Significato |
|---------|-------------|
| $P_{cs}$ | Potenza combustibile produzione separata |
| $P_c$ | Potenza combustibile cogenerativa |
| $\eta_{es}$ | Rendimento elettrico riferimento (centrale elettrica separata) |
| $\eta_{ts}$ | Rendimento termico riferimento (caldaia separata) |

> **Diagramma IRE:** ![[cogenerazione_ire_diagramma.png]]

#### Soglie decisionali

| IRE | Giudizio | Note |
|-----|----------|------|
| $\le 0$ | **NON CONVENIENTE** | Consumo pari/superiore a produzione separata |
| $> 0$ | **CONVENIENTE (Risparmio)** | Per micro/piccoli ($<1$ MW$_e$) basta $IRE>0$ per qualifica **CAR** |
| $\ge 10\%$ | **ALTAMENTE CONVENIENTE (CAR)** | Obbligatorio per medio-grandi ($\ge 1$ MW$_e$); accesso **Certificati Bianchi / TEE** |

---

### IRE riferito all'energia (vs potenza)

- **Potenza**: prestazioni massime impianto (punto di progetto)
- **Energia**: comportamento **effettivo** durante funzionamento (integrazione temporale)

$$IRE = \frac{ \int^{\Delta t}_{0} P_{cs}(t)dt - \int^{\Delta t}_{0} P_{c}(t)dt }{\int^{\Delta t}_{0} P_{cs}(t)dt} = 1 - \frac{1}{\frac{\eta_{e}}{\eta_{es}} + \frac{\eta_{t}}{\eta_{ts}}}$$

con $\eta_{e} = \frac{E_{e}}{E_{c}}$, $\eta_{t} = \frac{E_{t}}{E_{c}}$, $\eta_{es} = \frac{E_{e}}{E_{cse}}$, $\eta_{ts} = \frac{E_{t}}{E_{cst}}$.

---

### IREC – Indice di Risparmio Economico

Valuta convenienza **economica** vs acquisto energia da rete.

$$IREC = \frac{C_{s}-C}{C_{s}} = 1 - \frac{1}{\frac{\eta_{e}}{\frac{\lambda}{\zeta_{e}}} + \frac{\eta_{t}}{\frac{\lambda}{\zeta_{t}}}}}$$

| Simbolo | Significato |
|---------|-------------|
| $C_s$ | Costo acquisto esterno $E_e + E_t$ |
| $C$ | Costo combustibile impianto CHP |
| $\lambda$ | Costo specifico combustibile impianto |
| $\zeta_e$ | Costo specifico acquisto energia elettrica |
| $\zeta_t$ | Costo specifico acquisto energia termica |

| IREC | Giudizio |
|------|----------|
| $\le 0$ | **Economicamente NON conveniente** |
| $> 0$ | **Economicamente CONVENIENTE** (margine operativo $\Delta C > 0$) |

> **Diagramma IREC:** ![[cogenerazione_isec_diagramma.png|660]]

---

## Principali tipologie impianti cogenerativi

| Tipologia | Taglia tipica | Caratteristiche chiave |
|-----------|---------------|------------------------|
| **1. TG + HRSG** | Media/grande ($>5$ MW) | Semplicità, bassi costi investimento, fumi $500\text{–}600^\circ\text{C}$ → HRSG |
| **2. TV Contropressione** | Grande ($>25$ MW) | Vapore espanso fino $p_{utenza}$ (5–6 bar), no condensatore, utenza termica privilegiata |
| **3. TV Derivazione/Spillamento** | Grande | Spillamento a $p_{intermedia}$ per utenza, resto → condensatore, utenza elettrica privilegiata |
| **4. MCI (Motore Combustione Interna)** | Piccola/Media ($<5$ MW) | Recupero duale: fumi AT ($400\text{–}500^\circ\text{C}$) + camicia/olio BT ($80\text{–}90^\circ\text{C}$) |
| **5. CCGT Cogenerativo (CCGT-CHP)** | Molto grande | Ciclo combinato + spillamento vapore HRSG/TV per utenza termica, teleriscaldamento urbano |

> **Riferimento slide:** [[006_SistemiCogenerativi_MN.pdf#page=4|pagina 4]], [[006_SistemiCogenerativi_MN.pdf#page=5|pagina 5]]

---

## Criteri di scelta tipologia

| Criterio | Orientamento |
|----------|--------------|
| **Taglia** | $>25$ MW → TV; $>5$ MW → TG; $<5$ MW → MCI Diesel; $<1$ MW → MCI Otto |
| **Produzione principale** | Elettrica vs Termica → $I_e$ |
| **Temperatura utenza termica** | Alta ($>150^\circ\text{C}$) → vapore (TV, HRSG); Bassa ($<120^\circ\text{C}$) → acqua calda (MCI, HRSG acqua) |
| **Variabilità utenze** | Flessibilità modulazione $P_e/P_t$ (bypass, spillamento, post-combustione) |

---

## Collegamenti

- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Layout cogenerativi dettagliati (TG, TV, CCGT, MCI)]] — Schemi impianto, formule potenze, modulazione bypass/spillamento
- [[Sistemi a gas - Turbogas e ciclo Brayton]] — TG come topping cycle cogenerativo
- [[Sistemi a vapore - Cicli Rankine-Hirn, ORC]] — TV contropressione/derivazione = cicli Hirn modificati
- [[Cicli combinati gas-vapore (CCGT)]] — CCGT base, HRSG, post-combustione
- [[Motori a combustione interna – Principi e classificazione]] — MCI in cogenerazione (recupero fumi + camicia)