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

---
Per poter variare le $P_{e}$ e $P_{t}$ si deve avere un certo tipo di configurazione.
Che introduce il camio di bypass, e anche una **seconda camera di combustione**.

Bypass Fumi (_Diverter Damper_)
- **Scopo**: Ridurre la potenza termica $\dot{Q}_{th}$ mantenendo elevata la potenza elettrica $P_{el}$.
- **Principio**: Se l'utenza riduce la richiesta di calore ma necessita di piena potenza elettrica, una valvola a tre vie sul condotto dei fumi devia una quota dei fumi caldi direttamente al camino, "scavalcando" l'HRSG.
![[gruppo_cogenerativo_tg_hrsg_bypass_layout-v2.png]]

- $\alpha = 0$ **(Serranda al bypass completamente chiusa)**:
    - **100% dei fumi entra nell'HRSG**. L'impianto opera nel massimo assetto cogenerativo (massima potenza termica erogabile $\dot{Q}_{th, max}$).
- $0 < \alpha < 1$ **(Modulazione parziale del carico termico)**:
    - Una frazione dei fumi viene scaricata dal camino di bypass. Ciò consente di **ridurre a piacimento la potenza termica erogata all'utenza (**$\dot{Q}_{th}$**)** per inseguire la domanda termica, **mantenendo la turbina a gas a pieno carico elettrico (**$P_{el}$ **costante)**.
- $\alpha = 1$ **(Serranda verso l'HRSG completamente chiusa)**:
    - **100% dei fumi viene inviato al camino di bypass**. L'impianto funziona in **assetto puramente elettrico (**$\dot{Q}_{th} = 0$**)**.
    - _Vantaggio operativo_: consente la manutenzione o l'ispezione della caldaia HRSG senza dover spegnere la turbina a gas e senza interrompere la fornitura di energia elettrica alla rete.


# Gruppo Cogenerativo con turbina a vapore
**TURBINA IN CONTROPRESSIONE**

L'Impianto si basa sul **cicli HIRN-RANKINE**
![[Pasted image 20261019233357.png]]
![[Pasted image 20261019233449.png]]

- Le turbine in contropressione sono caratterizzate da una pressione di uscita simile a quella richiesta dall’utenza termica (5-6 bar). 
- Queste **TV** non possono funzionare in mancanza di un utenza termica. 
- Sono utilizzate quando l’**utenza termica è privilegiata su quella elettrica**. 
- Sc (scaricatore di condensa) e la valvola V1 producono una laminazione isoentalpica.
- **V1 parzializza la portata di vapore** togliendolo dalla disponibilità di TV. 
- La richiesta dell’utenza termica incide sulla portata di TV e quindi su $P_{e}$. 

Le potenze che genera questo gruppo sono:
$$
P_{c} = \dot{m_{c}}\cdot k_{i} = \frac{\dot{m_{v}}\cdot(h_{a}-h_{o})}{\eta_{g}}\\
P_{e} = \dot{m_{T}}\cdot(h_{a}-h_{bt})\cdot \eta_{i}\cdot \eta_{m}\cdot \eta_{aux}\cdot \eta_{alt} \\
P_{t} = \dot{m_{v}}\cdot(h_{d}-h_{e})
$$
Questo gruppo può avere dei casi estremi come:
**POTENZA ELETTRICA MASSIMA**
$$
\dot{m_{T}} = \dot{m_{v}} \\
P_{e} = \dot{m_{T}}\cdot(h_{a}-h_{bt})\cdot \eta_{i}\cdot \eta_{m}\cdot \eta_{aux}\cdot \eta_{alt} \\
P_{t} = \dot{m_{v}}\cdot(h_{b}-h_{e})
$$
**POTENZA TERMICA MASSIMA**
$$
\dot{m_{T}} = 0 \\
P_{e} = 0 \\
P_{t} = \dot{m_{v}}\cdot(h_{c}-h_{e})
$$
---
**TURBINA IN DERIVAZIONE**
Le turbine in **derivazione** consentono di **espandere** il fluido fino a raggiungere **pressioni inferiori a quella atm**.
Sono utilizzate quando è **privilegiata l’utenza elettrica rispetto a quella termica**.

Questo gruppo è formato da:
- **Generatore di Vapore (Caldaia)**: Produce la portata totale di vapore surriscaldato ad alta pressione ($\dot{m}_v, p_{HP}, T_{HP}$).
- **Sezione di Alta Pressione (Turbina AP)**: Il vapore si espande producendo la prima quota di lavoro elettrico fino a raggiungere una pressione intermedia ($p_{spill}$).
- **Nodo di Derivazione / Spillevamento**: All'uscita dalla sezione AP, il flusso si sdoppia tramite una valvola di regolazione:
    - **Quota Spillata/Derivata (**$\dot{m}_{th}$**)**: Viene estratta alla pressione $p_{spill}$ e inviata all'**Utenza Termica** (condensatore utile), dove condensa cedendo la **potenza termica utile (**$\dot{Q}_{th}$**)**.
    - **Quota Rimanente (**$\dot{m}_{cond} = \dot{m}_v - \dot{m}_{th}$**)**: Prosegue l'espansione nella **Sezione di Bassa Pressione (Turbina BP)** fino alla pressione di vuoto del **Condensatore Freddo** ($p_{cond} \approx 0{,}04\text{–}0{,}08\text{ bar}$).
- **Condensatore Freddo**: Dissipa verso l'ambiente (es. torre evaporativa o fiume) il calore del vapore non richiesto dall'utenza termica.
- **Ritorno Condensa**: Le condense provenienti sia dall'utenza che dal condensatore freddo si uniscono e vengono ricondotte in caldaia tramite la **Pompa di Alimento (PA)**.
![[gruppo_cogenerativo_tv_derivazione_layout_ts.png]]
- **Tratto** $1 \rightarrow 2 \rightarrow 3 \rightarrow 4$ **(Rosso)**: Riscaldamento dell'acqua, evaporazione isotermo-isobara ed elevato surriscaldamento fino a $T_4 = 500\text{ °C}$ sulla pressione massima $p_{HP} = 80\text{ bar}$ (Stato **4**).
- **Tratto** $4 \rightarrow M$ **(Verde Chiaro)**: Prima espansione nella **Turbina AP** fino alla pressione intermediata di spillevamento $p_{spill} = 5\text{ bar}$ (Stato **M**).
- **Biforcazione del Flusso al Punto** $M$:
    - **Tratto** $M \rightarrow 6_U$ **(Linea Tratteggiata Viola)**: La quota di vapore spillata $\dot{m}_{th}$ condensa a pressione e temperatura costanti ($T_{sat} \approx 152\text{ °C}$) cedendo il calore latente all'**Utenza Termica** (effetto cogenerativo $Q_{th}$).
    - **Tratto** $M \rightarrow 5_C$ **(Verde Scuro)**: La frazione restante $\dot{m}_v - \dot{m}_{th}$ prosegue l'espansione nella **Turbina BP** fino alla pressione di vuoto $p_{cond} = 0{,}05\text{ bar}$ (Stato $5_C$).
- **Tratto** $5_C \rightarrow 6_C$ **(Azzurro Puntinato)**: Condensazione nel **Condensatore Freddo** a $T \approx 33\text{ °C}$ con rigetto del calore non recuperabile $Q_{lost}$.
- **Tratto** $6_C / 6_U \rightarrow 1$ **(Blu Tratteggiato)**: Ricircolo e pompaggio delle condense miscelate alla pressione $p_{HP}$.
$$
h_{6c} = \frac{(\dot{m_{v}}-\dot{m}_{TAP})\cdot h_{c}+\dot{m}_{TAP}\cdot h_{b}}{\dot{m_{v}}}\\
P_{c} = \dot{m_{c}}\cdot k_{i} = \frac{\dot{m_{v}}\cdot(h_{a}-h_{o})}{\eta_g}\\
P_{e} = [\dot{m}_{TAP}\cdot(h_{a}-h_{bt})\cdot \eta_{i,TAP}\cdot \eta_{m,TAP} + \dot{m}_{TBP} \cdot (h_{d}-h_{kt}) \cdot \eta_{i,TBP} \cdot \eta_{m,TBP}] \eta_{aux}\cdot \eta_{alt}\\
P_{t} = \dot{m}_{UT}\cdot(h_{d}-h_{e})
$$
Questo gruppo può avere dei casi estremi come:
**POTENZA ELETTRICA MASSIMA**
$$
\dot{m}_{TAP} = \dot{m}_{TBP} = \dot{m_{v}}\\
P_{e} = \dot{m_{v}}\cdot[(h_{a}-h_{bt})\cdot \eta_{i,TAP} \cdot \eta_{m,TAP} +  (h_{b}-h_{kt}) \cdot \eta_{i,TBP} \cdot \eta_{m,TBP}]\cdot \eta_{aux} \cdot \eta_{alt} \\
P_{t} = 0
$$

**POTENZA TERMICA MASSIMA**
$$
\dot{m}_{TAP} = \dot{m}_{TBP} = 0 ; \space \dot{m}_{UT} = \dot{m_{v}}\\
P_{e} = 0 \\
P_{t} = \dot{m_{v}}\cdot(h_{c}-h_{e})
$$

**PORTATA DISTRIBUITA**
$$
\dot{m}_{UT} = \dot{m}_{TBP} ; \space \dot{m}_{TAP} = \dot{m_{v}}\\
P_{e} = [\dot{m_{v}}\cdot(h_{a}-h_{bt})\cdot \eta_{i,TAP} \cdot \eta_{m,TAP} +  \dot{m}_{TBP}\cdot(h_{b}-h_{kt}) \cdot \eta_{i,TBP} \cdot \eta_{m,TBP}]\cdot \eta_{aux} \cdot \eta_{alt} \\
P_{t} = \dot{m}_{UT}\cdot(h_{b}-h_{e})
$$

# GRUPPO COMBINATO COGENERATIVO - VAPORE COGENERATIVO
In una caldaia a recupero ad un solo livello di pressione, il processo di evaporazione dell'acqua avviene a una singola temperatura fissa $T_{sat}$. Di conseguenza, sul diagramma dello scambio termico $T-Q$, si crea un considerevole "divario" (salto termico) tra la linea di raffreddamento dei fumi e la curva dell'acqua/vapore. Questo divario rappresenta una forte **distruzione di energetica (irreversibilità)**.

Il layout del gruppo è definito da:
1. **Sezione Turbina a Gas (TG)**:
    - Il turbogas brucia il combustibile ($\dot{Q}_{in}$), produce la prima quota di **potenza elettrica (**$P_{el, TG}$**)** e scarica i fumi esausti ad alta temperatura ($550\text{--}600\ ^\circ\text{C}$).
2. **Caldaia a Recupero a 2 Livelli (HRSG 2LP)**: I fumi attraversano in sequenza 6 banchi di scambiatori disposti in controcorrente:
    - **Sezione AP**: Surriscaldatore AP ($SH_{AP}$), Evaporatore AP con corpo d'allevamento ($EVA_{AP} + D_{AP}$), Economizzatore AP ($ECO_{AP}$).
    - **Sezione BP**: Surriscaldatore BP ($SH_{BP}$), Evaporatore BP con corpo d'allevamento ($EVA_{BP} + D_{BP}$), Economizzatore BP ($ECO_{BP}$).
    - **Camino**: I fumi esausti vengono espulsi a $\sim 100\ ^\circ\text{C}$.
3. **Turbina a Vapore a Spillevamento & Utenza Termica (CHP)**:
    - Il vapore surriscaldato AP ($80\text{--}100\text{ bar}, 520\ ^\circ\text{C}$) entra nella **Turbina a Vapore AP (**$TV_{AP}$**)**.
    - Il vapore uscente da $TV_{AP}$ si miscela con il vapore prodotto dalla sezione BP ($6\text{--}10\text{ bar}$) ed entra nella **Turbina a Vapore BP (**$TV_{BP}$**)**.
    - **Spillamento Cogenerativo**: Dalla sezione intermedia/BP viene estratta la portata di vapore inviata all'**Utenza Termica** per soddisfare il carico di processo/riscaldamento ($\dot{Q}_{th}$).
    - La frazione rimanente espande fino al vuoto nel **Condensatore Freddo** per massimizzare la **potenza elettrica (**$P_{el, TV}$**)**.
    - Le condense raccolte vengono ripressurizzate dalle pompe di alimento $P_{BP}$ e $P_{AP}$ e ricircolate all'HRSG.
![[ciclo_combinato_cogenerativo_2lp_layout-v2.png]]![[Pasted image 20261020235607.png]]

Il calore scambiato in questo impianto viene calcolato:
$$
\dot{Q}_{scambiato} = \dot{m_{a}}\cdot c_{p} \cdot(T_{4'}-T_{5})
$$
Invece le potenze sono:
$$
P_{c} = \dot{m_{c}}\cdot K_{i} = \frac{\dot{m_{a}}\cdot c_{p} \cdot (T_{3}-T_{4'})}{\eta_{cc}} \\
P_{e} = P_{g} + P_{v} \\
P_{t} = \dot{m}_{UT} \cdot (h_{d} - h_{e})
$$
# Gruppo cogenerativo con motore a combustione interna
![[gruppo_cogenerativo_mci_layout.png]]
A differenza di una turbina a gas (dove il calore recuperabile si trova concentrato esclusivamente nei fumi ad alta temperatura), un motore a combustione interna (solitamente un 4 tempi ad accensione comandata a gas naturale o ciclo Diesel) rende disponibile il calore su **due livelli termici distinti**:
1. **Alta Temperatura (AT) — Fumi di Scarico**:
    - I fumi fuoriescono dai cilindri a $400\text{--}500\text{ °C}$.
    - Attraversano uno **Scambiatore Fumi** (a fascio tubiero) per riscaldare il vettore termico (acqua o vapore a bassa pressione) fino a $90\text{--}110\text{ °C}$, prima di essere espulsi dal camino a $110\text{--}120\text{ °C}$.
2. **Media / Bassa Temperatura (BT/MT) — Circuito di Raffreddamento e Olio**:
    - Il calore generato dalla combustione all'interno delle pareti dei cilindri viene asportato dall'**Acqua di Camicia (*jacket water*)**  $80\text{--}90\text{ °C}$.
    - A questo si aggiungono il calore sottratto dall'**Olio di Lubrificazione** e la refrigerazione dell'aria di alimentazione (**Intercooler** del turbocompressore).
    - Questo calore viene trasferito all'acqua dell'utenza tramite uno **Scambiatore a Piastre (HT)**.

