# Sistemi a vapore – Cicli Rankine/Hirn, ORC

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Ciclo Hirn (Rankine con surriscaldamento), ottimizzazioni, risurriscaldamento, rigenerativo, cicli ORC**.

---

## Ciclo Hirn (Rankine con surriscaldamento)

> **Schema impianto:** ![[Pasted image 20251009094214.png]]  
> **Riferimento slide:** [[003_SistemiAVapore_MN.pdf#page=2|pagina 2]]

### Componenti impianto
| Componente | Funzione |
|------------|----------|
| **Generatore di vapore** | Economizzatore + Vaporizzatore + Surriscaldatore → converte energia chimica combustibile in energia termica vapore |
| **Turbina a vapore** | Macchina motrice: vapore surriscaldato HP si espande a $p_{cond}$ → energia vapore → lavoro meccanico |
| **Condensatore** | Scambiatore: vapore uscita turbina condensato completamente cedendo calore a fluido refrigerante |
| **Pompa alimentazione/estrazione** | Alimentazione: aspira acqua serbatoio → generatore; Estrazione: condensa fondo condensatore → serbatoio |
| **Alternatore** | Meccanico → elettrico |
| **Serbatoio** | Pressione atmosferica |

### 4 Trasformazioni fluido operatore (acqua/vapore)

| Tratto | Trasformazione | Equazione |
|--------|----------------|-----------|
| $o \to o'$ | **Pressurizzazione** (pompa) | — |
| $o' \to a$ | **Riscaldamento** (caldaia E+V+S) | $q_{oa}=q_1=h_a-h_o$ |
| $a \to b$ | **Espansione** (turbina) | $l_{ab}=h_a-h_b=l_{is}$ |
| $b \to o$ | **Condensazione** (condensatore) | $q_{bo}=q_2=h_b-h_o$ |

> **Diagramma $T-s$:** ![[Pasted image 20251102232758.png]]  
> **Riferimento slide:** [[003_SistemiAVapore_MN.pdf#page=8|pagina 8]]

### Rendimento termodinamico
$$\eta_{th} = \frac{l_{is}}{q_1} = \frac{h_a-h_b}{h_a-h_o}$$

### Potenze
| Potenza | Formula |
|---------|---------|
| Termica fornita | $\dot{Q}_1 = \dot{m}_v \cdot q_1 = \dot{m}_v(h_a-h_o)$ |
| Meccanica utile turbina | $P_{ut} = \dot{m}_v(h_a-h_{b'})\eta_{mt}\eta_{it}$ |
| Elettrica alternatore | $P_e = P_{ut}\cdot\eta_{aux}\cdot\eta_{alt} = \dot{m}_v(h_a-h_{b'})\eta_{it}\eta_{mt}\eta_{aux}\eta_{alt}$ |

### Rendimento totale impianto
$$\eta_{imp} = \frac{P_e}{\dot{m}_c K_i} = \eta_{it}\eta_{mt}\eta_{aux}\eta_{alt}\eta_{th}\eta_g$$

---

## Ottimizzazione rendimento termodinamico

### 1. Pressione condensazione ($p_k$)
Più alta $\Delta T$ tra isotermi → ↑ rendimento (come Carnot).  
Guadagno se $\frac{\Delta L}{\Delta q} > \frac{l}{q_1}$.

> **Riferimento:** [[003_SistemiAVapore_MN.pdf#page=15|page 15]], [[Termodinamica di base#Teorema di Carnot|Ciclo Carnot]]

### 2. Pressione vaporizzazione ($p_{vap}$)
- **Basse pressioni**: ↑ $p_{vap}$ → ↑ $\eta_{th}$
- **Avvicinandosi a pressione critica**: ↑ $p_{vap}$ → ↓ $\eta_{th}$

> **Riferimento:** [[003_SistemiAVapore_MN.pdf#page=17|page 17]]

### 3. Grado di surriscaldamento
Quanto si scalda il fluido oltre lo stato gassoso.  
Divisione ciclo: area campana + area surriscaldamento.  
Uso **temperatura di compenso** per rendimento complessivo.

> **Schema:** ![[Pasted image 20251009103411.png]]  
> **Riferimento:** [[003_SistemiAVapore_MN.pdf#page=19|page 19]], [[Sistemi a vapore - Cicli Rankine-Hirn, ORC#Temperatura di compenso|Temperatura di compenso]]

---

## Temperatura di compenso

Dato un ciclo generico, lo si confronta con un **ciclo Carnot** che ha **stesso rendimento e stesso lavoro**. La **temperatura di compenso** = **temperatura superiore** del ciclo Carnot equivalente.

> **Schema:** ![[Pasted image 20251103000122.png]]  
> **Riferimento:** [[003_SistemiAVapore_MN.pdf#page=18|page 18]]

---

## Ciclo a Risurriscaldamento (Reheat)

> **Schema:** ![[Pasted image 20251009105813.png]]

Flusso: caldaia → **Turbina AP** (espansione parziale) → **risurriscaldamento in caldaia** → **Turbina BP** (espansione finale).

**Ottimizzazione (tipo 3):** aree = ciclo Hirn + parte risurriscaldamento.  
**Rendimento ↑ rispetto a Hirn solo se:** $p_{cond} < p_{rs}^* < p_{vap}$

> **Riferimento:** [[003_SistemiAVapore_MN.pdf#page=20|pagina 20]]

---

## Ciclo Rigenerativo (con spillamenti)

Parte vapore prelevata da turbina → **preriscalda acqua alimento** prima caldaia.  
Vapore spillato cede calore in rigeneratore → condensa o si miscela.

> **Schema spillamento:** ![[Pasted image 20251009121138.png]]  
> **Divisione in 3 sottocicli:** ![[Pasted image 20251009121247.png]]  
> **Temperature compenso:** $T_{mII}=T_v$, $T_m \le T_{mIII} \le T_q$  
> **Riferimento:** [[003_SistemiAVapore_MN.pdf#page=21|pagina 21]]

**Ciclo termodinamico:** ![[Pasted image 20251009123109.png]]  
Fluido si espande → punto 1 → inizia spillamento per rigenerazione.

---

## Cicli ORC (Organic Rankine Cycle)

Ciclo Hirn-Rankine con **acqua/vapore svantaggioso** per **basse temperature** perché:
- Tubi/scambiatori elevato volume → costosi, antieconomici per bassi rendimenti
- Bassa densità vapore fine espansione → pale molto lunghe stadi BP
- Umidità vapore fine espansione → serve surriscaldare o proteggere pale → ↑ costi
- $p_{cond} < p_{atm}$ a normali $T_{cond}$ → infiltrazioni aria, serve degassatore

### Soluzione: **Fluidi organici bassobollenti** ($T_{ebollizione} < T_{acqua}$)
- Ciclo base = Rankine
- Proprietà → costi impianto contenuti anche a basse $T$

### Caratteristiche impianti ORC (piccoli, basse $T$, bassi rendimenti)
- Ciclo **più semplice possibile**
- **No rigenerazione** spillamenti
- **No surriscaldamento**
- **No degassatore** incondensabili

### Classificazione fluidi per forma curva saturazione ($T-s$)

| Tipo | Pendenza curva limite sat. superiore | Comportamento espansione isoentropica |
|------|--------------------------------------|----------------------------------------|
| **ISOENTROPICO** | Verticale | Resta su curva sat. |
| **BAGNATO** (es. acqua) | Negativa | Entra in campana → **condensazione** |
| **SECCO** (dry) | Positiva | Va in zona **vapore surriscaldato** |

> **Schema:** ![[Pasted image 20261014235036.png]]

### Influenza fluidi su ciclo

| Fluido | Surriscaldamento | Rigenerazione | Note |
|--------|------------------|---------------|------|
| **Bagnati** (acqua) | **Aumenta** efficienza | — | $T_{critica}$ modesta → serve alte $p$ |
| **Asciutti / Isoentropici** | **Diminuisce** rendimento se **no rigeneratore** | **Aumenta** efficienza (usa calore residuo) | Rigeneratore = costo aggiuntivo; attento: ↑ $T_{uscita}$ può ↓ rendimento; **impianti piccoli: no rigeneratore** |

### Problematiche fluidi organici
- **Stabilità chimica** ad alta $T$ (vs acqua)
- **Stabilità a contatto pareti solide** componenti
- **Tossicità** e **infiammabilità** (idrocarburi → apparecchiature ATEX; tossicità → ventilazione)
- **ODP** (Ozone Depletion Potential): impatto ozono stratosferico
- **GWP** (Global Warming Potential): contributo effetto serra (riferito a $CO_2$)

---

## Collegamenti
- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Termodinamica di base]] — Carnot, funzioni stato, lavoro espansione/compressione, scambiatori
- [[Generatori di vapore - Tipologie e componenti]] — Caldaia (E+V+S) = sorgente calda ciclo
- [[Rendimento, rugiada acida e parametri combustione]] — Bilancio caldaia, $T_u$ limite rugiada acida
- [[Cicli combinati gas-vapore (CCGT)]] — Ciclo vapore bottoming (HRSG → TV)
- [[Sistemi con impianti cogenerativi]] — Cicli rigenerativi, spillamenti per utenza termica