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
	