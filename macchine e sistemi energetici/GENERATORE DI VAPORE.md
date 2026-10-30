I **generatori di vapore** (comunemente chiamati anche **caldaie**) sono apparecchiature termiche e scambiatori di calore complessi il cui scopo fondamentale è trasformare l'acqua liquida di alimento in vapore d'acqua ad elevate condizioni di pressione e temperatura, somministrando energia termica.

All'interno dei **sistemi energetici a vapore (cicli Rankine-Hirn)** e degli **impianti combinati e cogenerativi**, il generatore di vapore costituisce il cuore della sorgente calda del ciclo.

**Impianti a Vapore Convenzionali (Ciclo Rankine-Hirn)**: Il generatore di vapore brucia direttamente un combustibile (gas naturale, carbone, biomassa) per produrre il vapore surriscaldato ad alta pressione che s'espanderà poi nella turbina a vapore.

**Cicli Combinati (CCGT) e Cogenerativi (TG + HRSG)**: Assume la forma della **Caldaia a Recupero (HRSG —** **Heat Recovery Steam Generator** **)**, in cui il calore non deriva da una combustione diretta ma dal raffreddamento dei fumi caldi di scarico della turbina a gas.

Per ottimizzare lo scambio termico ed evitare shock termici, la trasformazione dell'acqua in vapore avviene attraversando **tre sezioni principali disposte in serie**:
1. **ECONOMIZZATORE**
	Riceve l'acqua liquida compressa dalla pompa di alimento e la preriscalda sfruttando i fumi a temperatura più bassa, portandola in prossimità della temperatura di saturazione. ^1676a5
2. **EVAPORIZZATORE**
	Compie il cambio di fase da acqua liquida satura a vapore saturo secco a pressione e temperatura costanti. ^2726ef
3. **SURRISCALDATORE**
	Riceve il vapore saturo secco e ne innalza ulteriormente la temperatura al di sopra della temperatura di saturazione, producendo **vapore surriscaldato** ad alta entalpia prima dell'ingresso in turbina a vapore.
![[Pasted image 20261021161558.png|549]] ^16978c
# Prametri caratteristici delle combustione
## Massa d'aria stechiometrica
La **miscela stechiometrica** rappresenta il rapporto aria/combustibile corrispondente alla **minima quantità teorica d'aria** affinché la combustione del combustibile sia completa.

Considerando un combustibile formato da **Carbonio (**$C$**)**, **Idrogeno (**$H$**)** ed eventualmente **Zolfo (**$S$**)**, le cui **frazioni in massa** siano indicate rispettivamente con $c$, $h$ e $s$, le reazioni elementari di ossidazione e i relativi calori di reazione sono:

1. **Ossidazione del Carbonio**: $$C + O_2 \Rightarrow CO_2 \quad (394{,}36\text{ kJ/mol})$$
    - Per bruciare $1\text{ kg}$ di $C$ occorrono $\frac{8}{3}\text{ kg}$ di $O_2$.
2. **Ossidazione dell'Idrogeno**: $$H_2 + \frac{1}{2}O_2 \Rightarrow H_2O \quad (237{,}13\text{ kJ/mol})$$
    - Per bruciare $1\text{ kg}$ di $H$ occorrono $8\text{ kg}$ di $O_2$.
3. **Ossidazione dello Zolfo**: $$S + O_2 \Rightarrow SO_2 \quad (297\text{ kJ/mol})$$
    - Per bruciare $1\text{ kg}$ di $S$ occorre $1\text{ kg}$ di $O_2$.

Considerando che l'aria atmosferica contiene circa il $23\%$ **in massa di ossigeno** ($0{,}23$), la **massa d'aria stechiometrica** ($M_{at}$ o $\alpha_s$), espressa in $\text{kg}_{\text{aria}} / \text{kg}_{\text{comb.}}$, si calcola come:

$$M_{at} = \alpha_s = \frac{1}{0{,}23} \cdot \left( \frac{8}{3} c + 8 h + s \right) \quad \left[ \frac{\text{kg}_{\text{aria}}}{\text{kg}_{\text{comb.}}} \right]$$

Nella pratica industriale, la sola miscela stechiometrica non è sufficiente a garantire il contatto intimo tra tutti i reagenti e completare la reazione; si opera quindi con un **eccesso d'aria** ($e$):

- **Eccesso d'Aria (**$e$**)**: $$e = \frac{M_a - M_{a,t}}{M_{a,t}}$$
- **Massa d'Aria Effettiva (**$M_a$**)**: $$M_a = (1 + e) \cdot M_{a,t} \quad \left[ \frac{\text{kg}_{\text{aria}}}{\text{kg}_{\text{comb.}}} \right]$$
- **Massa di Fumi al Camino (**$M_f$**)** (riferita all'unità di massa di combustibile): $$M_f = M_a + 1 \quad \left[ \frac{\text{kg}_{\text{fumi}}}{\text{kg}_{\text{comb.}}} \right]$$

# Rendimento del generatore di vapore
## METODO DIRETTO
Il **rendimento del generatore di vapore calcolato in modo diretto** (o _metodo diretto_) misura l'efficienza con cui l'energia chimica contenuta nel combustibile viene effettivamente trasferita al fluido operatore (acqua/vapore) sotto forma di calore utile.

$$\eta_{gen} = \frac{\dot{Q}}{P_i} = \frac{\dot{m}_v \cdot (h_1 - h_0)}{\dot{m}_c \cdot K_i}$$

I parametri della formula rappresentano:

- $\dot{m}_v$: Portata massica di vapore generato (in regime stazionario corrisponde alla portata d'acqua di alimento $\dot{m}_{H_2O}$) .
- $h_1$: Entalpia specifica del vapore in uscita dal generatore/surriscaldatore .
- $h_0$: Entalpia specifica dell'acqua di alimento in ingresso al generatore.
- $\dot{m}_c$: Portata massica di combustibile bruciata.
- $K_i$: Potere calorifico inferiore (PCI) del combustibile.

Sebbene sia immediato, il metodo diretto **non fornisce alcuna indicazione sulle cause o sui singoli fattori di perdita che influenzano il rendimento** (come il calore sensibile disperso con i fumi al camino, gli incombusti o la dispersione termica dalle pareti). Per analizzare la ripartizione dettagliata delle perdite si ricorre invece al **metodo indiretto** (o _metodo delle perdite_).

## METODO INDIRETTO
![[Pasted image 20261021173159.png]]
Il **metodo indiretto** (detto anche _metodo delle perdite_) per la determinazione del **rendimento del generatore di vapore** ($\eta_{gen}$) si basa sul **bilancio energetico globale dell'intera caldaia**.

$$\eta_{gen} = \varepsilon - \frac{\dot{q}_d}{K_i} - \frac{\dot{M}_f \cdot c_{pm,f} \cdot (t_u - t_a)}{K_i}$$

Dove:

- $K_i$: Potere calorifico inferiore del combustibile.
- $\varepsilon$: **Rendimento di combustione**, che tiene conto delle perdite per incombusti.
- $\dot{q}_d$: **Potenza termica dispersa** attraverso le pareti esterne della caldaia per unità di massa di combustibile.
- $\dot{M}_f$: Massa totale dei fumi prodotta per unità di massa di combustibile.
- $c_{pm,f}$: Calore specifico medio a pressione costante dei fumi esausti.
- $t_u$: Temperatura dei fumi in uscita al camino.
- $t_a$: Temperatura dell'aria comburente all'ingresso (con $t_b \approx t_a$).

Il metodo indiretto suddivide l'energia non recuperata in tre contributi distinti12:

1. **Perdita per Incombusti (Rendimento di Combustione** $\varepsilon$**)**:
    - Misura la quota di energia chimica del combustibile effettivamente liberata dalle reazioni di ossidazione.
    - È influenzata dalla presenza di incombusti gassosi nei fumi (es. $CO$) o incombusti solidi nelle ceneri.
2. **Calore Sensibile Disperso con i Fumi al Camino (Perdita Principale)**:
    - Rappresenta la quota maggiore di perdita in un generatore di vapore.
    - È direttamente proporzionale al salto termico tra la **temperatura dei fumi al camino (**$t_u$**)** e la **temperatura dell'aria ambiente (**$t_a$**)**, nonché alla **massa di fumi (**$\dot{M}_f$**)**.
    - Per minimizzare questa perdita occorre abbassare il più possibile $t_u$ (sfruttando economizzatori e preriscaldatori d'aria) e contenere l'eccesso d'aria per ridurre $\dot{M}_f$.
3. **Potenza Termica Dispersa dalle Pareti (**$\dot{q}_d$**)**:
    - È il calore ceduto verso l'ambiente esterno per convezione ed irraggiamento dalle pareti e dal rivestimento isolante della caldaia.

# RUGIADE ACIDE
Le **rugiade acide** (o condense acide) sono depositi liquidi ad alto contenuto acido  principalmente **acido solforico (**$\mathrm{H_2SO_4}$**)** che si formano quando i fumi di combustione vengono raffreddati al di sotto di una specifica temperatura, detta **temperatura di rugiada acida**.

Il fenomeno origina dalla presenza di **zolfo (**$\mathrm{S}$**)** all'interno del combustibile2:

1. **Formazione di Anidride Solforosa**: Durante la combustione, lo zolfo si ossida producendo anidride solforosa: $$S + O_2 \longrightarrow SO_2$$
2. **Ossidazione ad Anidride Solforica**: In presenza di un eccesso d'ossigeno e di catalizzatori nei condotti fumi, una frazione di $\mathrm{SO_2}$ si ossida ulteriormente ad anidride solforica: $$SO_2 + \frac{1}{2}O_2 \longrightarrow SO_3$$
3. **Sintesi di Acido Solforico**: L'anidride solforica reagisce prontamente con il vapore d'acqua generato dalla combustione: $$SO_3 + H_2O \longrightarrow H_2SO_4$$
**Ridurre la temperatura** dei fumi **migliora il rendimento del generatore** (limita la perdita di calore nei fumi), ma al di sotto di certe temperature si formano condense acide corrosive e inquinanti.
![[formazione_inquinanti_temperatura_fumi-v2.png]]

# Parametri caratteristici del Generatore di Vapore
## Carico TERMICO e Temperatura di Combustione
![[Pasted image 20261021190219.png]]
Il **carico termico volumetrico** ($C_t$) esprime la densità di potenza termica liberata dalla combustione per unità di volume della camera12:

$$\mathbf{C_t = \frac{\dot{m}_c \cdot K_i}{V}} \quad \left[\frac{\text{kW}}{\text{m}^3} \text{ o } \frac{\text{kJ}}{\text{s}\cdot\text{m}^3}\right]$$
V indica il volume della camera di combustione.

In condizioni di **regime stazionario** (l'energia in ingresso eguaglia quella in uscita), il bilancio termico della c.c. riferito all'unità di massa di combustibile si scrive come:
$$\mathbf{1 \cdot \varepsilon \cdot K_i + M_a \cdot c_{pm,a} \cdot t_a + 1 \cdot c_{pm,b} \cdot t_b = (M_a + 1) \cdot c_{pm,f} \cdot t_c + q_i}$$

I singoli termini rappresentano:

- $\varepsilon \cdot K_i$: Energia chimica effettivamente liberata (con $\varepsilon$ rendimento di combustione).
- $M_a \cdot c_{pm,a} \cdot t_a$: Entalpia sensibile dell'aria comburente in ingresso.
- $1 \cdot c_{pm,b} \cdot t_b$: Entalpia sensibile del combustibile.
- $(M_a + 1) \cdot c_{pm,f} \cdot t_c$: Entalpia sensibile dei fumi in uscita alla temperatura media di combustione $t_c$.
- $q_i$: **Calore ceduto per irraggiamento** dalla fiamma alle pareti/tubi vaporizzatori per unità di massa di combustibile

Il calore radiativo $q_i$ ceduto ai tubi vaporizzatori che rivestono la camera segue la legge di Stefan-Boltzmann:

$$\mathbf{q_i = \frac{\alpha \cdot \sigma_0 \cdot S_{irr} \cdot (T_c^4 - T_p^4)}{\dot{m}_c}}$$

Dove:

- $\sigma_0$: Costante d'irraggiamento del corpo nero ($5{,}67 \times 10^{-8} \text{ W/(m}^2\text{K}^4)$)3.
- $\alpha$: Coefficiente correttivo per le proprietà geometriche, d'assorbimento ed emissività della camera3.
- $S_{irr}$: Superficie radiante efficace delle pareti raffreddate3.
- $T_c$: **Temperatura assoluta** media della **fiamma** $K$ ($T_c = t_c + 273{,}15$)3.
- $T_p$: **Temperatura assoluta** superficiale dei **tubi vaporizzatori** $K$

La **temperatura media di combustione (**$t_c$**)** rappresenta il livello termico dei fumi nella c.c. ed è condizionata dai seguenti parametri operativi4:

1. **Carico termico superficiale (**$\frac{\dot{m}_c}{S_{irr}}$**)**: $t_c$ **aumenta** all'aumentare della portata di combustibile $\dot{m}_c$ o al diminuire delle superfici radianti $S_{irr}$.
2. **Eccesso d'aria (**$e$**)**: $t_c$ **aumenta al diminuire dell'eccesso d'aria** $e$, poiché si riduce la massa d'aria inerte che diluisce il calore rilasciato4.
3. **Preriscaldamento dei reagenti**: $t_c$ **aumenta** al crescere dell'entalpia iniziale dell'aria comburente.

La temperatura di combustione si può calcolare per via grafica grazie a:
1. **Curva del Calore Disponibile** $f(t)$: Si definisce la funzione della potenza termica netta rimanente nei fumi: $$f(t) = \varepsilon \cdot K_i + H_r - q_i(t) \quad$$dove $H_r = M_a c_{pm,a} t_a + c_{pm,b} t_b$ rappresenta l'entalpia dei reagenti. Per $t \le t_p$, l'irraggiamento netto è nullo ($q_i = 0$), quindi $f(t_p) = \varepsilon K_i + H_r$. A temperature superiori a $t_p$, $q_i$ cresce con la quarta potenza, facendo decrescere la curva $f(t)$.
- **Curva dell'Entalpia dei Fumi** $H_f(t)$: Rappresenta l'energia contenuta nei fumi: $$H_f(t) = (M_a + 1) \cdot c_{pm,f}(t) \cdot t \quad$$Poiché $c_{pm,f}$ aumenta con la temperatura, la curva $H_f(t)$ ha un andamento leggermente parabolico/concavo verso l'alto.
- **Punto d'Intersezione** $P$: La temperatura di combustione effettiva $t = t_c$ viene individuata dal **punto di intersezione** $P$ tra la curva del calore netto $f(t)$ e la curva entalpica dei fumi $H_f(t)$.
![[determinazione_grafica_tc.png]]

Una temperatura di combustione $t_c$ troppo elevata comporta gravi inconvenienti:

- **Danneggiamento dei materiali**: Sollecitazioni termiche critiche sulle pareti e sui fasci tubieri.
- **Inquinamento ambientale**: Marcata formazione di **ossidi di azoto (**$\text{NO}_x$ **termici)** per via cinetica ad alta temperatura.

Per queste ragioni, nella progettazione della caldaia si sceglie con precisione il volume $V$, la geometria della camera e il grado di schermatura $\varphi$.
Per limitare $t_{c}$ ci sono soluzioni come:
- **Incremento** dell'**eccesso d'aria**, questo comporta ad una **diminuzione del rendimento del fgeneratore**($\eta_{gen}$).
- **Ridurre** $\frac{\dot{m_{c}}}{S_{irr}}$, facendo così diventare il calcolo $C_{t} =\frac{\dot{m_{c}} \cdot K_{i}}{S\cdot l}$, con $S$ **area delle pareti di c.c.**, $l$ **lunghezza caratteristica della c.c.**
Sia il **grado di raffreddamento** o di **schermatura** $\varphi$.
$$
\varphi = \frac{S_{irr}}{S} \to \frac{\dot{m_{c}}}{S_{irr}} = \frac{\dot{m_{c}}}{\varphi \cdot S} = \frac{C_{t}\cdot l}{\varphi \cdot K_{i}}
$$
Quindi si **agisce** sulle **dimensioni della camera di combustione**, $C_{t}$ e $\varphi$ **schermando** le pareti della camera di combustione.

## Posizione degli scambiatori di calore e diagramma di scambio termico

La **posizione degli scambiatori di calore** e la loro rappresentazione sul **diagramma di scambio termico (𝑇 −˙𝑄 o 𝑇 −ℎ)** svolgono un ruolo fondamentale nella progettazione e nel rendimento di un **generatore di vapore** (sia esso a combustione diretta o a recupero/HRSG).


## IL DIAGRAMMA DI SCAMBIO TERMICO 
Il diagramma descrive l'andamento della temperatura dei due fluidi in funzione del calore scambiato 𝑞:

![[Pasted image 20261023172948.png]]

- **Lato fumi/sorgente calda:**
    - In 𝑉, lo scambio avviene prevalentemente per **irraggiamento** e la temperatura dei fumi si mantiene elevata e costante a 𝑇𝑐 (sostenuta dalla fiamma).
    - Nei tratti successivi (𝑆, 𝑉′, 𝐸), lo scambio avviene prevalentemente per **convezione** e la temperatura diminuisce con andamento parabolico (dovuto al calore specifico dei fumi 𝑐𝑝𝑚,𝑓 che varia con 𝑇).
- **Lato acqua/vapore:** la curva del fluido operatore è divisa nei tre fasci tubieri caratteristici:
    1. **Preriscaldamento del liquido** (in **Economizzatore - E**): l'acqua passa dalla temperatura di ingresso 𝑇𝑂 fino a una temperatura 𝑇𝑂′ prossima a quella di vaporizzazione.
    2. **Vaporizzazione** (in **Vaporizzatore - V / V'**): avviene il cambio di fase da liquido saturo a vapore saturo secco (𝑂′ →𝐵) a temperatura costante 𝑇𝑣 =𝑇𝑠𝑎𝑡(𝑝).
    3. **Surriscaldamento** (in **Surriscaldatore - S**): il vapore saturo passa da 𝑇𝑣 fino alla temperatura di surriscaldamento finale 𝑇1 fissata per l'ingresso in turbina.

## Disposizione degli Scambiatori e Trasmissione del Calore
La disposizione fisica dei banchi lungo il percorso dei fumi è vincolata dalla trasmissione di calore tra fumi e fluido attraverso le pareti dei tubi 
$$
\frac{T_{1}-T_{p}}{T_{p}-T_{2}}=\frac{\alpha_{2}}{\alpha_{1}}
$$
, rispettivamente con 
- $\alpha_{1} \to T_{1} \to$ **coefficiente di trasmissione tra** fluido esterno e parete esterna
- $\alpha_{2} \to T_{2} \to$ **coefficiente di trasmissione tra** fluido interno e parete interna
- $T_{p} \to$ Temperature dei tubi surriscaldatori

![[Pasted image 20261023174539.png]]

### Sintesi dell'impatto complessivo

|Scambiatore / Parametro|Ruolo sul diagramma 𝑇 −𝑞|Effetto sul Generatore di Vapore|
|:--|:--|:--|
|**Surriscaldatore (𝑆)**|Eleva il vapore da 𝑇𝑣 a 𝑇1 a valle della camera di combustione|Fornisce vapore surriscaldato alla turbina; la disposizione in equicorrente/controcorrente (𝑆1/𝑆2) evita il surriscaldamento critico delle pareti (𝑇𝑝).|
|**Vaporizzatore (𝑉)**|Tratto orizzontale a 𝑇𝑣 =𝑇𝑠𝑎𝑡(𝑝) costante; irraggiamento in c.c.|𝛼𝑣 ≫𝛼𝑓 mantiene 𝑇𝑝 ≈𝑇𝑣 protetta dai fumi; limita 𝑇𝑐 e riduce la formazione di 𝑁𝑂𝑥 e i danni ai materiali refrattari.|
|**Economizzatore (𝐸)**|Preriscalda il liquido da 𝑇𝑂 a 𝑇𝑂′ nella zona a 𝑇𝑓𝑢𝑚𝑖 più bassa|Riduce la temperatura dei fumi 𝑇𝑢 aumentando il rendimento 𝜂𝑔𝑒𝑛; il limite inferiore di 𝑇𝑢 è fissato per prevenire le **rugiade acide** (𝐻2𝑆𝑂4).|
|**Profilo Fumi (𝑇𝑐 →𝑇𝑢)**|Irraggiamento a 𝑇𝑐 costante in c.c., seguito da decadimento parabolico convettivo|Definisce la disponibilità termica sfilabile per il salto entalpico totale dell'acqua/vapore fino alla temperatura di camino 𝑇𝑢.|
# Caldaia di Cornovaglia
La **caldaia Cornovaglia** (o _Cornish boiler_) è uno dei primi e più storici modelli di caldaia industriale a grande volume d'acqua, ampiamente utilizzata nel XIX secolo per la produzione di vapore a bassa e media pressione.

È una **caldaia a tubi di fumo ad alto volume d'acqua**, costituita da un grande corpo cilindrico orizzontale in lamiera d'acciaio riempito per circa due terzi d'acqua. All'interno del mantello d'acqua è immerso un **unico grande tubo focolare** (di diametro notevole) all'interno del quale avviene la combustione.
![[caldaia_cornovaglia_spaccato.png]]
## Come funziona?
1. **Il Tubo Focolare e la Combustione:**
    - La griglia su cui brucia il combustibile (solitamente carbone) si trova all'estremità anteriore, direttamente **all'interno del tubo focolare**.
    - I fumi caldi prodotti dalla combustione attraversano la lunghezza del tubo focolare cedendo calore, per conduzione attraverso la parete metallica, all'acqua che lo circonda.

2. **Giro dei Fumi:**
    - Una volta usciti dal tubo focolare sul fondo della caldaia, i fumi non vanno direttamente al camino, ma vengono fatti tornare indietro e poi ripassare attraverso appositi **condotti in muratura** ricavati esternamente sotto e ai lati del mantello cilindrico, massimizzando lo scambio termico con l'acqua prima di essere espulsi.

3. **Posizione Eccentrica del Tubo Focolare:**
    - Il tubo focolare non è posizionato al centro perfetto del mantello, ma è installato **in posizione eccentrica** (spostato verso il basso/un lato).
    - **Motivo:** Questa assimmetria genera e induce la **circolazione naturale dell'acqua** all'interno del corpo cilindrico per moti convettivi (l'acqua calda risale attorno al focolare, quella più fredda discende sui lati), evitando il ristagno e facilitando il distacco delle bolle di vapore.

4. **Il Duomo di Vapore:**    
    - Sulla parte superiore del mantello cilindrico è presente una cupola chiamata **duomo**.
    - Funziona come **camera di calma**: il vapore prodotto sulla superficie libera dell'acqua risale nel duomo, dove la velocità del flusso diminuisce consentendo alle goccioline d'acqua trascinate di separarsi per gravità e ricadere in caldaia. Da qui viene prelevato **vapore praticamente secco** verso la turbina o l'utenza.

5. **Tubo Focolare ad Onda/Superficie Ondulata:**
    - Per resistere alle alte pressioni ed evitare l'inflessione, la parete del tubo focolare viene realizzata con ondulazioni perimetrali.
    - L'ondulazione garantisce due vantaggi:
        - **Aumenta la superficie di scambio termico** a parità di lunghezza del tubo.
        - **Aumenta la stabilità elastica e meccanica** della parete soggetti alla pressione esterna dell'acqua.

## Caldaie a tubi di fumo
Le **caldaie a tubi di fumo** rappresentano l'evoluzione diretta delle caldaie tipo Cornovaglia, nate per rispondere alla necessità di **aumentare la superficie di scambio termico, la pressione di esercizio e la potenza termica unitaria**.

A differenza della caldaia Cornovaglia (che possedeva un solo grande tubo focolare), nelle caldaie a tubi di fumo il ruolo di scambiatore di calore viene affidato a una **fitta fascera di molti tubi di piccolo diametro**, detti appunto **tubi da fumo**.

### Come funzionano ?
- **Struttura:** Un grande mantello cilindrico riempito d'acqua, all'interno del quale sono totalmente **annegati nell'acqua** sia un focolare di lunghezza contenuta, sia una molteplicità di tubi da fumo paralelli.
- **Flusso dei fluidi:**
    - **All'interno dei tubi:** scorrono i **fumi caldi** della combustione.
    - **All'esterno dei tubi:** c'è l'**acqua** da riscaldare/evaporare.

1. **Combustione nel Tubo Focolare:** La combustione del combustibile avviene all'interno del focolare principale (anch'esso corto e annegato in acqua).
2. **Passaggio nella Cassa da Fumo e nei Tubi:** I fumi caldi prodotti escono dal focolare e confluiscono in una camera detta **cassa da fumo**. Da qui vengono distribuiti e fatti passare attraverso i numerosi tubi da fumo.
3. **Scambio Termico:** Passando nei tubi di piccolo diametro, i fumi offrono un'area di contatto complessiva enormemente superiore rispetto a quella di un unico tubo. Cedono così il loro calore per conduzione attraverso le pareti dei tubi all'acqua circostante, provocandone l'ebollizione.
4. **Espulsione al Camino:** I fumi raffreddati escono dai tubi, vengono raccolti nella cassa fumi opposta ed espulsi attraverso il **camino**.

![[caldaia_tubi_di_fumo_spaccato.png]]

# Caldaia Babcok a tubi d'acqua
La **Caldaia Babcock** rappresenta una vera e propria rivoluzione tecnologica nei generatori di vapore, basata sull'**inversione del principio di funzionamento**:

## Concetto FONDAMENTALE
- **Nei tubi:** scorre l'**acqua** (e la miscela acqua/vapore).
- **All'esterno dei tubi:** scorrono i **fumi caldi** della combustione, che lambiscono esternamente i banchi tubieri.
- Contenere l'acqua a forte pressione all'interno di **tubi di piccolo diametro** (<100 mm) permette di sopportare **pressioni di esercizio e potenze termiche nettamente superiori**, riducendo gli spessori delle pareti metalliche (per la legge di Mariotte, la sollecitazione nel tubo è proporzionale al diametro).
- Aumenta enormemente la superficie di scambio termico e la sicurezza d'impianto (in caso di rottura di un piccolo tubo d'acqua si ha un danno contenuto, mentre la rottura di un grande mantello in pressione sarebbe catastrofica).
![[caldaia_babcock_wilcox_spaccato.png]]


## Come funziona?
1. **Presenza di tutti e 3 i fasci tubieri:** Introduce chiaramente la separazione funzionale tra **Economizzatore (E)**, **Vaporizzatore (V)** e **Surriscaldatore (S)**.
2. **Disposizione dei banchi:** Il primo fascio tubiero direttamente lambito dai fumi caldi uscenti dalla camera di combustione è il **vaporizzatore (V)**.
3. **Circolazione Naturale:** Il fluido all'interno del circuito vaporizzatore circola grazie alla **differenza di densità** tra la fase liquida (𝜌𝑙) presente nel tubo discendente e la miscela bifase acqua-vapore (𝜌𝑙𝑣) presente nel tubo montante riscaldato dai fumi

$$
\Delta p = (pv+g\rho lH)-(pv+g\rho lv(H-\Delta H)) = gH(\rho l-\rho lv)g\rho lv\Delta H
$$
Questa differenza di carico idrostatico spinge naturalmente l'acqua a circolare nel circuito senza bisogno di pompe di circolazione aggiuntive (valido per pressioni d'esercizio subcritiche, tipicamente <160 bar).

# Caldaie ad irraggiamento
Le **caldaie ad irraggiamento** nascono per soddisfare la necessità di produrre **potenze termiche molto elevate (> 100 MW)**, risolvendo al contempo i problemi critici legati alle temperature troppo alte della camera di combustione.

Nelle caldaie di grande potenza, se la camera di combustione non è adeguatamente raffreddata, si verificano tre gravi problemi:

1. **Danneggiamento dei materiali refrattari** della camera.
2. **Formazione di 𝑁𝑂𝑥**, favorita dalle temperature di combustione molto elevate e dall'eccesso di ossigeno.
3. **Depositi di ceneri pastose** sulle superfici di scambio (nel caso di combustibili solidi o liquidi pesanti).

Per evitare tutto ciò, si aumenta il cosiddetto **grado di raffreddamento (o di schermatura) 𝜑**:  
$$
\varphi=\frac{S_{irr}}{S}
$$
Ossia si realizzano camere di combustione le cui pareti sono interamente schermate da tubi vaporizzatori ravvicinati, capaci di assorbire direttamente il calore per irraggiamento dalla fiamma.

## Come funzionano?
![[caldaia_ad_irraggiamento_spaccato.png]]
Il ciclo dell'acqua/vapore all'interno di una caldaia ad irraggiamento si sviluppa attraverso i seguenti componenti e passaggi chiave:

1. **Pre-riscaldamento:** L'acqua di alimento viene preriscaldata esternamente (tramite sistemi di rigenerazione con gli spillamenti della turbina) e poi passa all'interno dei fasci **economizzatori** sfruttando il calore dei fumi in uscita.
2. **Alimentazione del Vaporizzatore:** L'acqua entra nel **collettore inferiore 𝐶𝑎** (dove lo stato fluido è puramente liquido) e sale attraverso i **tubi vaporizzatori 𝑉** che rivestono e schermano la camera di combustione.
3. **Assorbimento del Calore per Irraggiamento:** All'interno di questi tubi, l'acqua riceve il calore radiante della fiamma e vaporizza parzialmente. La miscela risultante (liquido/vapore) si raccoglie nel **collettore superiore 𝐶𝑣**.
4. **Separazione:** La miscela passa attraverso un **corpo separatore (𝑆𝑉)**, che separa l'acqua residua dal vapore saturo.
5. **Surriscaldamento:** Il vapore saturo viene inviato ai **fasci surriscaldatori**:
    - **Primo banco (𝑆1):** Spesso disposto in **equicorrente** nella zona a fumi più caldi, per limitare la temperatura delle pareti dei tubi ed evitare surriscaldamenti critici del metallo.
    - **Secondo banco (𝑆2):** Disposto in **controcorrente** nella zona successiva, dove la temperatura dei fumi è ormai sufficientemente bassa per raggiungere la temperatura finale di surriscaldamento richiesta dalla turbina.

- **Circolazione Naturale:** È garantita dalla differenza di volume specifico (e quindi di densità) tra la fase liquida e la fase gassosa all'interno del circuito. Funziona finché la pressione di esercizio è **inferiore a quella critica** (circa 221 bar).
- **Limiti dell'alta pressione e Circolazione Forzata:**  
    Al crescere della pressione di esercizio, il differenziale di pressione indotto dalla differenza di volume specifico diminuisce progressivamente (perché l'acqua e il vapore diventano via via simili come densità). **Sopra i 160 bar**, la circolazione naturale non è più sufficiente e si applica obbligatoriamente la **circolazione forzata** mediante pompe di circolazione dedicate.

## Preriscaldatore a masse di accumulo Ljungström
Il **preriscaldatore a masse di accumulo Ljungström** (noto anche come preriscaldatore rigenerativo rotativo) è un dispositivo utilizzato per recuperare il calore termico dai fumi di scarico di una caldaia e cederlo all'aria fresca in ingresso.

Si tratta di un grande **tamburo cilindrico rotante** (che ruota a bassa velocità, circa 3 giri al minuto) suddiviso in settori e riempito internamente da **lamierini sottili di metallo** ad altissima superficie specifica

Il tamburo è posizionato in modo tale che la sua sezione sia divisa a metà da setti fissi:
- Una metà del tamburo è lambita dai **gas caldi (fumi)** in uscita dalla caldaia.
- L'altra metà è lambita dall'**aria fredda** proveniente dall'esterno diretta alla camera di combustione.

Il principio di funzionamento è di tipo **rigenerativo a contatto indiretto**:

1. **Fase di riscaldamento (Accumulo):** Mentre i lamierini metallici ruotano attraversando il settore dei gas caldi, assorbono ed accumulano il calore termico dei fumi in uscita.
2. **Fase di raffreddamento (Cessione):** Continuando a ruotare, quei stessi lamierini caldi passano nel settore opposto, dove vengono investiti dall'aria fredda in ingresso. Qui rilasciano il calore accumulato, preriscaldando l'aria prima che entri nella camera di combustione.
![[Pasted image 20261023185348.png]]

