# Ciclo HIRN
#ciclo_surriscaldamento
[[003_SistemiAVapore_MN.pdf#page=2|003_SistemiAVapore_MN, pagina 2]]
Utilizza un liquido operatore, di solito l'acqua, ed essendo un ciclo ad ogni cambiamento alla fine torna sempre ai valori di partenza.

![[Pasted image 20251009094214.png]]

Per ogni trasformazione il fluido operatore in questo ciclo ottiene 4 trasformazioni,:
- **Pressurizzazione**
	Avviene nel tratto **o - o"** 

- **Riscaldamento**
	Avviene nel tratto **o" - a**

- **Espansione**
	Avviene nel tratto **a - b**

- **Condensazione**
	Avviene nel tratto **b - o**
![[Pasted image 20251102232758.png]]
Queste trasformazione avvengono nel momento che il fluido attraverso le corrispetticve macchine.
[[003_SistemiAVapore_MN.pdf#page=8|003_SistemiAVapore_MN, pagina 8]]


## Ottimazzazione del rendimento termodinamico
1. **Influenza della pressione a condensazione**
	Più la differenza di temperatura fra le trasformazioni **isoterme**, più **migliora** il rendimento ad una certe pressione di condensazione $p_k$ , come succede nel [[Termodinamica di base#Teorema di Carnot|Ciclo di trasformazione di carnot]] .
	Se $\frac{\Delta L}{\Delta q} > \frac{l}{q1}$ allora si ha un guadagno sul rednimento del sistema.
 	[[003_SistemiAVapore_MN.pdf#page=15|003_SistemiAVapore_MN, page 15]]

2. **Influenza della pressione di vaporizzazione**
	La variazione di pressione di vaporizzazione causa un aumento del rendimento più la variazione **avviene lontano** dalla cuspide della curva termodinamica.
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
In questo tipo di ciclo il fluido una volta uscito dalla caldaia, esce ad una certa pressione di vaporizzazzione $P_v$ passando attraverso una turbina di **alta pressione(AP)**, uscendo e passando di nuovo nella caldaia per risurriscaldarsi e attraversare la trurbina di **bassa pressione(BP)**.

Per questo tipo di ciclo se si vuole utilizzare il terzo tipo di [[SISTEMI A VAPORE#Ottimazzazione del rendimento termodinamico|Ottimazzazione del rendimento termodinamico]] , le aree questa volta saranno, la prima il ciclo di HIRN, invece la seconda la parte di risurriscaldamento.

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


