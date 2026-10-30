mo# Ciclo HIRN
#ciclo_surriscaldamento
[[003_SistemiAVapore_MN.pdf#page=2|003_SistemiAVapore_MN, pagina 2]]
Utilizza un liquido operatore, di solito l'acqua, ed essendo un ciclo ad ogni cambiamento alla fine torna sempre ai valori di partenza.

![[Pasted image 20251009094214.png]]

L'impianto è costituito da:
-  **[[GENERATORE DI VAPORE]]** a sua volta formato da:
	- **[[GENERATORE DI VAPORE#^1676a5|Economizzatore]]** 
	- **[[GENERATORE DI VAPORE#^2726ef|Vaporizzatore]]**
	- **[[GENERATORE DI VAPORE#^16978c|Surriscaldatore]]**
	Questa macchina converte l'energia chimica del combustibile in energia termica.
- **Turbina a vapore**: Macchina motrice, che utilizzando il vapore surriscaldato ad alta pressione ed entalpia si espande fino alla pressione di condensazione, durante l'espansione l'energia del vapore viene convertita in **lavoro meccanico**
- **Condensatore**: Scambiatore di calore in cui il vapore uscente dalla trubina viene condensato completamente cedendo calore al fuido refrigerante.
- **Pompa di estrazione/alimento**: La pompa di **alimento** **aspira acqua** dal serbatoio e la invia al generatore di vapore, invece quella di **estrazione** estrae la condensa raccolta sul fondo del condensatore e la invia al serbatoio. 
- **Alternatore**: Converte l'energia meccanica prodotta dalla turbina in energia elettrica.
- **Serbatoio**: Serbatoio a pressione atmosferica.

Per ogni trasformazione il fluido operatore in questo ciclo subisce 4 trasformazioni,:
- **Pressurizzazione**
	Avviene nel tratto **o - o"** 
- **Riscaldamento**
	Avviene nel tratto **o" - a**
	$q_{oa} = q_{1} = h_{a}-h_{o}$
- **Espansione**
	Avviene nel tratto **a - b**
	$l_{ab} = h_{a} - h_{b} = l_{is}$
- **Condensazione**
	Avviene nel tratto **b - o**
	$q_{bo} = q_{2} = h_{b} - h_{o}$
![[Pasted image 20251102232758.png]]
Queste trasformazione avvengono nel momento che il fluido attraverso le corrispettive macchine.
[[003_SistemiAVapore_MN.pdf#page=8|003_SistemiAVapore_MN, pagina 8]]

Il rendimento termodinamico di questo impianto viene definito da:
$$
\eta_{th} = \frac{l_{is}}{q_{1}} = \frac{h_{a}-h_{b}}{h_{a}-h_{o}}
$$
La potenza termica fornita invece è:
$$
\dot{Q_{1}} = \dot{m_{v}}\cdot q_{1} = \dot{m_{v}}\cdot (h_{a}-h_{o})
$$
La potenza utila fornita dalla turbina è:
$$
P_{ut} = \dot{m_{v}} \cdot (h_{a}-h_{b'})\eta_{mt} = \dot{m_{v}} \cdot (h_{a}-h_{b'})\eta_{mt}\eta_{it}
$$
dove i rendimenti aggiunti sono rispettivamente il rendimento **interno della turbina** e il rendimento **meccanico della turbina**.

La potenza elettrica fornita dall'alternatore è:
$$
P_{e} = P_{ut}\cdot \eta_{aux}\cdot \eta_{alt} = \dot{m_{v}}\cdot(h_{a}-h_{b'})\eta_{it}\eta_{mt}\eta_{aux}\eta_{alt}
$$
I rendimenti aggiunti nell'operazione centrale sono rispettivamente il rendimento dei  **componenti ausiliari** come pompe e altri, invece l'altro rendimento indica quello dell'**alternatore**.

Il rendimento totale dell'impianto viene definito da:
$$
\eta_{imp} = \frac{P_{e}}{\dot{m_{c}}\cdot k_{i}} = \frac{\dot{m_{v}}\cdot(h_{a}-h_{b'})\eta_{it}\eta_{mt}\eta_{aux}\eta_{alt}}{\dot{m_{v}}\cdot (h_{a}-h_{o}) / \eta_{g}} = \eta_{it}\eta_{mt}\eta_{aux}\eta_{alt}\eta_{th}\eta_{g}
$$
## Ottimazzazione del rendimento termodinamico
1. **Influenza della pressione a condensazione**
	Più la differenza di temperatura fra le trasformazioni **isoterme**, più **migliora** il rendimento ad una certe pressione di condensazione $p_k$ , come succede nel [[Termodinamica di base#Teorema di Carnot|Ciclo di trasformazione di carnot]].
	
	Se $\frac{\Delta L}{\Delta q} > \frac{l}{q1}$ allora si ha un guadagno sul rendimento del sistema.
 	[[003_SistemiAVapore_MN.pdf#page=15|003_SistemiAVapore_MN, page 15]]

2. **Influenza della pressione di vaporizzazione**
	La variazione di pressione di vaporizzazione causa un aumento del rendimento se nel campo delle basse pressioni, noi **aumentiamo** la **pressione di vaporizzazione** determina un **aumento del rendimento termodinamico**.
	Però più ci si avvicina alla cuspide della campa, ci sia avvicina alla **pressione critica**, questo comporta una **diminuzione del rendimento termodinamico** all'aumentare della pressione di vaporizzazione.
	[[003_SistemiAVapore_MN.pdf#page=17|003_SistemiAVapore_MN, page 17]]

3. **Influenza del grado di surriscaldamento**
	Il **grado di surriscaldamento** è quanto scaldo il fluido una volta raggiunto lo stato gassoso.
	Si divide il ciclo termodinamico in 2, il primo comprende l'area della campana, invece la seconda comprende l'area di surriscaldamento del fluido.
	![[Pasted image 20251009103411.png]]
	Utilizzando la [[SISTEMI A VAPORE#Temperatura di compenso|temperatura di compenso]] si può ricavare il rendimento complessivo del ciclo totale.
	[[003_SistemiAVapore_MN.pdf#page=19|003_SistemiAVapore_MN, page 19]]
# Temperatura di compenso
Dato un ciclo termodinamico generico, si può comparare con un ciclo termodinamico di Carnot, evente stesso **rendimento** e **lavoro**, con ==**temperatura di compenso**== uguale alla  **temperatura superiore** del ciclo termodinamico di Carnot. 
![[Pasted image 20251103000122.png]]
[[003_SistemiAVapore_MN.pdf#page=18|003_SistemiAVapore_MN, page 18]]

# Ciclo a Risurriscaldamento
![[Pasted image 20251009105813.png]]
In questo tipo di ciclo il fluido una volta uscito dalla caldaia, esce ad una certa pressione di vaporizzazione $P_v$ passando attraverso una turbina di **alta pressione(AP)**, uscendo e passando di nuovo nella caldaia per risurriscaldarsi e attraversare la turbina di **bassa pressione(BP)**.

Per questo tipo di ciclo se si vuole utilizzare il terzo tipo di [[SISTEMI A VAPORE#Ottimazzazione del rendimento termodinamico|Ottimizzazione del rendimento termodinamico]] , le aree questa volta saranno, la prima il ciclo di HIRN, invece la seconda la parte di risurriscaldamento.

Il rendimento in questo ciclo aumenta rispetto a quello di HIRN solo quando $P_k< P_{rs}^* < P_v$    
[[003_SistemiAVapore_MN.pdf#page=20|003_SistemiAVapore_MN, pagina 20]]

# CICLO RIGENERATIVO
![[Pasted image 20251009121138.png]]
Si Divide il classico ciclo di HIRN in tre cicli:
![[Pasted image 20251009121247.png]]
Con temperature di compenso $T_{mII} = T_v$ e $T_m \le T_{mIII} \le T_q$ 
[[003_SistemiAVapore_MN.pdf#page=21|003_SistemiAVapore_MN, pagina 21]]

Il ciclo termodinamico avviene:
![[Pasted image 20251009123109.png]]
Quando il fluido si espande e arriva al punto 1, il fluido inizia a spillarsi, così da poter essere rigenerato.

# CICLI ORC
Il ciclo HIRN-RANKINE risulta essere **svantaggioso** con l'utilizzo del vapore per applicazioni a bassa temperatura in quanto:
- Richiedono tubi e scambiatori di elevato volume, e quindi apparecchiature costose, che risultano essere antieconomiche per i valori di efficienza che si riescono a raggiungere
- Bassa densità del vapore alla fine dell’espansione: richiede macchine con pale molto lunghe negli stadi di bassa pressione
- Necessità di surriscaldare o di proteggere le pale delle turbine, a causa dell’umidità del vapore a fine espansione. Entrambi gli accorgimenti fanno lievitare i costi d’impianto.
- Pressione di condensazione minore della pressione ambiente alle normali temperature di condensazione, con infiltrazioni d’aria e necessità di degassare l’impianto. 

 In questo tipo di cicli si utilizzano:
 - Fluidi bassobollenti, fluidi con temperatura di ebollizione minore a quella dell'acqua
 - Il ciclo base è quello Rankine
 - Proprietà che permettono di mantenere i costi dell'impianto anche in caso di temperature basse.

Vengono utilizzati **fluidi organici**, che hanno proprietà diverse da quelle dell'acqua:
- Date le basse temperature, le basse potenze in gioco e i bassi rendimenti, il ciclo deve essere il più semplice possibile.
- Assenza di rigenerazione con spillamenti di vapore
- No surriscaldamento
- Assenza di degassatore per l'estrazione degli incondensabili

L'architettura dell'impianto varia anche in base al tipo di fluido:
- **ISOENTROPICO**
	Pendenza della curva limite superiore verticale
- **BAGNATO**
	Pendenza della curva limite superiore negativa (come l’acqua): espandendo isoentropicamente si entra all’interno della campana, con formazione di condensato
- **SECCO**
	Pendenza della curva limite superiore positiva: espandendo isoentropicamente si arriva nella zona dei vapori surriscaldati
![[Pasted image 20261014235036.png]]

Le proprietà dei fluidi possono modificare il comportamento durante le trasformazioni all'interno di un sistema:
- **fluidi bagnati**(come l'acqua)
	Sviluppano condensa negli ultimi stadi di espansione. I fluidi bagnati solitamente hanno una temperatura critica abbastanza modesta, per queste si deve lavorare a pressioni elevate.
	Per aumentare il rendimento dell'impianto si può surriscaldare, però questo fa lievitare i costi dell'impianto.
- **fluidi asciutti e isoentropici**
	Al termine dell’espansione si rientra nella zona dei vapori surriscaldati: non è necessario surriscaldare.
	È possibile aumentare il rendimento tramite la rigenerazione utilizzando il calore residuo nel vapore.
	La presenza del rigeneratore comporta un **costo aggiuntivo**, ma **aumenta l'efficienza** dell'impianto.
	Però non sempre porta benefici poiché aumenta la temperatura d'uscita del fluido e questo potrebbe causare una riduzione del rendimento dell'impianto, per questo bisogna prestare particolare **attenzione** alla sua **progettazione**.
	Infatti per **impianti piccoli** il rigeneratore **non viene utilizzato**.

L'influenza di questi fluidi sul ciclo:
- Per i **fluidi bagnati** il surriscaldamento **aumenta** l'efficienza del ciclo.
- Per i **fluidi asciutti** il **surriscaldamento diminuisce** il rendimento del ciclo, se questo **non è dotato di rigeneratore**.
- Per i fluidi asciutti il rendimento aumenta con il surriscaldamento solo se si utilizza il rigeneratore, in quanto il surriscaldamento incrementa la temperatura di uscita dalla turbina e incrementa il calore sensibile scambiabile nel rigeneratore. Si riduce in questo modo la fase di economizzazione.
- Diversamente dall’acqua i fluidi organici soffrono il problema della **stabilità chimica** ad alta temperatura.
- Altra problematica è la ==stabilità dei fluidi a contato con le pareti solide dei componenti dell’impianto. ==
 - Molti dei fluidi di lavoro utilizzati negli ORC hanno un certo grado di **tossicità** e di **infiammabilità**. 
 - La tossicità e l’infiammabilità possono diventare problematiche in caso di fughe di fluido. Per quanto riguarda l’infiammabilità (tipica dei fluidi appartenenti alla classe degli idrocarburi) è necessario utilizzare apparecchiature a norma ATEX. Per quanto riguarda la tossicità̀ è necessario mantenere una buona ventilazione dei locali. 
 - I fluidi organici possono avere un impatto sull’ozono negli strati alti dell’atmosfera (ODP, Ozone Depletion Potential, ne misura la capacità di distruggere l’ozono) 
 - I ==fluidi organici possono contribuire all’effetto serra== (l’indice è il GWP, Global Warming Potential, calcolato relativamente all’effetto della CO2)