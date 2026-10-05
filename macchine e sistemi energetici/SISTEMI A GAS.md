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


### Condizione di lavoro Utile e massimo rendimento
Il **Lavoro utile** e il lavoro in eccesso rispetto alla condizione di autosufficienza.
[[004_SistemiAGas_MN.pdf#page=15|004_SistemiAGas_MN, pagina 15]]

**MASSIMO LAVORO UTILE**
![[Pasted image 20251023101308.png]]

**MASSIMO RENDIMENTO**
![[Pasted image 20251023101418.png]]

### GRUPPO TURBO-GAS CON RECUPERO DI CALORE
Si utilizzano i fumi caldi uscenti dalla turbina, che verrebbero scartati, per **PRERISCALDARE** il fluido operatore prima che entri in **CAMERA DI COMBUSTIONE**.
[[004_SistemiAGas_MN.pdf#page=20|004_SistemiAGas_MN, pagina 20]]

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
![[Pasted image 20251023113641.png]]
![[Pasted image 20251023113717.png]]

