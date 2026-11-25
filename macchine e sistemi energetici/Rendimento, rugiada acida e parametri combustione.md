# Rendimento, rugiada acida e parametri combustione

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Parametri combustione, rendimento diretto/indiretto, rugiade acide, carico termico, temperatura combustione, diagramma T-Q, trasmissione calore**.

---

## Parametri caratteristici della combustione

### Massa d'aria stechiometrica
Miscela stechiometrica = minima aria teorica per combustione completa.

Combustibile: frazioni massiche $c$ (Carbonio), $h$ (Idrogeno), $s$ (Zolfo).

| Reazione | Equazione | $O_2$ richiesto per 1 kg elemento |
|----------|-----------|-----------------------------------|
| **Carbonio** | $C + O_2 \to CO_2$ (394,36 kJ/mol) | $\frac{8}{3}$ kg $O_2$ / kg $C$ |
| **Idrogeno** | $H_2 + \frac{1}{2}O_2 \to H_2O$ (237,13 kJ/mol) | 8 kg $O_2$ / kg $H$ |
| **Zolfo** | $S + O_2 \to SO_2$ (297 kJ/mol) | 1 kg $O_2$ / kg $S$ |

Aria ≈ 23% massa $O_2$ (0,23).

**Massa aria stechiometrica:**
$$M_{at} = \alpha_s = \frac{1}{0{,}23} \left( \frac{8}{3}c + 8h + s \right) \quad \left[ \frac{\text{kg}_{\text{aria}}}{\text{kg}_{\text{comb.}}} \right]$$

### Eccesso d'aria ($e$) — Pratica industriale
Stechiometria non basta (contatto intimo incompleto) → si usa eccesso.

| Parametro | Formula |
|-----------|---------|
| **Eccesso aria** $e$ | $e = \frac{M_a - M_{a,t}}{M_{a,t}}$ |
| **Massa aria effettiva** $M_a$ | $M_a = (1+e) M_{a,t}$ |
| **Massa fumi camino** $M_f$ (per kg comb.) | $M_f = M_a + 1$ |

---

## Rendimento generatore di vapore

### METODO DIRETTO
Misura efficienza trasferimento energia chimica combustibile → calore utile fluido (acqua/vapore).

$$\eta_{gen} = \frac{\dot{Q}}{P_i} = \frac{\dot{m}_v \cdot (h_1 - h_0)}{\dot{m}_c \cdot K_i}$$

| Simbolo | Significato |
|---------|-------------|
| $\dot{m}_v$ | Portata vapore generato (= portata acqua alimento in regime stazionario) |
| $h_1$ | Entalpia vapore uscita generatore/surriscaldatore |
| $h_0$ | Entalpia acqua alimento ingresso |
| $\dot{m}_c$ | Portata combustibile bruciata |
| $K_i$ | PCI (Potere calorifico inferiore) combustibile |

**Limite:** non indica cause/fattori perdita (fumi, incombusti, dispersione pareti) → serve **metodo indiretto**.

> **Riferimento slide:** [[007_Generatori_di_Vapore_MN.pdf#page=...|pagina ...]]

---

### METODO INDIRETTO (delle perdite)
Bilancio energetico globale caldaia.

> **Schema perdite:** ![[Pasted image 20261021173159.png]]

$$\eta_{gen} = \varepsilon - \frac{\dot{q}_d}{K_i} - \frac{\dot{M}_f \cdot c_{pm,f} \cdot (t_u - t_a)}{K_i}$$

| Termine | Significato |
|---------|-------------|
| $K_i$ | PCI combustibile |
| $\varepsilon$ | **Rendimento combustione** (perdite incombusti: $CO$ fumi, ceneri solide) |
| $\dot{q}_d$ | **Potenza termica dispersa** pareti esterne (convezione + irraggiamento) |
| $\dot{M}_f$ | Massa fumi per kg combustibile |
| $c_{pm,f}$ | Calore specifico medio $p=cost$ fumi esausti |
| $t_u$ | **Temperatura fumi uscita camino** |
| $t_a$ | Temperatura aria comburente ingresso ($t_b \approx t_a$) |

**Tre contributi perdita:**
1. **Incombusti** ($\varepsilon$): energia chimica non liberata
2. **Calore sensibile fumi** (PERDITA PRINCIPALE): ∝ $(t_u - t_a) \cdot \dot{M}_f$ → minimizzare ↓ $t_u$ (economizzatori, preriscaldatori aria), contenere $e$ (↓ $\dot{M}_f$)
3. **Dispersione pareti** ($\dot{q}_d$): convezione + irraggiamento rivestimento isolante

---

## RUGIADE ACIDE (Condense acide)

Depositi liquidi ad alto contenuto acido, principalmente **acido solforico $H_2SO_4$**, formati raffreddando fumi sotto **temperatura rugiada acida**.

**Origine: Zolfo ($S$) nel combustibile**

1. **Combustione**: $S + O_2 \to SO_2$
2. **Ossidazione catalitica** (eccesso $O_2$, catalizzatori condotti): $SO_2 + \frac{1}{2}O_2 \to SO_3$
3. **Sintesi acido**: $SO_3 + H_2O \to H_2SO_4$

> **Trade-off:** ↓ $t_u$ → ↑ rendimento (meno calore fumi) MA sotto $T_{rugiada}$ → **condense acide corrosive + inquinanti**.

> **Diagramma formazione inquinanti vs $T$ fumi:** ![[formazione_inquinanti_temperatura_fumi-v2.png]]

---

## Parametri caratteristici Generatore di Vapore

### Carico termico e Temperatura di combustione

> **Schema camera combustione:** ![[Pasted image 20261021190219.png]]

**Carico termico volumetrico:**
$$C_t = \frac{\dot{m}_c \cdot K_i}{V} \quad \left[ \frac{\text{kW}}{\text{m}^3} \right]$$
$V$ = volume camera combustione.

**Bilancio termico c.c. (regime stazionario, per kg comb.):**
$$1 \cdot \varepsilon \cdot K_i + M_a \cdot c_{pm,a} \cdot t_a + 1 \cdot c_{pm,b} \cdot t_b = (M_a+1) \cdot c_{pm,f} \cdot t_c + q_i$$

| Termine | Significato |
|---------|-------------|
| $\varepsilon K_i$ | Energia chimica liberata |
| $M_a c_{pm,a} t_a$ | Entalpia sensibile aria ingresso |
| $c_{pm,b} t_b$ | Entalpia sensibile combustibile |
| $(M_a+1)c_{pm,f} t_c$ | Entalpia sensibile fumi uscita a $t_c$ (media combustione) |
| $q_i$ | **Calore ceduto per irraggiamento** fiamma → pareti/tubi vaporizzatori |

**Calore radiante $q_i$ (Stefan-Boltzmann):**
$$q_i = \frac{\alpha \cdot \sigma_0 \cdot S_{irr} \cdot (T_c^4 - T_p^4)}{\dot{m}_c}$$

| Simbolo | Significato |
|---------|-------------|
| $\sigma_0$ | Costante corpo nero $5,67\times10^{-8}$ W/(m²K⁴) |
| $\alpha$ | Coeff. correttivo geometria/assorbimento/emissività |
| $S_{irr}$ | Superficie radiante efficace pareti raffreddate |
| $T_c$ | $T$ assoluta media **fiamma** K ($t_c+273,15$) |
| $T_p$ | $T$ assoluta superficiale **tubi vaporizzatori** K |

---

### Determinazione grafica $t_c$ (temperatura combustione)

> **Diagramma:** ![[determinazione_grafica_tc.png]]

1. **Curva Calore Disponibile** $f(t)$: potenza termica netta rimanente fumi
   $$f(t) = \varepsilon K_i + H_r - q_i(t)$$
   $H_r = M_a c_{pm,a} t_a + c_{pm,b} t_b$ (entalpia reagenti)
   - Per $t \le t_p$: $q_i=0$ → $f(t_p) = \varepsilon K_i + H_r$
   - Per $t > t_p$: $q_i \propto T^4$ → $f(t)$ decresce

2. **Curva Entalpia Fumi** $H_f(t)$:
   $$H_f(t) = (M_a+1) \cdot c_{pm,f}(t) \cdot t$$
   $c_{pm,f}$ cresce con $T$ → parabola concava verso l'alto

3. **Punto intersezione $P$**: $t_c = T$ dove $f(t) = H_f(t)$

---

### Parametri che influenzano $t_c$

| Parametro | Effetto su $t_c$ |
|-----------|------------------|
| **Carico termico superficiale** $\frac{\dot{m}_c}{S_{irr}}$ | ↑ $\dot{m}_c$ o ↓ $S_{irr}$ → ↑ $t_c$ |
| **Eccesso aria $e$** | ↓ $e$ → ↑ $t_c$ (meno aria inerte diluisce calore) |
| **Preriscaldamento reagenti** | ↑ entalpia iniziale aria → ↑ $t_c$ |

**Problemi $t_c$ troppo alta:**
- Danneggiamento materiali refrattari / fasci tubieri
- ↑ **$NO_x$ termici** (cinetica alta $T$)

**Soluzioni limitazione $t_c$:**
1. ↑ **Eccesso aria** (ma ↓ $\eta_{gen}$)
2. ↓ $\frac{\dot{m}_c}{S_{irr}}$ → agire su dimensioni c.c., $C_t$, **grado schermatura $\varphi$**
   $$\varphi = \frac{S_{irr}}{S} \quad \Rightarrow \quad \frac{\dot{m}_c}{S_{irr}} = \frac{\dot{m}_c}{\varphi S} = \frac{C_t \cdot l}{\varphi K_i}$$
   Si agisce su **dimensioni camera**, $C_t$, $\varphi$ schermando pareti.

---

## Posizione scambiatori e Diagramma di scambio termico ($T-Q$ o $T-h$)

Fondamentale per progettazione/rendimento generatore (combustione diretta o HRSG).

> **Diagramma $T-Q$:** ![[Pasted image 20261023172948.png]]

### Lato fumi / sorgente calda
- **In $V$ (camera combustione)**: scambio prevalente **irraggiamento** → $T_{fumi} \approx T_c$ costante (sostenuta da fiamma)
- **Tratti successivi ($S, V', E$)**: scambio **convezione** → $T$ decresce andamento parabolico ($c_{pm,f}$ varia con $T$)

### Lato acqua / vapore (3 fasci tubieri)
1. **Economizzatore (E)**: preriscaldo liquido $T_0 \to T_0'$ (prossima $T_{vap}$)
2. **Vaporizzatore (V / V')**: cambio fase **orizzontale** a $T_v = T_{sat}(p)$ costante
3. **Surriscaldatore (S)**: vapore saturo $T_v \to T_1$ finale (ingresso turbina)

---

### Disposizione scambiatori e Trasmissione calore

Vincolo fisico: trasmissione calore fumi ↔ fluido attraverso pareti tubi.

$$\frac{T_1 - T_p}{T_p - T_2} = \frac{\alpha_2}{\alpha_1}$$

| Simbolo | Significato |
|---------|-------------|
| $\alpha_1$ | Coeff. trasmissione fluido esterno (fumi) ↔ parete esterna |
| $\alpha_2$ | Coeff. trasmissione fluido interno (acqua/vapore) ↔ parete interna |
| $T_p$ | Temperatura parete tubo (es. surriscaldatore) |

> **Schema resistenze termiche:** ![[Pasted image 20261023174539.png]]

---

### Sintesi impatto scambiatori su Generatore

| Scambiatore / Parametro | Ruolo diagramma $T-Q$ | Effetto su Generatore |
|-------------------------|------------------------|------------------------|
| **Surriscaldatore (S)** | Eleva vapore $T_v \to T_1$ a valle c.c. | Fornisce vapore surriscaldato turbina; disposizione equicorrente/controcorrente (S1/S2) evita surriscaldamento critico pareti ($T_p$) |
| **Vaporizzatore (V)** | Tratto orizzontale $T_v=T_{sat}(p)$; irraggiamento in c.c. | $\alpha_v \gg \alpha_f$ mantiene $T_p \approx T_v$ protetta da fumi; limita $T_c$ → ↓ $NO_x$, ↓ danni refrattari |
| **Economizzatore (E)** | Preriscalda liquido $T_0 \to T_0'$ in zona $T_{fumi}$ più bassa | ↓ $T_u$ fumi camino → ↑ $\eta_{gen}$; **limite inferiore $T_u$ = prevenzione rugiade acide ($H_2SO_4$)** |
| **Profilo Fumi ($T_c \to T_u$)** | Irraggiamento $T_c$ costante in c.c., poi decadimento parabolico convettivo | Definisce disponibilità termica sfilabile per salto entalpico totale acqua/vapore fino a $T_u$ |

---

## Collegamenti
- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Generatori di vapore - Tipologie e componenti]] — Tipologie caldaie (Cornovaglia, tubi fumo, Babcock, irraggiamento), Ljungström
- [[Sistemi a vapore – Cicli Rankine/Hirn, ORC]] — Generatore = sorgente calda (E+V+S)
- [[Cicli combinati gas-vapore (CCGT)]] — HRSG = stesso schema 3 sezioni, pinch point
- [[Termodinamica di base]] — Scambiatori equicorrente/controcorrente, bilanci energia
- [[Sistemi con impianti cogenerativi]] — HRSG in cogenerazione, bypass fumi per modulazione $Q_{th}$