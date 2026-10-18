Gli **impianti cogenerativi** (noti anche come sistemi **CHP –** **Combined Heat and Power**) sono sistemi energetici progettati per la **produzione simultanea di energia elettrica (o meccanica) e calore utile** a partire da un'unica fonte primaria di energia (combustibile fossile o biomassa).
# HCP
Esistono diversi tipi di sistemi HCP, i quali possono essere divisi in:
1) Sistemi generatori di potenza ad energia con recupero termico di calore.
2) Sistemi di energia primaria con recupero di calore ed introduzione di energia supplementare.
3) Sistema di recupero termico da generatori di calore per produzione di potenza
4) Sistema di recupero di calore per la produzione di potenza e ulteriore recupero a valle del generatore di potenza

## INDICI
- # IUC
	Questo è il **coefficiente di utilizzo**, ed esprime la quantità di combustibile valorizzata nell'impianto:
	$$
		\begin{align}
		\eta _{u} = \frac{P_{e}+P_{t}}{P_{c}} = \frac{P_{e}}{P_{t}} + \frac{P_{t}}{P_{c}} = u_{e} + u_{t} < 1  \\
		\eta_{e} = \frac{P_{e}}{P_{c}} \to rendimento \space elettrico \\
		\eta_{t} = \frac{P_{t}}{P_{c}} \to rendimento \space termico \\
		\eta_{u} = \eta_{e} + \eta_{t} \\
		\end{align}
	$$
- # INDICE ELETTRICO
	L’Indice Elettrico **definisce** la **propensione** di un particolare impianto **per la produzione elettrica piuttosto che termica**, $$I_{e} = \frac{P_{e}}{P_{t}}$$
- # INDICE DI RISPARMIO ENERGETICO
	Definisce il **confronto** fra la **produzione separata** e la **produzione cogenerativa** della stessa potenza elettrica e termica.
	
	Per capire se conviene mantenere 2 centrali (1 termica, 1 elettrica), o avere un sistema cogenerativo, bisogna ideare un metodo di comparazione tra i 2 metodi.
	per questo si usa **IRE**, un indice che avente la stessa gli stessi valori nelle uscite di $P_e$ e $P_t$ in base a quanto combustibile viene consumato dai 2 metodi. 
	$$
		IRE = \frac{P_{cs} - P_{c}}{P_{cs}} = 1-\frac{P_{c}}{P_{cs}} = 1-\frac{P_{c}}{P_{cse}+P_{cst}} = 1 - \frac{1}{\frac{P_{cse}}{P_{c}} + \frac{P_{cst}}{P_{c}}} =1 - \frac{1}{\frac{P_{cse}}{P_{e}} \frac{P_{e}}{P_{c}} + \frac{P_{cst}}{P_{t}} \frac{P_{t}}{P_{c}}} \\= 1 - \frac{1}{\frac{\eta_{e}}{\eta_{es}} + \frac{\eta_{t}}{\eta ts}} 
	$$
	![[Pasted image 20261017001807.png]]
	
	
	Un impianto con sistema cogenerativo viene deciso su un sistema separato quando:
	- $IRE \le 0$ $\rightarrow$ **NON CONVENIENTE** L'impianto cogenerativo consuma una quantità di energia primaria pari o superiore rispetto alla produzione separata. L'intervento è termodinamicamente ed energeticamente inefficiente.
	- $IRE > 0$ $\rightarrow$ **CONVENIENTE (Risparmio Energetico)** Il CHP consuma meno energia primaria rispetto alla produzione separata. Per micro e piccoli impianti (sotto $1\text{ MW}_e$), un $IRE > 0$ è sufficiente per garantire il risparmio di combustibile e accedere alla qualifica di **CAR (Cogenerazione ad Alto Rendimento)**.
	- $IRE \ge 10\%$ **(0,10)** $\rightarrow$ **ALTAMENTE CONVENIENTE (Cogenerazione ad Alto Rendimento - CAR)** Per impianti medio-grandi ($\ge 1\text{ MW}_e$), la normativa richiede che l'IRE sia almeno del **10%**. In questo caso si ottiene il riconoscimento **CAR**, che dà diritto agli incentivi statali (es. **Certificati Bianchi / TEE**) aumentando drasticamente la redditività finanziaria.
	![[cogenerazione_ire_diagramma.png]]
- # IRE RIFERITO ALL'ENERGIA
	L’IRE riferito alla **potenza** è più adatto a **descrivere** le **prestazioni massime dell’impianto cogenerativo** mentre riferito all’**energia** **descrive** il **comportamento** effettivo **durante il funzionamento.**
	$$
	\begin{align}
	IRE = \frac{ \int^{\Delta t}_{0} P_{cs}(t)dt - \int^{\Delta t}_{0} P_{c}(t)dt }{\int^{\Delta t}_{0} P_{cs}(t)dt} \\
	IRE = 1 - \frac{1}{\frac{\eta_{e}}{\eta_{es}} + \frac{\eta_{t}}{\eta_{ts}}} \\
	\end{align}
	$$
	- $\eta_{e}  = \frac{E_{e}}{E_{c}} \to$ **Rendimento elettrico impianto cogenerativo**
	- $\eta_{t}  = \frac{E_{t}}{E_{c}} \to$ **Rendimento elettrico impianto cogenerativo**
	- $\eta_{es}  = \frac{E_{e}}{E_{cse}} \to$ **Rendimento elettrico impianto separato**
	- $\eta_{ts}  = \frac{E_{t}}{E_{cst}} \to$ **Rendimento elettrico impianto cogenerativo**
- # INDICE RISPARMIO ECONOMICO (IREC)
	L’IREC valuta l’impianto cogenerativo rispetto all’**acquisto** di energia elettrica e/o termica. 
	$$
		IREC = \frac{C_{s}-C}{C_{s}} = 1 - \frac{1}{\frac{\eta_{e}}{\frac{\lambda}{\zeta_{e}}} + \frac{\eta_{t}}{\frac{\lambda}{\zeta_{t}}}}
	$$
	- $C_{s} \to$ **Costo dell'acquisto esterno** di $E_{e}$ e $E_{t}$
	- $C \to$ **Costo acquisto combustibile** impianto cogenerativo per produrre $E_{e}$ e $E_{t}$
	- $\lambda \to$ **costo specifico del combustibile dell’impianto cogenerativo**
	- $\zeta_{e} \to$ **costo specifico acquisto energia elettrica** $E_{e}$
	- $\zeta_{t} \to$ **costo specifico acquisto energia termica** $E_{t}$
	
	- $IREC \le 0$ $\rightarrow$ **Economicamente NON conveniente** (l'autoproduzione costa più della spesa energetica tradizionale).
	- $IREC > 0$ $\rightarrow$ **Economicamente CONVENIENTE** (si genera un margine operativo annuo positivo $\Delta C = C_{sep} - C_{CHP} > 0$).
	![[cogenerazione_isec_diagramma.png|660]]


# Principali tipologie di impianti cogenerativi
1. Impianti con Turbina a Gas (TG) e Caldaia a Recupero (HRSG)

- **Funzionamento**: La turbina a gas produce potenza elettrica. I fumi di scarico esausti ad alta temperatura ($500\text{–}600\text{ °C}$) vengono inviati a una **caldaia a recupero (HRSG)** per generare vapore o acqua calda utili per l'utenza.
- **Applicazioni**: Centrali industriali di media/grande taglia e teleriscaldamento urbano.

---

2. Impianti con Turbina a Vapore (TV)

Utilizzano un ciclo Rankine/Rankine-Hirn e si dividono in due configurazioni principali:

- **A Contropressione**: Il vapore si espande in turbina fino alla pressione/temperatura richiesta dal processo industriale e viene scaricato interamente verso l'utenza termica (senza condensatore tradizionale).
- **A Spillamento (e Condensazione)**: Una parte del vapore viene prelevata (_spillata_) a pressione intermedia per soddisfare il carico termico, mentre la quota restante prosegue l'espansione fino al condensatore.

---

3. Impianti con Motore a Combustione Interna (MCI)

- **Funzionamento**: Utilizzano motori alternativi (a gas naturale o diesel). Il recupero termico è duale:
    1. **Alta temperatura**: dai fumi di scarico ($400\text{–}500\text{ °C}$).
    2. **Bassa/media temperatura**: dal circuito di raffreddamento del motore e dell'olio ($80\text{–}90\text{ °C}$).
    Infatti viene recuperato il calore contenuto nei fumi di scarico e nei fluidi di raffreddamento del motore.

- **Applicazioni**: Ospedali, centri commerciali, piccole/medie industrie e micro-cogenerazione terziaria.

---

4. Cicli Combinati Cogenerativi (CCGT-CHP)

- **Funzionamento**: Integrano un ciclo a gas e un ciclo a vapore. Il calore di scarico del turbogas genera vapore nell'HRSG; una quota di questo vapore (o del vapore spillato dalla turbina) viene destinata all'utenza termica anziché alla sola produzione elettrica.
- **Applicazioni**: Grandi centrali termoelettriche e reti cittadine di teleriscaldamento ad altissima efficienza.

Questi vengono scelti in base all'applicazione dell'impianto, e vengono decisi grazie a questi criteri:
- **Taglia**
	- $>25MW \to$ Turbina a vapore
	- $> 5MW \to$ Turbine a gas
	- $< 5MW\to$ ICE a ciclo diesel
	- $<1MW\to$ ICE  a ciclo Otto
- **Produzione principale**
- **Temperatura**
- **Variabilità delle utenze**

# GRUPPO Cogenerativo con Turbina a Gas
Questi impianti sono caratterizzati da semplicità, bassi costi d’investimento e da un layout analogo ai cicli combinati (senza TV).

L'impianto si compone di tre sezioni fondamentali disposte in cascata:

1. **Turbina a Gas (TG)**:
    - **Compressore**: Aspira aria dall'ambiente e la comprime ad alta pressione.
    - **Camera di Combustione**: Il combustibile (solitamente gas naturale) brucia con un forte eccesso d'aria, innalzando la temperatura dei gas fino alla temperatura di picco.
    - **Turbina di Espansione**: I gas caldi si espandono producendo potenza meccanica, usata sia per trascinare il compressore sia per azionare l'alternatore che eroga la **potenza elettrica (**$P_{el}$**)**.
2. **Fumi di Scarico Esausti**:
    - All'uscita della turbina a gas, i fumi si trovano ancora ad **alta temperatura (**$500\text{–}600\text{ °C}$**)** ed elevata portata, e contengono un'abbondante percentuale di ossigeno incombusto ($12\text{–}15\%$ in volume).
3. **Caldaia a Recupero (HRSG)**:
    - Sfrutta il contenuto termico dei fumi per riscaldare l'acqua e produrre vapore o acqua calda senza bruciare ulteriore combustibile.
    - Internamente è suddivisa in **Surriscaldatore**, **Evaporatore** ed **Economizzatore**, regolati dai salti termici di **Pinch Point**.
4. **Utenza Termica**:
    - Il vapore o l'acqua surriscaldata prodotti nell'HRSG vengono inviati ai processi industriali (chimica, cartiere, alimentare) o alla rete di teleriscaldamento, erogando la **potenza termica utile (**$\dot{Q}_{th}$**)**.
![[gruppo_cogenerativo_tg_hrsg_layout-v2.png]]

![[Pasted image 20261019003741.png]]

L'**efficienza** del **recuperatore termico**, viene calcolato tramite:
$$
\sigma = \frac{P_{T,reale}}{P_{t,ideale}} = \frac{\dot{m_{v}}(h_{a}-h_{o})}{\dot{m_{a}}c_{p}(T_{4'}-T_{o})} = \frac{T_{4'}-T_{5}}{T_{4'}-t_{0}}\\
\dot{Q}_{scambiato} = \dot{m_{a}}c_{p}(T_{4'}-T_{5}) 
$$
---
Quando si parla di potenze, in questo tipo d'impianto si deve **dividere** la **potenza elettrica, generata dalla turbina a gas**, dalla **potenza termica data all'utenza termica.**

**TG**
A sua volta la potenza elettrica si deve calcolare tenendo conto anche dalla potenza del compressore.
$$
\begin{align}
P_{c} = \dot{m_{c}}k_{i} = \frac{\dot{m_{a}}c_{p}(T_{3}-T_{2'})}{\eta_{cc}} \\
P_{e} = \dot{m_{a}}c_{p}\left[ (T_{3}-T_{4})\eta_{i,T}- \frac{T_{2}-T_{2}}{\eta_{iC}} \right]\eta_{mTG}\cdot\eta_{auxTG}\cdot\eta_{altTG} 
\end{align}
$$
---
**UT**
$$
P_{t} = \dot{m_{v}}\cdot(h_{a}-h_{b})
$$



