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

