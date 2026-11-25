# Generatori di vapore – Tipologie e componenti

> Nota derivata da [[Macchine e Sistemi Energetici]] — macro-argomento: **Funzione, 3 sezioni principali, tipologie storiche/evolutive (Cornovaglia, tubi fumo, Babcock, irraggiamento), preriscaldatore Ljungström**.

---

## Funzione e ruolo nei sistemi energetici

**Generatore di vapore** (caldaia) = apparecchiatura termica + scambiatore calore complesso che trasforma **acqua liquida alimentazione → vapore surriscaldato** ad alta $p,T$, somministrando energia termica.

| Contesto | Ruolo |
|----------|-------|
| **Impianti vapore convenzionali (Rankine-Hirn)** | Brucia combustibile direttamente (gas, carbone, biomassa) → vapore surriscaldato HP → turbina vapore |
| **Cicli combinati (CCGT) / Cogenerativi (TG+HRSG)** | **HRSG** (Heat Recovery Steam Generator): calore da **fumi scarico turbina gas** (no combustione diretta) |

> **Schema 3 sezioni:** ![[Pasted image 20261021161558.png|549]]

---

## Tre sezioni principali (in serie)

| Sezione | Funzione | Fluido lato acqua/vapore |
|---------|----------|--------------------------|
| **1. ECONOMIZZATORE** | Preriscalda acqua liquida compressa da pompa alimentazione sfruttando fumi a $T$ più bassa → porta a $T$ vicina saturazione | Liquido compresso → liquido saturo |
| **2. EVAPORIZZATORE** | Cambio fase: **acqua liquida satura → vapore saturo secco** a $p,T$ costanti | Cambio fase isobaro-isotermo |
| **3. SURRISCALDATORE** | Innista $T$ vapore saturo oltre $T_{sat}$ → **vapore surriscaldato** alta entalpia prima turbina | Vapore saturo → vapore surriscaldato |

---

## Tipologie generatori di vapore (evoluzione storica/tecnologica)

### 1. Caldaia di Cornovaglia (Cornish boiler) — XIX secolo
- **Tipo**: tubi di fumo ad **alto volume d'acqua**
- **Struttura**: grande corpo cilindrico orizzontale (≈2/3 acqua), **unico grande tubo focolare** interno (combustione dentro)
- **Combustibile**: carbone su griglia all'estremità tubo focolare
- **Giro fumi**: escono tubo focolare → tornano indietro in **condotti muratura** sotto/ai lati mantello → camino (massimizza scambio)
- **Tubo focolare eccentrico** (spostato basso/lato) → induce **circolazione naturale** per convezione (acqua calda sale presso focolare, fredda scende lati)
- **Duomo vapore** (cupola superiore): camera calma → separa gocce acqua trascinate → vapore secco
- **Tubo focolare ondulato**: ↑ superficie scambio + ↑ stabilità meccanica (pressione esterna acqua)

> **Schema:** ![[caldaia_cornovaglia_spaccato.png]]

---

### 2. Caldaie a tubi di fumo (evoluzione Cornovaglia)
- **Obiettivo**: ↑ superficie scambio, ↑ pressione esercizio, ↑ potenza termica unitaria
- **Struttura**: grande mantello cilindrico acqua, **fittissimo fascio tubi piccolo diametro** (tubi da fumo) annegati in acqua
- **Flussi**: **Dentro tubi = fumi caldi**; **Fuori tubi = acqua**
- **Funzionamento**:
  1. Combustione in focolare principale (corto, annegato)
  2. Fumi → cassa da fumo → distribuiti nei tubi da fumo
  3. Scambio termico: fumi cedono calore per conduzione pareti tubi → acqua bolle
  4. Fumi raffreddati → cassa fumi opposta → camino

> **Schema:** ![[caldaia_tubi_di_fumo_spaccato.png]]

---

### 3. Caldaia Babcock & Wilcox a tubi d'acqua — Rivoluzione tecnologica
**Concetto fondamentale: INVERSIONE principio**
- **Nei tubi = ACQUA** (e miscela acqua/vapore)
- **Fuori tubi = FUMI CALDI** lambiscono banchi tubieri
- **Vantaggi**:
  - Acqua alta pressione in tubi piccolo diametro (<100 mm) → ↓ spessori pareti (legge Mariotte: sollecitazione ∝ diametro)
  - ↑↑ superficie scambio
  - ↑ sicurezza: rottura piccolo tubo = danno contenuto vs rottura mantello grande = catastrofe

> **Schema:** ![[caldaia_babcock_wilcox_spaccato.png]]

#### Funzionamento
1. **Presenza chiara 3 fasci**: Economizzatore (E), Vaporizzatore (V), Surriscaldatore (S)
2. **Primo fascio lambito da fumi caldi uscenti c.c. = Vaporizzatore (V)**
3. **Circolazione naturale**: differenza densità fase liquida (tubo discendente, $\rho_l$) vs bifase acqua-vapore (tubo montante riscaldato, $\rho_{lv}$)
   $$\Delta p = gH(\rho_l - \rho_{lv}) + g\rho_{lv}\Delta H$$
   Spinge circolazione **senza pompe** (valido pressioni subcritiche, tipicamente **< 160 bar**)

---

### 4. Caldaie ad irraggiamento — Per potenze molto elevate (> 100 MW)
**Problemi caldaie grande potenza senza adeguato raffreddamento c.c.**:
1. Danneggiamento materiali refrattari camera
2. Formazione **$NO_x$** (alte $T_{combustione}$ + eccesso $O_2$)
3. Depositi ceneri pastose (combustibili solidi/pesanti)

**Soluzione**: ↑ **grado raffreddamento/schermatura $\varphi$**
$$\varphi = \frac{S_{irr}}{S}$$
Pareti c.c. **interamente schermate** da tubi vaporizzatori ravvicinati → assorbono calore radiante fiamma direttamente.

> **Schema:** ![[caldaia_ad_irraggiamento_spaccato.png]]

#### Ciclo acqua/vapore caldaia irraggiamento
1. **Preriscaldamento**: acqua alimento preriscaldata esternamente (rigenerazione spillamenti turbina) + economizzatori fumi uscita
2. **Alimentazione vaporizzatore**: acqua → collettore inferiore $C_a$ (liquido) → sale tubi vaporizzatori $V$ (schermano c.c.) → vaporizza parzialmente → miscela → collettore superiore $C_v$
3. **Separazione**: corpo separatore $SV$ → separa acqua residua / vapore saturo
4. **Surriscaldamento**: vapore saturo → fasci surriscaldatori
   - **S1 (primo banco)**: spesso **equicorrente** in zona fumi più caldi → limita $T_{parete}$ tubi, evita surriscaldamento critico metallo
   - **S2 (secondo banco)**: **controcorrente** zona successiva, fumi più freddi → raggiunge $T_{surrisc}$ finale richiesta turbina
5. **Circolazione naturale**: differenza volume specifico (densità) liquido/gas. Funziona **< pressione critica (≈221 bar)**.
6. **Limite alta pressione → Circolazione forzata**: sopra **~160 bar** differenziale pressione da densità insufficiente → **pompe circolazione dedicate obbligatorie**

---

### 5. Preriscaldatore a masse di accumulo Ljungström
- **Dispositivo**: grande **tamburo cilindrico rotante** (~3 rpm), settori, lamierini sottili metallo ad altissima superficie specifica
- **Posizione**: sezione divisa a metà da setti fissi
  - Metà 1: lambita da **gas caldi (fumi)** uscita caldaia
  - Metà 2: lambita da **aria fredda** ingresso → camera combustione
- **Principio**: **rigenerativo a contatto indiretto**
  1. **Fase accumulo**: lamierini ruotano in settore fumi → assorbono/accumulo calore
  2. **Fase cessione**: stessi lamierini ruotano in settore aria fredda → rilasciano calore → preriscaldano aria combustione

> **Schema:** ![[Pasted image 20261023185348.png]]

---

## Collegamenti
- [[Macchine e Sistemi Energetici]] — Indice generale
- [[Rendimento, rugiada acida e parametri combustione]] — Bilancio energetico, perdite, rugiada acida, diagramma $T-Q$
- [[Sistemi a vapore – Cicli Rankine/Hirn, ORC]] — Generatore = sorgente calda ciclo Hirn (E+V+S)
- [[Cicli combinati gas-vapore (CCGT)]] — HRSG = generatore a recupero (stesse 3 sezioni)
- [[Sistemi con impianti cogenerativi]] — HRSG in cogenerazione TG+TV
- [[Termodinamica di base]] — Scambiatori equicorrente/controcorrente, lavoro espansione/compressione