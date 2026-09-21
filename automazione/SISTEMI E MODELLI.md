**Sistema**: è un modello di un oggetto che interagisce con il modno circostante tramite 2 variabili nel tempo.
![[Pasted image 20260226111014.png]]

- **Variabili d'ingresso**: azioni compiute da **==agenti esterni==** che influiscono sul comportamento del sistema
- **Variabili di uscita**: **==grandezze del sistema==** in esame che sono di ==**interesse**==.
- **Parametri**(di solito costanti): descrivono lastruttura del sistema

## SISTEMA STATICO
Un **sistema statico** rappresenta un oggetto in cui l'**uscita** in un certo istante **dipende solo dal valore dell'ingresso nello stesso istante**.
Questo può essere descritto da un'==equazione algebrica==.
## SISTEMA DINAMICO
Un **sistema dinamico** rapprestente un oggetta dove l'uscita in un certo istante dipende **valore di ingresso** allo stesso istante, ma anche da altre **variabili** che **descrivono la situazione interna del sistema**(**==Variabili di stato==**).

**Variabili di stato**:  Variabili che descrivono la “situazione” interna del sistema e necessarie per determinarne l’uscita


### RAPPRESENTAZIONE ISU
Per rappresentare uesto tipo di sistema si utilizza la **rappresentazione Ingresso-Stato-Uscita**(ISU), in questa rappresentazione si devono utilizzare **2 equeazioni**:
- **Equazione delle stato**: Rappresenta l'**evoluzione dello stato in funzione dello stato stesso**, cioè rappresenta la ==situazione interna del sistema in funzione dell'ingresso e del tempo==.
![[Pasted image 20260226120724.png]]
questa funzione può essere rappresentata come $\frac{dx}{dt} = f(x(t),u(t),t)$  

- **Equazione di uscita**: Rappresenta l'uscita in funzione dello stato, dell'ingresso e del tempo. 
![[Pasted image 20260226121305.png]]
![[Pasted image 20260226121325.png]]

In generale in un sistema sono presenti **più variabili** di ingresso e di uscita, per questo ingresso e uscita sono rappresentate da vettori così parlando di **vettore di ingresso/uscita**, questo vale anche per le variabili di stato così avendo anche un **vetore di stato**, il numero si variabili di stato viene chiamato **ordine del sistema**.

Oltre alla rappresentazione ISU si utilizza insieme alla rappresentazione **Ingresso-Uscita**(IU), questa viene rappresentata con un **equazione di ingresso-uscita**, è un legame tra ingresso e uscite tra le porprie derivate(cioè l'ordine della derivata dipende dal numero di ingresso/uscite della funzione ingresso/uscita).
![[Pasted image 20260226123300.png]]
L'ordine del sistema viene ricavato dal **numero di variabili di y** o  dal **numero di variabili di stato**
### RAPPRESENTAZIONE IU
La soluzione dell'equazione ==rappresenta l'evoluzione dell'uscita in funzione dell'ingresso==, cioè un legame diretto tra l'ingresso e l'uscita.
![[Pasted image 20260226123537.png]]
![[Pasted image 20260304102341.png]]

## DISTINZIONE DEI SISTEMI
- Statici: modello matematico dei sistemi static, dato da equazioni algebriche
- **Dinamici**: modello dei sistemi dinamici (a parametri concentrati), dati da ==equazioni differenziali==

- **Manovariabili(SISO)**: sistemi con una varibili di entrata e di uscita
- Multivariabili(MIMO): sistemi con più di una variabile per entrate e uscite

- **Parametri concentrati**:equazioni differenziali ordinarie
- Distribuiti: equazioni alle derivate parziali

- **Invarianti**: le loro caratteristiche sono costanti nel tempo
- Tempo varianti:le loro caratteristiche variano nel tempo

- **Lineari**: le variabili entrano linearmente
- Non lineari: le variabili non entrano linearmente

Oltre queste distinzioni, un sistema si può dintinguere anche per la sua **causalità**, cioè quando ==ingresso e uscita dipendono dallo stesso istante di tempo o a qualli precedenti==.
Un modello **non causale** si dice **anticipativo**, però questo tipo di sistema non può essere rappresentato fisicamento, poiché è **impossibile** che un sistema reagisca **prima che di una sollecitazione esterna**.

## RISPOSTA DI UN SISTEMA
La risposta $y(t)$ di un sistema diinamico, per $t \ge 0$ dipenda da:
- **Le condizioni iniziali**, cioè dallo **stato iniziale del sistema** $x(0)$
- **Dall'inigresso** $u(\tau)$, applicato nelli'intervallo $[0,\tau]$ 

La risposta di un sistema può essere:
- **Libera**: La risposta viene data da uno ==stato iniziale **non nulo**, ma con un ingresso **nullo**== 
- **Forzata**: La risposta del sistema viene data ==da uno **stato iniziale nullo(in quiete**), ma sollecitato da un ingresso **non nullo**.==
- **Completa**: La risposta del sistema a partire da uno **stato iniziale non nullo** e soggetto a un **ingresso non nullo**

# SISTEMI MECCANICI
I sistemi  meccanici in un **moto transitorio** si possono considerare costituiti da:

| **MASSA** in cui si concentrano le forze d’inerzia                   | ![[Pasted image 20260311115316.png]] | ![[Pasted image 20260311115329.png]] |
| -------------------------------------------------------------------- | ------------------------------------ | ------------------------------------ |
| **MOLLA** in cui si concentrano le forze di richiamo elastico        | ![[Pasted image 20260311115356.png]] | ![[Pasted image 20260311115407.png]] |
| **AMMORTIZZATORE** in cui si concentrano le forze di attrito viscoso | ![[Pasted image 20260311115435.png]] | ![[Pasted image 20260311115449.png]] |

## MASSA
Un sistema puù essere modellato come una massa sosspitna da una forza motrice su un piano
L'**ingresso** è **la forza motrice**, invece l'**uscita** è **la velocità**
Una possibile **variabile di stato è la velocità**, visto che è legata all’accumulo di energia cinetica.

**POSSIBILE RAPPRESENTAZIONE ISU**:
![[Pasted image 20260311115855.png]]
Che viene ricavata dalla equazione di Newton:
![[Pasted image 20260311122024.png]]


==**Z COME VARIABILE DI STATO**==
[[AuIn02.2-Sistemi e Modelli.pdf#page=28|AuIn02.2-Sistemi e Modelli, pagina 28]]

Se invece è presente l'**attrito viscoso**:
L'equazione fondamentale diventa:
![[Pasted image 20260311122057.png]]

## CONTROLLO DI UNO SPINTORE
 Il sistema può essere modellato come un **sistema massa-molla- smorzatore** sospinto da una forza motrice. Lo ==smorzatore descrive l’attrito viscoso del piano== e ==la molla il richiamo elastico nella posizione di riposo==
L’ingresso è la forza motrice. L’uscita è la posizione.
Essendoci **due accumuli di energia**, ci sono **due variabili di stato**. **Velocità e posizione** della massa sono una possibile scelta.

Equazione della legge Newton:
![[Pasted image 20260311124430.png]]

[[AuIn02.2-Sistemi e Modelli.pdf#page=32|AuIn02.2-Sistemi e Modelli, pagina 32]]


# FUNZIONI DI TRASFERIMENTO
Per risolvere le proprietà dell'uscita è sempre necessario risolvere un equazione differenziale.
La composizione di 2 sistemi dinamici, porta ad un'equazione differenziale più complessa.

Per trasformare queste equazioni differenziali, si usa la **trasformata di Laplace**, utilizzando **i numeri complessi e funzioni a variabili complesse**.
Questa trasformata si utilizza per:
-  Risoluzione di equazioni differenziali 
- Funzioni di trasferimento 
- Risposta all’impulso 
- Risposta al gradino 
- Comportamento dinamico dei sistemi lineari

La trasformazione di Laplace **associa in modo biunivoco** a una generica ==funzione del tempo f(t) a valori reali o complessi una funzione F(s)== a valori in genere complessi e definita per valori di s pure complessi.

La **trasformata di Laplace** viene definita come:
![[Pasted image 20260312113554.png]]

L'**antitrasformata di Laplace** viene definita come:
![[Pasted image 20260312113624.png]]

## PROPRIETà DELLA TRASFORMATA
- **CONIUGAZIONE**
- **LINEARITA**
	[[AuIn03.2-Funzioni di trasferimento.pdf#page=12|AuIn03.2-Funzioni di trasferimento, pagina 12]]
- **TRASLAZIONE NEL TEMPO**
- **TRASLAZIONE NEL DOMINIO s**
	[[AuIn03.2-Funzioni di trasferimento.pdf#page=13|AuIn03.2-Funzioni di trasferimento, pagina 13]]
- **DERIVAZIONE**
	[[AuIn03.2-Funzioni di trasferimento.pdf#page=14|AuIn03.2-Funzioni di trasferimento, pagina 14]]
- **INTEGRAZIONE**
- **Teorema del valore finale**
- **Teorema del valore iniziale**
	[[AuIn03.2-Funzioni di trasferimento.pdf#page=15|AuIn03.2-Funzioni di trasferimento, pagina 15]]

La quasi totalità delle trasformate di Laplace di uso più corrente nell'analisi dei sistemi lineari si può dedurre dalla relazione fondamentale
$$
L[t^ne^{at}] = \frac{n!}{(s-a)^{n+1}}
$$
- **n** come numero intero positivo
- **a** come costante reale o complessa


## TIPI DI TRASFORMATE
### IMPULSO
Descrive un fenomeno molto intenso, ma di durata **infinitesima**.
$$
\int_0^t\sigma(\tau)dr = 1,t > 0
$$
Questa trasformata ha come valore **1**
![[Pasted image 20260319103502.png]]
### GRADINO UNITARIO
Descrive uno stimolo costante nel tempo
![[Pasted image 20260319103439.png]]

### RAMPA
Descrive uno stimolo che **cresce linearmente**
[[AuIn03.3-Funzioni di trasferimento.pdf#page=6|AuIn03.3-Funzioni di trasferimento, pagina 6]]


## TRASFORMATA DI LAPLACE MODELLO IU
[[SISTEMI E MODELLI#RAPPRESENTAZIONE IU|RAPPESENTAZIONE IU]] 
La trasformata di laplace per la rappresentazione di IU può essere scritta come:
$$
\Sigma^n_{i=0} a_i \frac{d^iy(t)}{dt^i} = \Sigma_{i=0}^m b_i\frac{d^iu(t)}{dt^i}
$$
Essendo che tutti gli input iniziali di ogni funziona a **t < 0** sono nulle, tutti i termini iniziali di ogni funzione è nullo.
![[Pasted image 20260319105439.png]]
![[Pasted image 20260319105727.png]]


La trasformata di laplace del modello IU corrisponde a:
$$
\Sigma^n_{i=0}a_is^iY(s) = \Sigma^m_{i=0}b_is^iU(s) + \Sigma^n_{i=0}a_i\Sigma^{i-1}_{j=0}s^jy^{i-j-1}0^-
$$

Si possono anche isolare le costanti
![[Pasted image 20260319111832.png]]

Però se il sistema a t = 0, cioè in **quiete** la funzione diventerà:
![[Pasted image 20260319112316.png]]

La trasformata di Laplace dell’uscita si ottiene semplicemente moltiplicando la trasformata di Laplace dell’ingresso per la **funzione di trasferimento**, data da:

![[Pasted image 20260319112406.png]]

m non può essere **maggiore di n** poichè il sistema non sarebbe causale, al massimo il grado dei 2 polinomi potrà essere uguale,perciò il polinomio a numeratore avrà ordine **minore** del polinomio a denominatore.

La **funzione di trasferimento** di un sistema è **una funzione G(s) della variabile s**, moltiplicandola la trasformata di Laplace U(s) della funzione di ingresso si ottiene la trasformata di Laplace dell’uscita Y(s), quando il sistema parte da condizioni di quiete
![[Pasted image 20260319115335.png]]


## TRASRORMATA DI LAPLACE MODELLO ISU
[[SISTEMI E MODELLI#RAPPRESENTAZIONE ISU|RAPPRESENTAZIONE ISU]]
 La funzione di trasferimento può essere calcolata anche a partire dal modello ISU, considerando x(0)=0:
$$
 \begin{aligned}
 \dot{x}(t) = Ax(t) + Bu(t) \\
 y(t) = cx(t) + Du(t) 
 \end{aligned}
$$
Applicando la trasformata di Laplace e considerando il teorema della derivata si ha:
$$
\begin{aligned}
sX(s) = AX(s) + BU(s) \\
Y(s) = XC(s) + DU(s) \\
da \space cui \space si \space arriva \space a:\\
X(s) = (sI-A)^{-1}BU(s) \\
Y(s) = XC(s) + DU(s) \\
\end{aligned}
$$
Dove **I** è la **matrice identità**, e quindi:

$$
\begin{aligned}
Y(s) = C(sI-A)^{-1}BU(s)+DU(s) \\
G(s) = \frac{Y(s)}{U(s)} = C(sI-A)^{-1}B+D 
\end{aligned}
$$
L'ordine del sistema verrà dato dal numero di variabili di stato.

**==LE TRASFORMATE DI LAPLACE DEI MODELLI==**: [[AuIn03.3-Funzioni di trasferimento.pdf#page=19|AuIn03.3-Funzioni di trasferimento, pagina 19]]

La trasformate di laplace è un **modello algebrico** dei sistemi nel **dominio di Laplace**, in questo caso i sistemi nel domino del tempo, vengon tasformati in un sistema nel **dominio complesso**, infatti la trasformata diventerà **il modello del sistema**.


Calcolare l'inversa di unamatrice 2x2:
![[Pasted image 20260325110926.png]]
con $ad - bc \neq 0$ 


Esssendo che i sistemi presi in considerazioni sono sempre di tipo **SISO**, la funzione di trasferimento sarà sempre un **funzione frazionaria** in s.
La funzione di trasferimento sarà uguale sia che la rappresentazione sia fatto in ISU o in UI.


# SCHEMI A BLOCCHI
Un sistema si può rappresentare anche in **modo grafico**, dove ogni funzione viene rappresentata come un **blocco**.
Un sistema viene rappresentato graficamente con un blocco influenzato da un ingresso e che produce un’uscita.
![[Pasted image 20260325122048.png]]

Tramite questa rappresentazione è possibile, rappresentare più sistemi allo stesso tempo formando uno **schema a più blocchi**.
Un sistema a blocchi è formato da:
- **RAMI**: Vengono associati alle variabili di ingresso ed uscita
- **NODI DI SOMMA**: Organi dove avviene la somma di 2 o più variabili di uscita da un blocco. Se non viene specificato **+ o -** su questi nodi, allora tutte le variabili in input saranno **+**. 
- **NODI DI DERIVAZIONE**: Organi che provvedono a distribuire lo stesso ingresso a più blocchi.
- **BLOCCHI**: Organi che rappresentano il legame matematico tra entrate ed uscite.

Un sistema $G(s)$ può esssere rappresentato da 2 sottosistemi $G_{1}(s)\space e\space G_{2}(s)$  ![[Pasted image 20260325123014.png]]

Partendo da uno schema a più blocchi è possibile eseguire una **riduzione dello schema a blocchi** che permette di rappresentare lo schema tramite un'unica funzione di trasferimento.

## TIPI DI CONNESSIONI
Per connettere più blocchi esistono 2 tipi di connessioni.
### SERIE/CASCATA
2 sistemi sono connessi in **serie** se l'**uscita** del primo diventa **l'ingresso** del secondo.![[Pasted image 20260325123603.png]]

È **possibile eseguire una riduzione dello schema** dove $Y_{1}(s) = U_{2}(s)$.
$$
Y(s) = G_{2}(s)U_{2}(s) = G_{2}(s)Y_{1}(s) = G_{2}(s)G_{1}(s)U(s)
$$
L'interconnessione a cascata varrà:
![[Pasted image 20260325124657.png]]

### PARALLELO
Due blocchi sono interconnessi in **parallelo** se **hanno lo stesso ingresso**.
![[Pasted image 20260325124807.png]]

La riduzione a blocchi data da quasta connessione sarà ricavata da:
$$
Y(s) = Y_{1}(s) + Y_{2}(s) = G_{1}(s)U(s) + G_{2}(s)U(s) = U(s)(G_{1}(s)+G_{2}(s))
$$
### RETROAZIONE
Date due funzione G(s), l'uscita della prima funzione sarà uscita della prima, ma anche **input** della seconda, e l'uscita della seconda funzione **Z(s)**, sarà applicata, **tramite differenza**, in un nodo di somma all'entrata U(s), dando così E(s) **input della prima funzione**, $E(s) = U(s)-Z(s)$.
![[Pasted image 20260327103209.png]]

La funzione di trasferimento G(s),che mette in relazione U(s) con Y(s), data dalla rappresentazione a blocchi, sarà:
$$
\begin{flalign*}
&Y(s)=G_{1}(s)E(s)=G_{1}(s)(U(s)-Z(s))=G_{1}(s)(U(s)-G_{2}Y(s))=G_{1}(s)U(s)-G_{1}(s)G_{2}(s)Y(s) \\
&Y(s)+G_{1}(s)G_{2}(s)Y(s) = G_{1}(s)U(s)\\
&Y(s)(1+G_{1}(s)G_{2}(s))=G_{1}(s)U(s)\\
&\frac{Y(s)}{U(s)}=\frac{G_{1}(s)}{1+G_{1}(s)G_{2}(s)}
\end{flalign*}
$$


# ANTITRASFORMATA DI LAPLACE
Permette di tornare nel dominio nel tempo, dopo essere passati nel dominio dei numeri complessi.
La formula per calcolare l'antitrasformata è:
[[AuIn04.1-Antitrasformate e modi.pdf#page=5|AuIn04.1-Antitrasformate e modi, pagina 5]]

Le funzioni di cui faremo questa operazione saranno sempre **rapporti tra polinomi in s**.
Da una funzione razionale fratta:
$$
F(s)=\frac{P(s)}{Q(s)}
$$
Dove il **grado relativo** è la differenza tra il grado del denominatore(n) e il grado del numeratore(m).
L'equazione $\phi(s)$
$$
Q(s)=s^n+a_{n-1}s^{n-1}+\dots+a_{1}s+a_{0} = 0
$$
è detta equazione caratteristica di $F(s)$, dove $p_{1}\dots p_{n}$ sono le radici sono le radice dell'equazione a **denominatore**.
Questa equazione può essere scritta in forma fattorizzata:
$$
\Phi(s)=(s-p_{1})(s-p_{2})\dots(s-p_{n})
$$
Anche il polinomia a **numeratore può essere scritto nella stessa forma**, dove $z_{1},z_{2}\dots z_{m}$ sono le radici del polinomio P(s).
Quindi la funzione può essere scritta come:
$$
F(s)=K \frac{(s-z_{1})(s-z_{2})\dots(s-z_{m})}{(s-p_{1})(s-p_{2})\dots(s-p_{n})}
$$
dove K è detto **guadagno**, ed è un coefficiente di moltiplicazione.

I fattori z sono detti **zeri**.
I fattori p sono detti **poli**
Una funzione razionale è completamente determinata, a meno di un fattore costante K, una volta assegnati i suoi zeri e i suoi poli

Per antitrasformare F(s) può succedere di avere:
- Tutti i **poli semplici**: dove l'indice di molteplicità di una coppia di poli è pari ad 1
	È una funzione strettamente propri(**grado relativo > 0**), si può scomporre in una soma di n termini di $\sum^n_{i=1} \frac{R_{i}}{s-p_{i}}$, dove $R_{i}$ è una costante dal valore noto, chiamato **residuo**, il quale corrisponde ad un polo, il quale può essere reale(sarà reale anche il residuo), la stessa cosa sucederà se il polo sarà un numero complesso.	
- Ci possono essere **poli multipli**: dove l'indice di una coppia di poli è maggiore ad 1

# ANTITRASFORMATA A POLI MULTIPLI
Nel caso in cui ci sia un polo con moltplicità >1.
Da una funzione come:
$$
F(s)=\frac{P(s)}{Q(s)}=\frac{P(s)}{(s-p_{1})(s-p_{2})\dots(s-p_{i})^r\dots(s-p_{n})}
$$
si ottiene
$$
F(s)=\frac{R_{1}}{s-p_{1}}+\frac{R_{2}}{s-p_{2}}+\dots+\frac{R_{l}}{s-p_{l}}+\frac{A_{i,1}}{s-p_{i}}+\frac{A_{i,2}}{(s-p_{i})^2}+\dots+\frac{A_{i,r}}{(s-p_{i})^r}
$$
dove **i primi l termini si riferiscono a n-r poli semplici**, i **restanti r termini** si riferiscono **al polo $P_{i}$ avente molteplicità r**, dive i residui di questi termino sono **tutti diversi tra loro**.
## MODI DI UN SISTEMA
È l'antitrasformaata di ciascun fratto semplice, in cui viene decomposta la funzione di trasferimento.

Come l'ingresso, i modi **condizionano la risposta** del sistema.

Modi di un sistema nel caso di **POLI SEMPLICI**:
$$
\begin{aligned}
R\to se\space p=0 \\
Re^{pt}=Re^{\sigma t} \to \space se\space p \space è \space reale: p=\sigma\\
Re^{\sigma t}\cos(\omega t + \phi) \to se \space p \space è \space complesso: p = \sigma + i \omega
\end{aligned}
$$

Il comportamento dei modi è legato alla posizione dei poli in rapporto all'asse immaginario.
Nel caso dei poli semplici
$$
per \to \infty 
$$
La risposta dei modi sarà:
$$
\begin{aligned}
0 \to \sigma<0\\
limitati \to \sigma=0\\
\infty \to \sigma > 0
\end{aligned}
$$
Descritto anche da:[[AuIn04.3-Antitrasformate e modi.pdf#page=12|AuIn04.3-Antitrasformate e modi, pagina 12]]

Invece per **Poli multipli**:
$$
\begin{aligned}
Rt^h\to se\space p=0, molteplicita = h \\
Rt^he^{pt}=Re^{\sigma t} \to \space se\space p \space è \space reale: p=\sigma,molteplicita = h\\
Rt^he^{\sigma t}\cos(\omega t + \phi) \to se \space p \space è \space complesso: p = \sigma + i \omega,molteplicita = h
\end{aligned}
$$

Deescritto anche da:[[AuIn04.3-Antitrasformate e modi.pdf#page=17|AuIn04.3-Antitrasformate e modi, pagina 17]]

La risposta in questo caso sarà:
$$
per \space t\to \infty
$$
$$
\begin{aligned}
0 \to \sigma <0\\
\infty \to \sigma> 0
\end{aligned}
$$

I modi di un sistema: 
- rimangono **limitati**, se e solo se la funzione di trasferimento
	- non presenta alcun polo a parte reale positiva
	- gli eventuali poli a parte reale nulla sono semplici,
- **divergono** in caso contrario


Un sistema che presenta all'uscita una divergenza, questo sistema avrà un comportamento **instabile**.
[[AuIn04.3-Antitrasformate e modi.pdf#page=21|AuIn04.3-Antitrasformate e modi, pagina 21]]


La posizione dei poli della funzione di trasferimento (i poli del sistema) rispetto all’asse immaginario determina la **STABILITÀ** del sistema, ovvero la capacità del sistema di riportarsi in una configurazione di quiete dopo una perturbazione, di durata limitata, dello stato iniziale.

**La stabilità è una proprietà del sistema**: non dipende né dall’ampiezza della perturbazione, né dal tempo di applicazione.

Dopo una perurbazione dello stato iniziale, un sistema può avere tre comportamenti diversi:
- RISPOSTA LIMITATA
- RISPOSTA DIVERGENTE
- Risposta che **converge** asintoticamente  **a 0**

La stabilità di un sistema è data da queste condizione, ma si può ricavare anche dalla posizione dei poli rispetto all'asse immaginario:
- Risposta **limitata** $\to$ Sistema **stabile**
	Poli con parte reale nulla, **molteplicità = 1**
- Risposta **divergente** $\to$ Sistema **instabile**
	Poli a parte reale positiva o nulla, se nulla **molteplicutà > 1**
- Risposta che **converge a 0**$\to$ Sistema **asintoticamente stabile**
	Poli a **parte reale negativa**

Condizione **necessaria e suffieciente** per la ==stabilità di un sistema==, la sua funzione di trasferimento deve avere solo **poli a parte reale negativa o nulla**,e **quelli a parte reali nulla sia a molteplicità pari a 1**.

Condizione **necessaria e sufficiente** per la ==stabilità **asintotica** di un sistema==, è che **tutti i poli** della sua funzione di trasferimento siano a **parte reale strettamente negativa**.

Esiste anche un'alto tipo di stabilità, **STABILITÀ BIBO**, questa prende in considerazione l'ingresso del sistema.

In questo caso la stabilità, sarà se ad **ogni segnale d'ingresso u(t) limitato** presenta un'**uscita y(t) limitata**.

Un sistema inizialmente in quiete, descritto da funzione di trasferimento G(s) razionale fratta, è stabile BIBO se e solo se tutti i poli hanno parte reale strettamete negativa.

Questo significa che la stabilità asintotica garantisce anche la stabilità BIBO, anche viceversa.

## SISTEMA A POLI DOMINANTI
La risposta di un sistema è data da tutti i poli, ma alcuni di questi **contribuiscono maggiormente** alla risposta.
Si parla di un sistema a poli dominanti, quando è presente un **polo reale** o **una coppia di poli complessi coniugati** più vicina all'asse immaginario rispetto a tutti gli altri poli.

La funzione di risposta armonica, descrive alla variazione di omega la fase e l'ampiezza del segnale in ingresso.

