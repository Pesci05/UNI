Un **motore a combustione interna** (o _motore endotermico_) è una **macchina termica volumetrica a flusso periodico** che converte l'energia chimica contenuta in un combustibile in energia meccanica.

# Prinicipio di funzionamento
- **Sorgente di Calore:** Il calore viene generato direttamente **all'interno del fluido operatore** attraverso una reazione di combustione tra il combustibile e l'aria (comburente).
- **Trasformazione dell'Energia:** La combustione provoca un elevato incremento di pressione e temperatura del fluido, che si espande all'interno di un cilindro spingendo un pistone (organo mobile). Il movimento alternativo del pistone viene poi convertito in movimento rotatorio (albero motore) tramite un sistema biella-manovella.
- **Variazione del Fluido:** Durante il processo, il fluido di lavoro varia sia in massa (fasi di aspirazione e scarico) sia in composizione chimica (i reagenti si trasformano nei prodotti della combustione).
---
# Classificazione principale
I motori a combustione interna si classificano secondo diversi criteri:

1. **In base al numero di tempi (ciclo meccanico):**
    - **4 Tempi:** Il ciclo di lavoro si completa in 4 corse del pistone (2 giri dell'albero motore): _Aspirazione, Compressione, Espansione/Combustione, Scarico_.
    - **2 Tempi:** Il ciclo si completa in sole 2 corse del pistone (1 giro dell'albero motore), integrando le fasi di lavaggio/aspirazione e scarico vicino ai punti morti.

2. **Tipo di accensione**
	- **AS** $\to$ Accensione per Scintilla
	- **AC** $\to$ Accensione per Compressione 

3. **Ciclo termodinamico**
    - **Motori a Ciclo Otto / Benzina:**
        - La miscela aria-combustibile è **premiscelata** (carica omogenea).
        - La combustione viene innescata da una candela ed è caratterizzata dalla propagazione di un **fronte di fiamma**.
        - Il parametro chimico guida per evitare la detonazione (_knocking_) è il **numero di ottano**.
    - **Motori a Ciclo Diesel:**
        - Viene compressa solo l'aria; il combustibile viene iniettato ad alta pressione vicino al Punto Morto Superiore (PMS) dando vita a una **carica disomogenea** (combustione diffusiva).
        - L'accensione avviene **spontaneamente** per via delle elevate temperature e pressioni raggiunte durante la compressione.
        - Il parametro fondamentale è il **numero di cetano** (misura della prontezza all'autoaccensione).

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



