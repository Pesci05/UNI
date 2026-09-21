![[Pasted image 20260520102738.png|524]]
Un sistema di controllo è formato da più elementi:
- **CONTROLLORE**
	Può essere scritto come funzione C(s), poichè è un sistema dinamico il quale avrà una propria funzione di trasferimento.
- **ATTUATORE**
- **IMPIANTO** (MODELLO)

Un sistema di controllo ha come obiettivo **trovare l'entrata** U(s) di un sistema, però avendo un errore **piccolo** ( $e = y - y_{ref}$ ). 

Per capire se l'errore è ammissibile o no, si devono introdurre delle **regioni** in cui la variazione dell'uscita è ammissibile.
![[Pasted image 20260520104022.png|466]]

# CONTROLLO IN CATENA APERTA
Il **controllore deve sapere G(s) del sistema con cui lavora**, e ha come input $y_{ref}$ e **rappresenta il tipo di uscita che si vuole dal sistema**, per questo il controllore deve avere un **U(s) adatta ad adempiere a questo compito**.
![[Pasted image 20260520104530.png|480]]

Il controllore si ricava da:
$$
C(s)=\frac{1}{G(s)}G_{eq}(s)
$$
Idealmente l'uscita sarà data da:
$$
\begin{align} \\
\frac{Y(s)}{Y_{ref}(s)}=C(s)G(s) =G_{eq} \\
Y(s) = G_{eq}(s)Y_{ref}(s)
\end{align}
$$

Tuttavia il controllore o**pera senza possedere informazioni circa il reale andamento dell’uscita y(t),** diverso da quello ideale per effetto di:
- **Disturbi**
	Sono tutti quei **ingressi che non possono essere misurati**, i disturbi si sovrappongono agli input del sistema causando così un'uscita indesiderata.
	![[Pasted image 20260520110729.png|509]]
- **errori del modello G(s)**
- **Variazioni parametriche**
	Si intende la variazione di uno o piùcoefficienti dei polinomi a numeratore e/o denominatore delle funzioni di trasferimento


Infatti l'**uscita con il disturbo** sarà:
$$
	Y(s)=C(s)G(s)Y_{ref} + G_{2}(s)D(s) = G_{eq}(s)Y_{ref}(s)+G_{2}(s)D(s)
$$

Idealmente si ha $G(s) = G_{nom}(s)$, però in presenza di **errori sul modello** o **variazioni parametriche**, si ha $G(s)=G_{nom}(s) + \Delta G(s)$
Infatti l'uscita diventa:
$$
Y(s)=[G_{eq}(s)+\frac{G_{eq}(s)}{G_{nom}(s)}\Delta G(s)]*Y_{ref}(s)
$$
Il controllo a catena aperta **non è sempre possibile da costruire**, essendo che potrebbe avere più zeri che poli.

# CONTROLLO IN RETROAZIONE/CATENA CHIUSA
Il controllo in retroazione consente di fornire al controllore informazioni circa **l’andamento effettivo dell’uscita y(t)**.

**Sono reatroazionabili solo le variabili misurabili.**
![[Pasted image 20260520121932.png|595]]

Siccome non vi è nessuna dinamica sul ramo di retroazione, **il sistema complessivo si dice in retroazione unitaria**.

Si dice **guadagno ad anello** il prodotto di tutte le funzione di trasferimento nell'anello di retroazione. $L(s) =C(s)G(s)$

Il legame tra uscta $Y$ e uscita desiderata $Y_{ref}$ è data da:
$$
Y(s) = \frac{C(s)G(s)}{1+C(s)G(s)}Y_{ref}(s) = \frac{L(s)}{1+L(s)}Y_{ref}(s)
$$
Infatti il comportamento del sistema è controllato dal **controllore** e dalla **dinamica del sistema**

Ingressi ed uscite di un sistema di controllo a catena chiusa: [[AuIn07.1 - Controllo in Retroazione.pdf#page=21|AuIn07.1 - Controllo in Retroazione, pagina 21]]

Le **funzioni di sensitività** sono le funzioni di trasferimento che mettono in relazione gli ingressi di interesse con le uscite di interesse.

# SPECIFICHE DI CONTROLLO

## SPECIFICHE STATICHE
Per poter progettare un controllore è necessario stabilire delle richieste per il sistema in controllato, queste carattteristiche si chiamano **specifiche di controllo**, che definiscono il comportamento dell'uscita rispetto all'ingresso di riferimento.

Alcune di queste specifiche possono essere:
- **Stabilità**
	Il sistema contorllato deve essere asintoticamente stabile sia in condizioni nominali, sia in condizioni perturbate.
- **Prestazione**
[[AuIn07.2 - Controllo in Retroazione.pdf#page=4|AuIn07.2 - Controllo in Retroazione, pagina 4]]

Per trovare un **errore in stato di regime**, bisogna usare una formula che utilizza il teorema del valore finale come:
$$
\lim_{ t \to \infty } f(t) = \lim_{ s \to 0 } sF(s)
$$

[[AuIn07.2 - Controllo in Retroazione.pdf#page=7|AuIn07.2 - Controllo in Retroazione, pagina 7]]

Quelle appena viste vengono dette **specifiche statiche** e specificano l'errore a regime, che viene rappresentato come $e(t)=y_{ref}(t)-y(t)$, caratterizzando coì il $\lim_{ t \to \infty }e(t)$ essendo y(t) un segnale canonico.	L'errore dipende dal **tipo di L(s), cioè il numero di poli all'rigine di C(s)G(s).**

## SPECIFICHE DINAMICHE
Le specifiche dinamiche fanno riefimento al **tempo di assestamento e alla massima sobraelongazione percentuale** della risposta al riferimento a un gradino di un sistema, questi dipendono dai **poli del sistema controllato**.

**==NEL CASO DI UN SISTEMA DEL PRIMO ORDINE==**
![[Pasted image 20260527155203.png]]

I poli del sistema controllato si ricavano dall'equazione caratteristica:
$$
1+C(s)G(s)=0 \to 1+L(s)=0
$$
Bisogna capire come C(s) influenza i poli di $G_{cl}(s)$.
[[AuIn08.1 - Luogo delle radici.pdf#page=7|AuIn08.1 - Luogo delle radici, pagina 7]]
In questo caso i poli del sistema variano al variare del guadagno k, che verrà considerato sempre positivo.

Per questo la funzione sarà:
$$
\begin{align}
G_{cl}(s)=\frac{k}{s+2+k} \\ \\
poli \to s+2+k = 0 \to s=-2-k \\
\end{align}
$$

**==NEL CASO DI UN SISTEMA DEL SECONDO ORDINE==**
![[Pasted image 20260527160430.png]]
[[AuIn08.1 - Luogo delle radici.pdf#page=12|AuIn08.1 - Luogo delle radici, pagina 12]]

Il **lugo delle radice**, è lo strumento che permette di capire come variano i poli nel piano dei numeri complessi, per un sistema controllato in retroazione.


### PROPRIETÀ
1. Il luogo delle radici avrà un **numero di rami** pari a quello dei poli del sistema in catena aperta.
2. Ogni ramo:
	- Parte da una posizione di un **polo** in catena aperta
	- Termina nella posizione di un **zero** del sistema o va **all'infinito**
3. Il luogo è **simmetrico** rispetto all'asse reale
4. Un **punto sull'asse reale** appartiene al luogo se lascia a destra un numero dispari di singolarità
5. Ha **asintoti** in numero pari al grado relativo
6. Gli asintoti si incontrano in un punto dell'asse reale e formando un **stella** con gli angoli di tutti uguali tra loro, il loro punto d'incontro è $\sigma_{asintoti}=\frac{1}{n-m}\left( \sum^n_{i=1}p_{i} - \sum^m_{i=1}z_{i}  \right)$
7. Gli asintoti formano con l'asse reale gli angoli $\theta_{a,v}=\frac{(2v+1)\pi}{n-m}$ fino ad avere $V=0,1,2\dots,n-m-1$  dove n e m rappresentano rispettivamente il numero di poli e zeri del sistema in catena aperta

==**COME TRACCIARE IL LUOGO DELLE RADICI**==: [[AuIn08.1 - Luogo delle radici.pdf#page=22|AuIn08.1 - Luogo delle radici, pagina 22]]
V viene calcolato tante volte quanto sono gli asintoti
$$
V= 0,1,2,3\dots,n-m-1
$$
Dove la prima volta è 0, invece l'ultima sarà n-m-1.

Il **luogo delle radici** evidenzia il variare dei poli della $G_{cl}(s)$ e non descrive la G(s).

# PROGETTAZIONE DI UN CONTROLLORE
Progettare un controllore signicica costrure la funzione di trasferimento C(s) del controllore, tale che soddisfi **specifiche statiche(ERORRE A REGIME)** e dinamiche, 

## SPECIFICHE DINAMICHE
Specifiche relative al transitorio della risposta.
Tipicamente queste specifiche vengono **date in termini di massima sovraelongazione percentuale e massimo tempo di assestamento.**
Significa che i poli della $G_{cl}(s)$ devono trovarsi in alcune regioni del piano.
**Luogo delle Radici** $\to$ strumento che descrive come si muovono i poli di $G_{cl}(s)$ nel piano.

La posizione dei poli è determinata dalla **pulsazione naturale** $\omega_{n}$, e dal **coefficiente di smorzamento** $\delta$. **==[[SISTEMI ELEMENTARI#RISPOSTA GRADINO 2° ordine|Sistemi del secondo ordine]]==**
![[Pasted image 20260528120200.png|326]] 

## COSTRUZIONE DEL CONTROLLORE
1. Aggiungere un numero sufficiente di poli nell'origine affinchè il tipo del guadagno d'anello consenta di soddisfare le specifiche statiche $C_(s)=k \frac{1}{s^h}$
	[[AuIn08.2 - Progettazione del controllore.pdf#page=10|AuIn08.2 - Progettazione del controllore, pagina 10]]

2. **Tradurre le specifiche dinamiche in regioni del piano**.
	[[AuIn08.2 - Progettazione del controllore.pdf#page=11|AuIn08.2 - Progettazione del controllore, pagina 11]]

3. Verificare se al **variare di k**  esistono dei **poli che sono all'interno della regione di ammissibilità,** grazie al luogo delle radici.                                                                        [[AuIn08.2 - Progettazione del controllore.pdf#page=12|AuIn08.2 - Progettazione del controllore, pagina 12]]

4. Se per **ogni valore di k i poli non sono all'interno della regione ammissibilità**, **aggiungere zeri e poli al controllore** così da **modificare controllore** e guadagno ad anello **fino a quando almeno un polo sia all'interno della regione di ammissibilità.** [[AuIn08.2 - Progettazione del controllore.pdf#page=13|AuIn08.2 - Progettazione del controllore, pagina 13]]
