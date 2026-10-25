Un **motore a combustione interna** (o _motore endotermico_) è una **macchina termica volumetrica a flusso periodico** che converte l'energia chimica contenuta in un combustibile in energia meccanica.

# Principio di funzionamento
- **Sorgente di Calore:** Il calore viene generato direttamente **all'interno del fluido operatore** attraverso una reazione di combustione tra il combustibile e l'aria (comburente).
- **Trasformazione dell'Energia:** La combustione provoca un elevato incremento di pressione e temperatura del fluido, che si espande all'interno di un cilindro spingendo un pistone (organo mobile). Il movimento alternativo del pistone viene poi convertito in movimento rotatorio (albero motore) tramite un sistema biella-manovella.
- **Variazione del Fluido:** Durante il processo, il fluido di lavoro varia sia in massa (fasi di aspirazione e scarico) sia in composizione chimica (i reagenti si trasformano nei prodotti della combustione).
---
# Classificazione principale
I motori a combustione interna si classificano secondo diversi criteri:

1. **In base al numero di tempi (ciclo meccanico):**
    - **4 Tempi:** Il ciclo di lavoro si completa in 4 corse del pistone (2 giri dell'albero motore): _Aspirazione, Compressione, Espansione/Combustione, Scarico_.
    - **2 Tempi:** Il ciclo si completa in sole 2 corse del pistone (1 giro dell'albero motore), integrando le fasi di lavaggio/aspirazione e scarico vicino ai punti morti.

2. **Tipo di accensione**
	- **AS** $\rightarrow$ Accensione per Scintilla
	- **AC** $\rightarrow$ Accensione per Compressione 

3. **Ciclo termodinamico**
    - **Motori a Ciclo Otto / Benzina:**
        - La miscela aria-combustibile è **premiscelata** (carica omogenea).
        - La combustione viene innescata da una candela ed è caratterizzata dalla propagazione di un **fronte di fiamma**.
        - Il parametro chimico guida per evitare la detonazione (_knocking_) è il **numero di ottano**.
    - **Motori a Ciclo Diesel:**
        - Viene compressa solo l'aria; il combustibile viene iniettato ad alta pressione vicino al Punto Morto Superiore (PMS) dando vita a una **carica disomogenea** (combustione diffusiva).
        - L'accensione avviene **spontaneamente** per via delle elevate temperature e pressioni raggiunte durante la compressione.
        - Il parametro fondamentale è il **numero di cetano** (misura della prontezza all'autoaccensione).

4. **In base all'architettura:**    
    - In linea, a V, a W, a cilindri contrapposti (boxer), ecc.

![[Pasted image 20261024183634.png|488]]

![[Pasted image 20261024184044.png]]
---
# Grandezze geometriche fondamentali
- **PMS (Punto Morto Superiore):** La posizione del pistone più vicina alla testa del cilindro.
- **PMI (Punto Morto Inferiore):** La posizione del pistone più lontana dalla testa.
- **Alesaggio (𝐷):** Il diametro interno del cilindro.
- **Corsa (𝐶):** La distanza percorsa dal pistone tra PMS e PMI.
- **Cilindrata unitaria (𝑉𝑐):** Il volume spazzato dal pistone durante la corsa $V_{c} = \frac{\pi D^2}{4}\cdot C$ 
- **Volume della camera di combustione (𝑉0):** Il volume residuo quando il pistone si trova al PMS.
- **Rapporto volumetrico di compressione (𝛽 o 𝑟):**  
$$
\beta = \frac{V_{0}+V_{c}}{V_{0}}
$$
---
# Cicli termodinamici di riferimanto
- **Ciclo Otto (teorico):** La somministrazione del calore avviene a **volume costante** (trasformazione isocora).
- **Ciclo Diesel (teorico):** La somministrazione del calore avviene a **pressione costante** (trasformazione isobara).
- **Ciclo Sabathé (o Ciclo Misto):** Approssima meglio il ciclo reale dei motori moderni; la somministrazione di calore avviene parzialmente a volume costante e parzialmente a pressione costante.

# Diagramma di indicatore di un motore a 4 tempi
Il **diagramma di indicatore** di un motore a 4 tempi è un grafico cartesiano **Pressione-Volume (𝑝 −𝑉)** che rappresenta le variazioni di pressione all'interno del cilindro in funzione del volume occupato dal fluido durante l'intero ciclo di lavoro (pari a 2 giri dell'albero motore, cioè 720° di angolo di manovella).

## Differenza tra Ciclo Termodinamico e Diagramma di Indicatore
Il diagramma di indicatore **non è un ciclo termodinamico puro** perché:

- Il fluido varia in **massa** durante le fasi di aspirazione e scarico.
- Il fluido varia in **composizione chimica** a causa della combustione.
- Le trasformazioni avvengono lontano dall'equilibrio termodinamico e con scambio termico reale con le pareti.

L'area racchiusa all'interno del ciclo reale rappresenta il **lavoro indicato (𝐿𝑖)** scambiato dal fluido con il pistone:
$$
L_{i} = \int pdV
$$
---
## Le fasi del diagramma di Indicatore Reale
![[diagramma_indicatore_4tempi_confronto-v2.png]]
Il diagramma di un motore a 4 tempi si compone di **due cappi (o anelli)**:

1. **Cappo Utile (o Superiore):** racchiude il lavoro positivo prodotto dalla combustione ed espansione.
2. **Cappo di Pompaggio (o Inferiore):** racchiude il lavoro negativo speso dal motore per rinnovare la carica (aspirazione e scarico).

### 1. Aspirazione (da PMS a PMI)
- Il pistone si muove dal Punto Morto Superiore (PMS) al Punto Morto Inferiore (PMI).
- La pressione all'interno del cilindro scende leggermente al di sotto della pressione atmosferica (𝑝𝑎) creando una **depressione** necessaria a vincere le perdite di carico lungo i condotti di aspirazione.

### 2. Compressione (da PMI a PMS)
- La valvola di aspirazione si chiude e il pistone risale dal PMI al PMS compiendo lavoro sul fluido.
- La pressione e la temperatura aumentano progressivamente (trasformazione reale di compressione).
- **Accensione / Iniezione (prima del PMS):** Prima che il pistone raggiunga il PMS (anticipo accensione nei motori AS o anticipo iniezione nei motori AC), inizia la combustione per compensare i tempi chimico-fisici di innesco.

### 3. Combustione ed Espansione (da PMS a PMI)
- La rapida liberazione di calore fa salire la pressione fino al valore massimo ($p_{max}$).
- Successivamente, i gas ad alta pressione e temperatura si espandono spingendo il pistone verso il PMI e fornendo il **lavoro utile**.
- Durante l'espansione, la pressione e la temperatura diminuendo cedono lavoro all'albero motore.

### 4. Scarico (da PMI a PMS)
- Prima di raggiungere il PMI (anticipo apertura scarico, AAS), si apre la valvola di scarico: la pressione crolla rapidamente verso il valore atmosferico (spontanea fuoriuscita dei gas).
- Il pistone risale dal PMI al PMS spingendo fuori dal cilindro i gas combusti rimanenti. Durante questa fase la pressione nel cilindro è leggermente superiore a quella atmosferica (**sovrappressione allo scarico**).

---
## Differenza tra Diagramma Ideale, Teorico e Reale
1. **Diagramma Ideale:**    
    - Assume gas perfetto a calori specifici costanti, trasformazioni isoentropiche (adiabatiche e reversibili) per compressione/espansione, ed iso-volumiche o iso-bare per la combustione.
    - L'aspirazione e lo scarico avvengono esattamente alla pressione atmosferica 𝑝𝑎 senza lavoro di pompaggio.

2. **Diagramma Teorico / Limite:**
    - Tiene conto che il **fluido è reale** (i calori specifici 𝑐𝑝 e 𝑐𝑣 variano con la temperatura) e delle dissociazioni chimiche ad alta temperatura. Ciò riduce i picchi di pressione e temperatura massimi rispetto al caso ideale.

3. **Diagramma Reale (Effettivo):**    
    - **Arrotondamento delle curve:** La combustione non è istantanea e l'apertura/chiusura delle valvole non è immediata.
    - **Fasatura delle valvole:** Introduzione degli anticipi e ritardi reali per migliorare il riempimento e lo svuotamento:
        - **AAA**(Anticipo apertura aspirazione)
        - **RCS**(Ritardo chiusura scarico)
	    Queste 2 assieme cereano un **angolo di incrocio** questo permette di sfrutare  l'inerzia dei gas combusti per:
	    - migliorare il lavaggio
	    - richiamare aria fresca
	    - risurre il lavoro di pompaggio
		Oltre a questi 2 esistono anche:
		- **RCA**(Ritardo chiusura aspirazione): sfrìutta l'inerzia delle masse in movimento per migliorare il riempimento
		- **AAS**(Anticipo apertura scarico): Riduce la pressione all'interno del cilindro prima del PMI per ridurre il lavoro di pompaggio al costo di una piccola parte del lavoro di espansione
		
    - **Presenza del lavoro di pompaggio (𝑃):** A causa delle perdite di carico nei condotti e della valvola a farfalla (nei motori a benzina/Ciclo Otto regolati per quantità), l'area 𝑃 rappresenta un'area di lavoro negativo che viene sottratta all'area di lavoro utile 𝐴:  
$$
L_{netto} = A- P
$$

---
## Pressione media indicata
Per confrontare motori di cilindrate diverse, dal diagramma di indicatore si ricava la **Pressione Media Indicata (𝑝𝑚𝑖)**, definita come l'ordinata di compenso del ciclo indicato:  
$$
P_{mi} = \frac{L_{i}}{V_{c}} = \frac{1}{V_{c}}\oint pdV
$$
𝑝𝑚𝑖=𝐿𝑖𝑉𝑐=1𝑉𝑐∮𝑝𝑑𝑉Rappresenta quella pressione ipotetica e costante che, agendo sul pistone durante un'unica corsa di espansione, compirebbe lo stesso lavoro netto del ciclo reale.

---
## Cicli termodinamici ideali
![[Pasted image 20261025164235.png]]

Il ciclo termodinamico di questo tipo di impianto può essere descritto in:
1. **Stato iniziale del fluido**
	Il punto 1 corrisponde alle condizione del fluido dopo la fase di aspirazione.
2. **Compressione Isoentropica**(1-2)
	IL pistone sale dal PMI al PMS comprimendo il fluido in modo **adiabatico e reversibile**(isoentropico) di equazione 
$$
	pv^k = costante
$$
	dove $k = c_p/c_v$.
	La pressione finale al PMS($p_2$) dipende dal **rapporto volumetrico di compressione**, $\beta = V_1/V_0 = V_1/V_2$
$$
	p_{2}=p_{1} \cdot\left( \frac{V_{1}}{V_{2}} \right)^k = p_{1}\beta^k
$$
3.  **Somministrazione di calore**(2-3)
	Dal momento che in un ciclo ideale non ci sono reazioni chimiche reali, l'energia cioè il **calore** viene **assorbito interamente** dall'esetrno grazie ad uno scambiatore di calore ideale.
	- **Ciclo Otto** $\to$ Somministrazione di calore di tipo **isocora**, cioè a **colume costante**, simulando la combustione della miscela benzian-aria.
	- **Ciclo Diesel** $\to$ Somministarzione di calore di tipo **isobara**, cioè a pressione costante, simulando la combustione progressiva del gasolio.
	
4. **Espansione isoentropica**(3-4)
	Il fluido ad alta pressione e temperatura si espande dal PMS al PMI spingendo il pistone, grazie ad una **trasformazione adiabatica e reversibile** molto simile alla compressione avvenuta nel tratto 1-2, nel tratto 3-4 il motore compie **il lavoro utilie**.
	- Nel quart punto si individa il l'istante nel quale si apre la valvola di scarico al PMI 
5. **Cessione di calore**(4-1)
	Rappresenta la fase di scarico/rinnovo della carica.
	In un ciclo ideale viene rappresentata come una **cessione istantanea e reversibile di calore verso l'esterno a volume costante**.
	Il fluido torna così alle condizione iniziali dllo stato 1.
---
# Ciclo sabathè
Il **Ciclo Sabathé** (detto anche _ciclo misto_ o _ciclo Dual_) è il ciclo termodinamico ideale che **approssima meglio la combustione reale** nei motori endotermici moderni.

Nei cicli teorici puri:
- Nel **Ciclo Otto**, il calore viene fornito **istantaneamente a volume costante** (isocora 2 →3).
- Nel **Ciclo Diesel**, il calore viene fornito **a pressione costante** (isobara 2 →3).

Nella realtà, la combustione non è né istantanea né a pressione perfettamente costante. Nel ciclo Sabathé, la somministrazione di calore $q_{1}$ avviene in due fasi consecutive:
1. **Trasformazione 2 →3′ (Isocora):** Una prima quota di calore viene fornita a **volume costante** (𝑉 =cost).
2. **Trasformazione 3′ →3 (Isobara):** La restante quota di calore viene fornita a **pressione costante** (𝑝 =cost).

Il calore viene calcolato nei diversi cicli:
1. **Calore introdotto**
	- **Otto**
$$
	q_{1} = c_{v} =(T_{3}-T_{4})
$$
	- **Diesel**
$$
q_{1} = c_{p}(T_{3}-T_{2})
$$
	- **Sabathè**
$$
	q_{1} = c_{v}(T_{3'}-T_{2})+ c_{p}(T_{3}-T_{3'})
$$
1. **Calore ceduto**
	- **Per tutti e 3 i cicli:**
$$
	q_{2} = c_{v}(T_{4}-T_{1})
$$
---
## La fasi termodinamiche dei cicli
Le trasformazioni principali sui piani termodinamici 𝑝 −𝑣 (Pressione-Volume) e 𝑇 −𝑠 (Temperatura-Entropia) sono:

- **1 →2:** Compressione isoentropica (adiabatica reversibile)
- **2 →3 (o 2 →3′ →3):** Somministrazione di calore $q_{1}$ dall'esterno
- **3 →4:** Espansione isoentropica (lavoro utile)
- **4 →1:** Cessione di calore $q_{2}$ all'esterno a volume costante (isocora)
![[confronto_cicli_otto_diesel_sabathe_pv-v2.png]]

---
## Parametri caratteristici del ciclo sabathè
1. **Rapporto di compressione volumetrico**
$$
	\beta = \frac{V_{1}}{V_{2}}
$$
2. **Rapporto di combustione a volume costante**
$$
	a = \frac{p_{3'}}{p_{2}} = \frac{T_{3'}}{T_{2}}
$$
3. **Rapporto di combustione a pressione costante**
$$
b = \frac{V_{3}}{V_{3'}} = \frac{T_{3}}{T_{3'}}
$$
---
### Rendimenti termodinamici
Il rendimento termodinamico generale è dato da:
$$
\eta_{th} = \frac{L_{th}}{q_{1}} = \frac{q_{1}-q_{2}}{q_{1}} = 1- \frac{q_{2}}{q_{1}}
$$
Il **rendimento del ciclo sabthè:**
$$
\eta_{th,S} = 1 - \frac{1}{\beta^{k-1}}\cdot \left[  \frac{a\cdot b^k-1}{(a-1)+k\cdot a\cdot(b-1)} \right]
$$
**Casi limite** del **ciclo Sabathè**:
- Se $b\to 1$(combustione completamente a a volume costante) **Ciclo Otto**:
$$
	\eta_{thO} = 1-\frac{1}{\beta^{k-1}}
$$
- Se $a\to 1$(Combustione completamente a pressione costante) **Ciclo diesel**:
$$
\eta_{thD} = 1 - \frac{1}{\beta^{k-1}} \cdot \left[ \frac{b^k-1}{k(b-1)} \right]
$$
Poiché il termine tra parentesi quadre nel Ciclo Diesel $\left[ \frac{𝑏^𝑘−1}{𝑘(𝑏−1)} \right]$ è **sempre maggiore di 1** (per 𝑏 >1), ne consegue matematicamente che:

> **A parità di rapporto di compressione (𝛽), il rendimento del ciclo Otto è superiore a quello del ciclo Diesel:**  
> $\eta_{thO}>\eta_{thS}>\eta_{thD}$

## Confronto tra Benzina e Diesel
Sebbene a parità di 𝛽 il Ciclo Otto sia teoricamente più efficiente, **nella realtà i motori Diesel sono più efficienti dei motori ad accensione comandata (benzina)**. Le differenze si spiegano analizzando due diverse condizioni di confronto:
![[confronto_rendimento_otto_diesel_beta.png]]

### A parità di rapporto di compressione (𝛽) e calore introdotto ($q_{1}$)
- **Condizione:** $\beta_{0}=\beta_{D}$ e $q_{1,o}=q_{1D}$
- **Esito:** $\eta_{thO} > \eta_{thD}$
- **Motivazione Grafica (𝑇 −𝑠):** Il calore ceduto dal Diesel $q_{2,D} = c_{v}(T_{4D}-T_{1})$ è **maggiore** di quello ceduto dall'Otto $q_{2,0} = c_{v}(T_{4o}-T_{1})$ perché $T_{4D} > T_{4O}$.           Poiché $\eta = 1 - \frac{q_{2}}{q_{1}}$, il ciclo Otto ha un rendimento maggiore.
![[confronto_otto_diesel_ts_beta.png]]

### A parità di pressione massima ($𝑝_{max}$) e calore introdotto ($q_{1}$) — _Caso Reale_
Nei motori reali, il limite principale strutturale dei materiali è la **pressione massima ammissibile**($p_{max}$) in camera di combustione.
![[confronto_otto_diesel_ts_completo-v3.png]]

- **Condizione:**$p_{3,O} = p_{3,D} = p_{max}$ e $q_{1,O} = q_{1,D}$
- **Esito:**$\eta_{th,D} = \eta_{th,O}$
- **Motivazione:** Per non superare $p_{max}$ il ciclo Otto deve operare con rapporti di compressione **bassi**, per evitare il fenomeno nefasto della detonazione. Il ciclo Diesel, invece, lavora privo di carica premiscelata e può spingere il rapporto di comressione a valore **molto più elevati** 
- **Dimostrazione grafica:** A parità di $P_{max}$ la temperatura di fine espansione del ciclo diesel $T_{4,D}$ risulta **inferiore** a quella del ciclo Otto $T_{4O}$.

Poichè $T_{4D} < T_{4O}$ il calore scaricato all'esterno dal ciclo Diesel è minore($q_{2D}<q_{2O}$), rendendo il **motore Diesel pù efficiente nella pratica reale**:
$$
q_{2D}<q_{2O} \implies \eta_{thD} > \eta_{thO}
$$

| Caratteristica                           | Ciclo Otto                 | Ciclo Sabathé (Misto)                       | Ciclo Diesel                   |
| :--------------------------------------- | :------------------------- | :------------------------------------------ | :----------------------------- |
| **Somministrazione Calore (𝑞1)**        | Isocora (𝑉 =cost)         | Parzialmente Isocora + Parzialmente Isobara | Isobara (𝑝 =cost)             |
| **Accensione**                           | Comandata (Scintilla - AS) | Comandata o Compressione                    | Compressione Spontanea (AC)    |
| **Tipo di Miscela**                      | Premiscelata / Omogenea    | Variabile                                   | Non premiscelata / Disomogenea |
| **Rapporto di Compressione (𝛽)**        | Basso (𝛽 ≈8 ÷12)          | Intermedio (𝛽 ≈12 ÷16)                     | Elevato (𝛽 ≈14 ÷22)           |
| **Rendimento a parità di 𝛽**            | **Massimo** (𝜂𝑡ℎ,𝑂)     | Intermedio (𝜂𝑡ℎ,𝑆)                       | Minimo (𝜂𝑡ℎ,𝐷)              |
| **Rendimento a parità di 𝑝max (Reale)** | Minore                     | Intermedio                                  | **Maggiore**                   |

---
## Grandezze caratteristiche di un motore a 4 tempi
Le **grandezze caratteristiche di un motore a 4 tempi** si dividono in grandezze **geometriche, cinematiche, termodinamiche e di prestazione**.

### Grandezze Geometriche e Cinematiche
- **Alesaggio (𝐷):** Diametro interno del cilindro $[mm]$ o $[m]$.

- **Corsa (𝐶):** Distanza percorsa dal pistone tra il Punto Morto Superiore (PMS) e il Punto Morto Inferiore (PMI) $[mm]$ o $[m]$.  
$$
    𝐶=2𝑅_{m}
$$
(dove $R_{m}$ è il raggio di manovella dell'albero motore).
- **Cilindrata Unitaria (𝑉𝑐):** Volume spazzato dal pistone durante una corsa:  
$$
   V_{c} = \frac{\pi \cdot D^2}{4}\cdot C
$$
- **Volume della Camera di Combustione / Volume Nocivo (𝑉0):** Volume residuo sopra il pistone quando si trova al PMS.
   
- **Volume Totale del Cilindro (𝑉𝑡):**  
$$
V_{t} = V_{0}+V_{c}
$$
- **Rapporto Geometrico di Compressione (𝛽 o 𝑟):**  
$$
\beta = \frac{V_{t}}{V_{0}} = \frac{V_{0}+V_{c}}{V_{0}} = 1 + \frac{V_{c}}{V_{0}}   
$$
- **Rapporto Corsa-Alesaggio (𝐶/𝐷):**
    - 𝐶/𝐷 <1  ⟹  Motore **superquadro** (o a corsa corta, favorisce alti regimi di rotazione 𝑛).
    - 𝐶/𝐷 =1  ⟹  Motore **quadro**.
    - 𝐶/𝐷 >1  ⟹  Motore **sottoquadro** (o a corsa lunga).

- **Velocità Istantanea del Pistone (𝑣𝑝):**  
$$
v_{p} \approx R_{m} \cdot \omega \cdot\left( \sin \theta + \frac{\Phi}{2}\sin(2\theta) \right)
$$
    _(dove 𝜔 =2𝜋𝑛 è la velocità d'angolo, 𝜃 è l'angolo di manovella e Φ =𝑅𝑚/𝐿𝑡 è il rapporto biella-manovella)_

---
### Dosatura dei Reagenti e Indice d'Aria
- **Rapporto di Miscela o Dosatura(A/F):** Rapporto tra la massa d'aria ($m_a$) e la massa di combustibile ($m_{c}$)
$$
\frac{A}{F} = \frac{m_{a}}{m_{c}}
$$
- **Rapporto stechiometrico(A/F)s:** Quantità d'aria teorica strettamente necessaria per la combustione completa di 1 Kg di combustibile
$$
\left( \frac{A}{F} \right)_{s} = \frac{1}{0.23} \cdot \left( \frac{8}{3}c + 8h + s - o\right)
$$
- **Eccesso/ Indice d'aria:** 
$$
\lambda = \frac{\left( A/F \right)}{\left( A/F \right)_{s}}
$$
	- $\lambda = 1 \implies$ **MIscela stechiometrica**
	- $\lambda < 1 \implies$ **Miscela grassa** (ricca di combustione, tipica dei cicli Otto ad alte prestazione)
	- $\lambda > 1 \implies$ **Miscela magra** (povera di combustile, tipica dei cicli Diesel)

---
### Rendimenti
- **Rendimento Termodinamico (𝜂𝑡ℎ):** Valuta l'efficienza della conversione del calore introdotto (𝑄1) nel lavoro teorico del ciclo ideale (𝐿𝑡ℎ)
$$
\eta_{th} = \frac{L_{th}}{Q_{1}}
$$   
- **Rendimento Indicato (𝜂𝑖):** Tiene conto delle scostamenti tra ciclo reale e ciclo teorico (perdite per fluidi reali, scambio termico, combustione non istantanea, e lavoro di pompaggio):
$$
\eta_{i} = \frac{L_{i}}{L_{th}}
$$   
- **Rendimento Meccanico (𝜂𝑚):** Tiene conto delle perdite per attrito tra le parti meccaniche in moto e dell'energia spesa per azionare gli ausiliari (pompe, alternatore, ecc.):  
$$
    \eta_{m} = \frac{L_{e}}{L_{i}}
$$
	_(dove 𝐿𝑒 è il lavoro effettivo disponibile all'albero)._
    
- **Rendimento Globale / Totale (𝜂𝑡𝑜𝑡):** Rapporto tra il lavoro effettivo reso all'albero e l'energia chimica introdotta con il combustibile: 
$$
\eta_{tot} = \frac{L_{e}}{Q_{1}} = \eta_{th} \cdot \eta_{i} \eta_{m}
$$
    𝜂𝑡𝑜𝑡=𝐿𝑒𝑄1=𝜂𝑡ℎ⋅𝜂𝑖⋅𝜂𝑚
    
- **Rendimento Volumetrico (𝜂𝑣):** Misura la capacità del motore di riempire il cilindro con aria/miscela rispetto alla sua capacità geometrica teorica:
$$
\eta_{v} = \frac{m_{a}}{m_{a,t}} = \frac{m_{a}}{\rho_{a}\cdot V_{c}}
$$
    _(influenzato da perdite di carico nei condotti, scambi termici con le pareti calde ed effetti dinamici delle onde di pressione)._
---
### Grandezze di Prestazione Operativa
- **Pressione Media Indicata ($P_{𝑚𝑖}$) e Pressione Media Effettiva ($𝑝_{𝑚𝑒}$):** Pressioni fittizie costanti che, agendo sul pistone durante una corsa di espansione, compirebbero rispettivamente il lavoro indicato (𝐿𝑖) o il lavoro effettivo (𝐿𝑒):  
$$
P_{mi} = \frac{L_{i}}{V_{c}} \\
P_{me} = \frac{L_{e}}{V_{c}} = p_{mi}\cdot \eta_{m}
$$
   
- **Potenza Effettiva (𝑃𝑒):** Potenza meccanica erogata all'albero motore alla velocità di rotazione 𝑛:  
$$
P_{e} = \frac{L_{e}\cdot n}{\tau / 2} = p_{me} \cdot V_{c} \cdot \frac{n}{\tau / 2} = 2\pi \cdot M
$$
	_(per un motore a 4 tempi, il numero di tempi per ciclo è 𝜏 =4, quindi 𝜏/2 =2)._
     ^aa1d06
- **Coppia Motrice (𝑀𝑒):** Sforzo torsionale erogato dall'albero motore: 
$$
M_{e} = \frac{P_{e}}{\omega} = \frac{P_{e}}{2\pi n} = \frac{P_{me}\cdot V_{c}}{2\pi \cdot(\tau / 2)}  
$$
 ^3d0430
- **Consumo Specifico di Combustibile (𝑐𝑠):** Massa di combustibile consumata per unità di energia prodotta all'albero $[g/kWh]$:  
$$
    c_{s} = \frac{\dot{m_{c}}}{P_{e}} = \frac{1}{\eta_{tot}\cdot K_{i}}
$$
    _(dove 𝐾𝑖 è il potere calorifico inferiore del combustibile)_ ^d6343b
---
# Curve caratteristiche
Le **curve caratteristiche** di un motore a 4 tempi rappresentano l'andamento dei suoi principali parametri prestazionali al variare del regime di rotazione dell'albero motore 𝑛 (espresso solitamente in $[giri/min]$o $[rpm]$), nelle condizioni di **massima ammissione di carica** (ossia a pieno carico, a farfalla completamente aperta per i motori a benzina o con iniezione massima per i Diesel).

## Le tre curve principali
In un unico grafico con in ascissa la velocità di rotazione n, si tracciano:
1. **[[#^3d0430|Coppia Motrice effettiva]]** $M(n) [Nm]$: Rappresenta la capacità di rotazione del motore
2. **[[#^aa1d06|Potenza effettiva]]**$P(n)[kW]$ o $[CV]$: Rappresenta il lavoro meccanico prodotto nell'unità di tempo
3. **[[Motore a combustione interna#^d6343b|Consumo Specifico di Combustibile]]** $c_{s}(n) [g / kWh]$: Rappresenta la quantità in grammi di combustibile necessaria per erogare 1kWh di energia utile all'albero.

L'intervallo della **velocità della rotazione n**, è definito da:
- $n_{min}\implies$ Regime di **autosostentamento**: al di sotto di questo limite il motore non riesce a vincere le proprie resistenze quindi si deve avere **coppia motrice > coppia resistente**, se questa condizione non è soddisfiatta il motore si spegne.
- $n_{max} \implies$Regime del **carico massimo**: regimi massimo imposto dai limiti strutturali e meccanici dei materiali di cui è composto il motore.

>N.B.
>P ed M dipendono dal **rendimento globale** $\eta_{tot}$ e **volumetrico** $\eta_{v}$ e a loro volta dipendono da **n**

- $\eta_{tot} \downarrow$ (diminuisce) quando $n \uparrow$ 
- $\eta_{v} \to$ andamento massimo in funzione di n, effetti dinamici non ottimizzati a bassi regimi

---
## Il grafico
![[curve_caratteristiche_slide008-v2.png]]
### Curva della coppia motrice
- **Tratto iniziale crescente:** A bassi regimi partendo da $n_{min}$ la coppia aumenta con l'aumentare di n. In questo intervallo il **rendimento volumetrico** $\eta_{v}$ cresce grazie al miglioramento degli effetti dinamici d'inerzia di aspirazione.
- **Punto di massimo($n_{M}$):** La coppia raggiunge il suo valore massimo al regime $n_{M}$. IN questa zona il motore lavora nelle condizioni ottimali di riempimento, con $\eta_{v}$ al massimo, e rendimento globale.
- **Tratto decrescente:** Oltre $n_{M}$ la coppia inizia a scendere perchè:
	1. Il rendimento volumetrico 𝜂𝑣 crolla per via dell'aumento delle perdite di carico nei condotti (proporzionali al quadrato della velocità del fluido).
	2. Le perdite per attrito meccanico e di pompaggio aumentano notevolmente, riducendo $\eta_{tot}$.

>**Nota:** Nei motori **Diesel**, la curva della coppia 𝑀 è tendenzialmente più "piatta" rispetto ai motori a benzina (Ciclo Otto) perché il rendimento volumetrico è meno variabile e la regolazione del carico avviene per _qualità_ (variando la quantità di combustibile iniettato) anziché per _quantità_ tramite farfalla
---
### Curva della Potenza effettiva
Poichè $P = 2\pi n\cdot M$, la potenza dipende sia da regime n sia dalla coppia M.
- $n < n_{M}$: Sia n che M aumentano, per cui la potenza P cresce molto rapidamente
- $n_{M} < n < n_{p}$: Anche se la coppia M comincia a diminuire, l'aumento di n prevale, facendo continuare a salire fino al suo picco massimo al regime $n_{p}$ con ($N_{p} > n_{M}$)
- $n>n_{p}$: Il calo della coppia M diventa così rapido e marcato da superare l'aumento del regime n, causando un crollo repentino della potenza erogata.
---

