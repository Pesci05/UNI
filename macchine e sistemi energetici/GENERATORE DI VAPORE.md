I **generatori di vapore** (comunemente chiamati anche **caldaie**) sono apparecchiature termiche e scambiatori di calore complessi il cui scopo fondamentale è trasformare l'acqua liquida di alimento in vapore d'acqua ad elevate condizioni di pressione e temperatura, somministrando energia termica.

All'interno dei **sistemi energetici a vapore (cicli Rankine-Hirn)** e degli **impianti combinati e cogenerativi**, il generatore di vapore costituisce il cuore della sorgente calda del ciclo.

**Impianti a Vapore Convenzionali (Ciclo Rankine-Hirn)**: Il generatore di vapore brucia direttamente un combustibile (gas naturale, carbone, biomassa) per produrre il vapore surriscaldato ad alta pressione che s'espanderà poi nella turbina a vapore.

**Cicli Combinati (CCGT) e Cogenerativi (TG + HRSG)**: Assume la forma della **Caldaia a Recupero (HRSG —** **Heat Recovery Steam Generator** **)**, in cui il calore non deriva da una combustione diretta ma dal raffreddamento dei fumi caldi di scarico della turbina a gas.

Per ottimizzare lo scambio termico ed evitare shock termici, la trasformazione dell'acqua in vapore avviene attraversando **tre sezioni principali disposte in serie**:
1. **ECONOMIZZATORE**
	Riceve l'acqua liquida compressa dalla pompa di alimento e la preriscalda sfruttando i fumi a temperatura più bassa, portandola in prossimità della temperatura di saturazione.
2. **EVAPORIZZATORE**
	Compie il cambio di fase da acqua liquida satura a vapore saturo secco a pressione e temperatura costanti.
3. **SURRISCALDATORE**
	Riceve il vapore saturo secco e ne innalza ulteriormente la temperatura al di sopra della temperatura di saturazione, producendo **vapore surriscaldato** ad alta entalpia prima dell'ingresso in turbina a vapore.
![[Pasted image 20261021161558.png|549]]
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

