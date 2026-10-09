# Gruppo turbo-gas
#turbo_gas
Sono motori termici che trasformano l'energia chimica del combustibile, in energia meccanica.

Sono anche produttori di inquinanti.
[[004_SistemiAGas_MN.pdf#page=3|004_SistemiAGas_MN, pagina 3]]

# Turbo-gas semplice
![[Pasted image 20251022103036.png]]
- **C**
	**Compressore** dinamico assiale, aspira l'aria comprimendola portandola alla **pressione di esercizio**, $\frac{p_{1}}{p_{2}}$ è detto **rapporto di compressione**$\beta$.
- **CC**
	**Camera di combustione**, l'aria compressa subisce un riscaldamento portando un **conseguente aumento di volume**. I prodotti della combustione diventano parte integrante del fluido operatore. 
- **TG**
	**Turbina a Gas**, il fluido operatore subisce un'espansione cambiando il proprio stato fisico, tra i punti 3-4, nel punto 4 i gas vengono scaricati in atmosfera.
- **M**
	**Motore di lancio**, serve per avviare la turbina a gas grazie al trascinamento meccanico, il quale farà girare la turbina fino a quando il compressore non raggiunge la portata d'aria necessaria per permettere alla CC di innescare la combustione, una volta che raggiunge una certa velocità il motore di lancio viene disinnestato ed escluso dal ciclo, e la turbina prosegue la salita in frequenza/potenza verso il regime nominale.
- **A**
	**Alternatore**, converte l'energia meccanica in energia elettrica.

[[004_SistemiAGas_MN.pdf#page=4|004_SistemiAGas_MN, pagina 4]]

# Ciclo Brayton
![[Pasted image 20251022103157.png]]
==**IPOTESI:**==
1. Il fluido percorre un ciclo chiuso
2. Fluido operatore composto da solo aria
3. Le Trasformazioni avvengono in modo estremamente lento
4. Si trascurano le perdite di carico
5. La cessione di calore all'atmosfera avviene a pressione costante
6. La compressione e l'espansione del fluido operatore sono isoentropiche
[[004_SistemiAGas_MN.pdf#page=5|004_SistemiAGas_MN, pagina 5]]

- **Compressione**
	Avviene nel tratto **1 - 2'** 
	$l_{isC} = h_{2}-h_{1}$
	$\eta_{iC} = \frac{l_{is}}{l_{reale}} = \frac{h_{2}-h_{1}}{h_{2'}-h_{1}} \to l_{realeC} = \frac{l_{is}}{\eta_{i}}$
- **Combustione**
	Avviene nel tratto **2' - 3**
	$q_{1} = h_{2'}-h_{3}$
- **Espansione**
	Avviene nel tratto **3 - 4'**
	$l_{isT} = h_{3}-h_{4}$
	$\eta_{iT} = \frac{l_{realeT}}{l_{isT}} = \frac{h_{3}-h_{4'}}{h_{3}-h_{4}} \to l_{realeT} = \eta_{i}l_{is}$
- **Raffreddamento**
	Avviene nel tratto **4' - 1**
	$q_{2} = h_{4'} - h_{1}$

**Lavore reale all'albero della turbina**:
$$
l_{is} = l_{is,T} - l_{is,C} \geq 0;\space l_{reale}= l_{reale,T}-l_{reale,C} \geq 0
$$
Questa viene detta anche **condizione di autosufficienza**.
$l_{reale} = c_{p}(T_{3}-T_{4'})-c_{p}(T_{2'}-t_{3}) = c_{p}(T_{3}-T_{4})\eta_{i,T} -\frac{c_{p}(T_{2}-T_{1})}{\eta_{i,c}} \geq 0$

**RENDIMENTO TERMODINAMICO REALE:**
$$
\eta_{th,r} = \frac{l_{reale}}{q_{1}} = \frac{c_{p}(T_{3}-T_{4})\eta_{i,T} -\frac{c_{p}(T_{2}-T_{1})}{\eta_{i,c}}}{c_{p(T_{3}-T_{2'})}}
$$
**CALORE FORNITO:**
$$
q_{1} = h_{3}-h_{2'} = c_{p}\left[ (T_{3}-T_{1}) - \frac{1}{\eta_{i,C}}(T_{2}-T_{1})\right]
$$


![[ciclo_brayton_pv_ts.png|660]]
## LAVORO UTILE
Il **Lavoro utile** e il lavoro in eccesso rispetto alla condizione di autosufficienza.
$$\begin{aligned}
L_{u} = L_{T} -L_{C} = c_{p}(T_{3}-T_{4})\eta_{i,T}-\frac{c_{p}(T_{2}-T_{1})}{\eta_{i,C}} \\
\beta = \frac{T_{2}}{T_{1}} \to rapporto \space di\space compressione \\
\theta = \frac{T_{3}}{T_{1}} \to rapporto \space di \space temperatuture \space estreme \space del \space ciclo \\
L_{U}^* = \frac{L_{U}}{c_{p}T_{1}} = \left( \frac{T_{3}}{T_{1}} - \frac{T_{4}}{T_{1}} \right)\eta_{i,T}-\frac{1}{\eta_{i,C}}\left( \frac{T_{2}}{T_{1}}-1 \right)\\
L_{U}^* = \left( \theta- \frac{\theta}{\beta} \right) \eta_{iT} - \frac{1}{\eta_{iC}}(\beta - 1) = (\beta -1 )\left( \frac{\theta}{\beta} \eta_{iT} - \frac{1}{\eta_{iC}} \right)
\end{aligned}
$$

[[004_SistemiAGas_MN.pdf#page=15|004_SistemiAGas_MN, pagina 15]]

**MASSIMO LAVORO UTILE**
![[Pasted image 20251023101308.png]]

-  **TRATTO CRESCENTE**$\frac{dL_{U}*}{d\beta} > 0$
	Un aumento di compressione è vantaggioso per la potenza prodotta: l'incremento di lavoro estratto in turbina supera il lavoro aggiuntivo assorbito dal compressore, facendo **crescere il lavoro netto**.
- **PUNTO DI MASSIMO** $\frac{dL_{U}*}{d\beta} = 0$
	**Condizione di ottimo (stazionarietà)**, il guadagno marginale in turbina e il costo marginale al compressore si bilanciano perfettamente. Il ciclo eroga la **massima quantità di lavoro utile per unità di massa di fluido**.
- **TRATTO DECRESCENTE**$\frac{dL_{U}*}{d\beta} < 0$
	Continuare ad aumentare $\beta$ riduce la potenza disponibile: il lavoro parassita assorbito dal compressore cresce più velocemente rispetto a quanto la turbina riesca ad erogare, facendo **diminuire il lavoro netto**.


**MASSIMO RENDIMENTO**
![[Pasted image 20251023101418.png]]

### GRUPPO TURBO-GAS CON RECUPERO DI CALORE
Si utilizzano i fumi caldi uscenti dalla turbina, che verrebbero scartati, per **PRERISCALDARE** il fluido operatore prima che entri in **CAMERA DI COMBUSTIONE**.

![[ciclo_brayton_recupero_ts-v2.png|700]]
[[004_SistemiAGas_MN.pdf#page=20|004_SistemiAGas_MN, pagina 20]]
Infatti il rendimento diventa:
$$\eta_{rig} = \frac{L_{netto}}{c_p (T_3 - T_x)} > \eta_{semplice} = \frac{L_{netto}}{c_p (T_3 - T_2)}$$

### REGOLAZIONE DEI GRUPPI TURBOGAS
Si può regolare la potenza elettrica in uscita da una turbna grazie a vari paramentri come, densità e velocità del fluido in ingresso al compressore, e alla sezione d'ingresso del compressore.
[[004_SistemiAGas_MN.pdf#page=22|004_SistemiAGas_MN, pagina 22]]

Esistono **3 metodi di regolazione**:
1. **Ciclo termodinamico**
	![[Pasted image 20251023110359.png]]
2. Variare lo stato fisico del fluido in ingresso del compressione
3. **Velocità di rotazione**
	![[Pasted image 20251023110437.png]]

# TURBOGAS SU 2 ASSI
#2assi
![[Pasted image 20261009235436.png]]

Un ciclo a 2 assi in questo caso, la turbina viene separata in 2:
- **PRIMO ASSE (ASSE GENERATORE)**
	Il primo asse comprende Camera di combustione, Compressore, e **turbina ad alta pressione**.
	In questo ramo la turbina tramite l'espansione del gas fino ad una pressione intermedia, produce il lavoro **strettamente necessario** per trascinare il compressore.
	Quindi lavora in condizione di autosufficienza.
	$T_{3}-T_{in}\eta_{mTap} =\frac{T_{2}-T_{1}}{\eta_{m,C}}$ ^65da47
- **SECONDO ASSE (ASSE DI POTENZA)**
	Il secondo asse comprende la **turbin a bassa pressione** e l'alternatore, i gas che sono parzialmente espansi entrano nella turbina ad bassa pressione per espandersi fino a pressione ambientale, in questo caso il lavoro estratto dalla turbina costituirà il **lavoro erogato deall'impianto**.

Il suo diagramma sarà:
- **Tratto 1 → 2 (Compressione)**: L'aria passa da $p_1$ a $p_2$ assorbendo il lavoro $L_c = c_p(T_2 - T_1)$.
- **Tratto 2 → 3 (Combustione)**: Adduzione di calore a pressione costante $p_2$ fino alla temperatura massima $T_3 = TIT$.
- **Tratto 3 → 4a (Espansione Turbina HP)**: Espansione reale dalla pressione massima $p_2$ alla pressione intermedia $p_{int}$. Il salto entalpico estratto uguaglia il lavoro di compressione: $$c_p (T_3 - T_{4a}) = c_p (T_2 - T_1) \implies L_{t,HP} = L_c$$
- **Tratto 4a → 4 (Espansione Turbina LP)**: Espansione reale dalla pressione intermedia $p_{int}$ alla pressione di scarico $p_1$. Il salto entalpico fornisce il lavoro utile: $$L_{netto} = c_p (T_{4a} - T_4) = L_{t,LP}$$
- **Tratto 4 → 1 (Scarico Fumi)**: Raffreddamento/espulsione dei fumi esausti a pressione atmosferica $p_1$.

In questo caso le turbine sono **disaccoppiate**, questo significa che l'asse di potenza può rotare a velocità costante o variabile al carico meccanico, invece l'asse generatore varia la sua velocità per modulare la portata d'aria aspirata.

## 2 ASSI CON POST-COMBUSTIONE
![[Pasted image 20261010001552.png]]

Nei cicli con post-combustione (o _ricombustione_), l'espansione e l'apporto termico vengono frazionati per aumentare il lavoro specifico erogato dall'impianto:

1. **Compressore (C)**: Aspira aria dall'ambiente (stato 1) e la comprime fino alla pressione massima $p_2$ (stato 2).
2. **Camera di Combustione Principale (CC1)**: Riceve l'aria compressa, inietta il primo apporto di combustibile ($Q_{in1}$) e porta i fumi alla prima temperatura massima $TIT_1$ (stato 3).
3. **Turbina ad Alta Pressione (T1 / HP)**: I fumi caldi si espandono parzialmente da $p_2$ a una **pressione intermedia (**$p_{int}$**)** (stato 4a).
4. **Camera di Ricombustione / Post-Combustione (CC2)**: I fumi parzialmente espansi (che contengono ancora un'elevata percentuale di ossigeno incombusto) entrano in un secondo combustore, dove viene iniettato ulteriore combustibile ($Q_{in2}$) per riportare i fumi alla temperatura massima $TIT_2 \approx TIT_1$ (stato 3b).
5. **Turbina a Bassa Pressione (T2 / LP)**: I fumi riscaldati si espandono una seconda volta dalla pressione intermedia $p_{int}$ alla pressione atmosferica $p_1$ (stato 4), azionando il carico/alternatore.

Il diagramma termodinamico sarà:
- **Tratto 1 → 2 (Compressione Reale)**: Compressione dall'isobara $p_1$ all'isobara di alta pressione $p_2$.
- **Tratto 2 → 3 (Prima Combustione)**: Riscaldamento isobaro a pressione $p_2$ fino al punto 3 ($TIT_1 = 1400\text{ K}$).
- **Tratto 3 → 4a (Prima Espansione HP)**: I fumi si espandono in turbina HP fino all'isobara intermedia $p_{int}$ (punto 4a).
- **Tratto 4a → 3b (Post-Combustione)**: Riscaldamento isobaro a **pressione intermedia** $p_{int}$ che riporta la temperatura del fluido al valore di picco ($TIT_2 = 1400\text{ K}$, punto 3b).
- **Tratto 3b → 4 (Seconda Espansione LP)**: Espansione finale in turbina LP dall'isobara $p_{int}$ alla pressione atmosferica $p_1$ (punto 4).
- **Tratto 4 → 1 (Scarico Fumi)**: Raffreddamento/espulsione dei fumi a pressione atmosferica.

Gli assi di questo tipo di ciclo lavorano come quello del **[[#TURBOGAS SU 2 ASS|Ciclo a 2 assi]]**.


